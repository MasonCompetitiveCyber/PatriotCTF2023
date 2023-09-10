f = open('MasonCompetitiveCyber2.txt', 'rb')
f = f.readlines()

values = {'M':5, 'a':3, 's':8, 'o':4, 'n':7, 'C':1}
keys = "".join(list(values.keys()))
flag = ''
for row in f:
    line = str(row)[2:-1]
    temp = ''
    i=0
    while i < len(line):
        if line[i] in keys:
            temp += line[i]
            i+=1
        else:
            i+=4
    num=0
    for char in temp:
        num += values[char]
    flag += chr(num)

print(flag)

