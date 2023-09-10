### Description
I added a couple improvements to my reduced reduced instruction set and have another password checker program for your to check out!

### Difficulty
10/10 (Difficult)

### Flag
pctf{vM_r3v3rs1ng_g0t_a_l1ttl3_harder}

### Author
Christopher Roberts (caffix)

### Tester
me?

### Writeup
It's a VM reversing problem.
There are more instructions to reverse/decode and this is a HUGE
program. (300K lol) So you need some automation to fully decode the cipher I wrote.

You COULD side-channel it, but the full message is 840 characters long so
your side channel would take forever.

The cipher itself is pretty simple, but the "message" is gigantic (840 bytes) and you need to pull
"key" pieces out of the binary.
```python
def make_flag(password):
    encoded_flag = []
    for x,char in enumerate(password):
        if x != 0:
            val = ord(char) ^ encoded_flag[x-1]
            val = (val + (x % 0xFF)) % 0xFF
        else:
            val = (ord(char) + (x % 0xFF)) % 0xFF
        encoded_flag.append(val)
    return encoded_flag
```

### Solve
python solve.py | ./vm2 password_checker2.smol

### Given to user
- vm2
- password_checker2.smol
