import string

strings = string.ascii_lowercase

x_add = {}
x_orr = {}
x_xor =  {}

for i in strings:
    for j in strings:
        add = ord(i) & ord(j)
        if add == 0x60:
            x_add[i+j] = add
        orr = ord(i) | ord(j)
        if orr == 0x61:
            x_orr[i+j] = orr
        xor = ord(i) ^ ord(j)
        if xor == 0x6:
            x_xor[i+j] = xor
final_one = []

for i in x_add:
    for j in x_orr:
        for k in x_xor:
            ok = i+j+k
            final_one.append(ok[0]+ok[2]+ok[1]+ok[4]+ok[3]+ok[5])
print(final_one)
print(f"length : {len(final_one)}")
