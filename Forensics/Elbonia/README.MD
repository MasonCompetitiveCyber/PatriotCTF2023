# Elbonia

### Description
The Kingdom of Elbonia has intercepted a transfer of an encoded message, but they can't seem to break the code. They have tasked you with recovering the hidden message, it is of the utmost importance that you crack it. Good luck brave warrior!

### Difficulty 
5/10 (Medium)

### Flag
PCTF{53cr3t_c0d3_1n_p0rt5}

### Hints
None

### Author
Txnn3r (Tanner Leventry)

### Tester
None yet

### Writeup
`tshark -r message.pcapng -T fields -e udp.dstport | tr '\n' ' ' > file`

find the string '80 67 84 70 123' in the file (ASCII codes for `PCTF{`).

delete everything before that string (conversion can sometimes get messed up otherwise)

Alternatively you can also look for the ending bracket, `125 in ascii code`.

paste into https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html (or any other website / script for ASCII conversion) and the flag will appear!

#### Note 
There is almost certainly a way to do this with one long linux command.
