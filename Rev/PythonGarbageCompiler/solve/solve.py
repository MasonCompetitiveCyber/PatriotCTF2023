from random import *
seed(10)

flag = open('output.txt', 'r').readlines()[0]

i=0
temp = ''
while i < len(flag):
    try:
        temp += flag[i+1] + flag[i]
    except:
        temp += flag[i]
    i+=2

temp = list(temp)
temp.reverse()
flag = "".join(x for x in temp)


if flag == "y>dd0fX-886Su\\Nb$![oK=%jEz(]>h+VVeq^s":
    print("Final Stage solved")
    
temp = ''
rand = []
for i in range(len(flag)):
    temp += chr(ord(flag[i])+randint(0,5))
flag = temp

if flag == "}>gg4fY0;:;Tu`Qd$\"`qK@&nG}+_Cj.W[gv`t":
    print("Stage 2 solved")

flag = list(flag)
for i in range(len(flag)):
    flag[i] = chr(ord(flag[i])^i)
flag = "".join(x for x in flag)

if flag == "}?ed0c_7331_ym_k43rb_U0y_d1D_w0H{FTCP":
    print("Stage 1 solved")

flag = list(flag)
flag.reverse()
flag = "".join(x for x in flag)

if flag == "PCTF{H0w_D1d_y0U_br34k_my_1337_c0de?}":
    print("Challenge solved!")
    print(flag)