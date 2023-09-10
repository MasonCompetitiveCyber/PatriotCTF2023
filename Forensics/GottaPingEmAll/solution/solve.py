import binascii

fhex = open("imagehex.txt", "r").readlines()[0].split(",")

fhex[0] = fhex[0][2:]
fhex[-1] = fhex[-1][:-1]

fnum = open("portnumbers.txt", "r").readlines()[0].split(",")

del fnum[-1]

map = {}
for i in range(len(fhex)):
    map[int(fnum[i])] = binascii.unhexlify(fhex[i]).decode()

image = ''
i=1
while i <= len(map):
    image += map[i]
    i+=1

hexout = open("image.jpg", "wb")
hexout.write(binascii.unhexlify(image))
