from random import random

string = 'MasonCC'

zero = '\u200C'
one = '\u200D'
space = '\uFEFF'
count=0
flag = '01010000 01000011 01010100 01000110 01111011 01001101 01000000 01110011 00100100 00110000 01001110 01011111 01000011 01001111 01101101 01010000 00110011 01110100 00110001 01110100 00110001 01010110 01000101 01011111 01000011 01011001 01000010 00110011 01110010 00100001 01111101'
for i in range(38):
    for j in string:
        #print(int(random()*10)+1)
        print(j*(int(random()*10)+1), end='')
        if(random()*10>5.2):
            for i in range(2):
                if count < len(flag):
                    if(flag[count] == '0'):
                        print(zero, end='')
                        count+=1
                    elif(flag[count] == '1'):
                        print(one, end='')
                        count+=1
                    else:
                        print(space, end='')
                        count+=1
    print()
print()
print(count)
print(len(flag))