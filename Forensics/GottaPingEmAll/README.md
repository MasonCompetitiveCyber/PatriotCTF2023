### Description
Our SOC has recently discovered thousands of unusual packets being sent into our network from an unknown source. We have since traced the origin to a known APT group, however are still unable to determine the meaning behind the packets. You have been contracted to help investigate significance of the packets.

### Difficulty
8/10 (Hard)

### Flag
PCTF{Who's_that_pokemon?_ITS_PIKACHU!_9ce06f19a25}

### Hints
None

### Author
Tanner Leventry (Txnn3r)

### Tester
None

### Given to user
poke.pcapng

### Writeup
`tshark -r 'poke.pcapng' -T fields -e tcp.checksum | tr "\n" " " | sed 's/ 0x/,/g' > imagehex.txt`

`tshark -r 'poke.pcapng' -T fields -e tcp.dstport | tr "\n" "," > portnumbers.txt`

run solve.py (located in 'solution' folder)

copy hex data from after end of jpg file (after FF D9 hex bytes)

![image](https://github.com/MasonCompetitiveCyber/patriotctf2023-private/assets/101006959/92adb3ae-a238-4ba4-8035-eb2c531a5a42)

cyberchef: from hex > to binary > bit flip (0's become 1's, 1's become 0's) > from binary

![image](https://github.com/MasonCompetitiveCyber/patriotctf2023-private/assets/101006959/2d2e7e0f-1757-46f8-a1d9-6ac9e487a9f0)

Alternative solution: Instead of cyberchef, paste the hex in the [Boxentriq Hex Analysis Tool](https://www.boxentriq.com/code-breaking/hex-analysis)
