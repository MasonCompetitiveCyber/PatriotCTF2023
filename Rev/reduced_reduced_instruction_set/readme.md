### Description
I heard RISC was pretty good, so I reduced it some more! Check out my password checker program I wrote with it.

### Difficulty
7/10 (Difficult)

### Flag
pctf{vm_r3vers3inG_1s_tr1cky}

### Author
Christopher Roberts (caffix)

### Tester
me?

### Writeup
It's a simple VM reversing problem.
Figure out how it's decodeing and executing instruction.
Then either figure out how to set breakpoints on the cmp instructions
or follow along with my factorization inside the VM.

### Solve
bash solve.sh

Then each of the numbers used is actually 4 byte chunks of the flag eg
1885566054 is 0x70637466 which is "pctf"

### Given to user
- vm
- password_checker.smol
