import binascii
from scapy.all import *
from random import *

with open('pikachu.jpg', 'rb') as f: # note: bit flipped flag was placed at the end of pikachu.jpg manually.
    hexdata = binascii.hexlify(f.read())
hexdata = hexdata.decode()

i=0
maps = {}
j=1
while i < len(hexdata):
    maps[j] = hexdata[i]+hexdata[i+1]
    i += 2
    j+=1

pokef = open("pokemon-list-en.txt", "r").readlines()
for i in range(len(pokef)):
    pokef[i] = pokef[i].strip()

while len(maps) > 0:
    index = choice(list(maps.keys()))
    pokechoice = list(choice(pokef) + "1234567890")
    shuffle(pokechoice)
    cpoke = ''.join(pokechoice)
    cpoke = choice(pokef) + "_" + cpoke + "_" + choice(pokef)
    send(IP(src='127.0.0.1', dst='127.0.0.1')/ TCP(sport=1337, dport=index, chksum=RawVal(maps[index])) / cpoke)
    del maps[index]

print("Done!")
