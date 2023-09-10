from random import random

string = 'MasonCC'
flag = 'PCTF{M0r3!_C0mpET1tIve_CyB3R_@_M4$$on}'

values = {'M':5, 'a':3, 's':8, 'o':4, 'n':7, 'C':1}
lines = []
secret = '01011001 01101111 01110101 00100111 01110010 01100101 00100000 01101000 01100001 01101100 01100110 01110111 01100001 01111001 00100000 01110100 01101000 01100101 01110010 01100101 00101100 00100000 01101110 01101111 01110111 00100000 01110101 01110011 01100101 00100000 01110100 01101000 01100101 01110011 01100101 00100000 01101110 01110101 01101101 01100010 01100101 01110010 01110011 00100000 01110100 01101111 00100000 01110011 01101111 01101100 01110110 01100101 00100000 01110100 01101000 01100101 00100000 01110010 01100101 01110011 01110100 00111010 00100000 00110101 00100000 00110011 00100000 00111000 00100000 00110100 00100000 00110111 00100000 00110001'
i=0
while i < len(flag):
    temp = ''
    count=0
    for j in string:
        temp += j*(int(random()*10)+1)
    for j in temp:
        count += values[j]
    if count == ord(flag[i]):
        i+=1
        lines.append(temp)

count=0
zero = '\u2062'
one = '\u2063'
space = '\u200D'
for i in lines:
    for j in i:
        print(j, end='')
        if (random()*10)>2.2:
            if count < len(secret):
                if(secret[count] == '0'):
                    print(zero, end='')
                    count+=1
                elif(secret[count] == '1'):
                    print(one, end='')
                    count+=1
                else:
                    print(space, end='')
                    count+=1
    print()

print()
print(count)
print(len(secret))