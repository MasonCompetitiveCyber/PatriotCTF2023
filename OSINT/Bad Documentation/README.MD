# Bad Documentation

### Description

I heard that this security researcher accidentally leaked his password in his documentation, but he deleted all the files in his repository so now we don't have access to it anymore! I'm pretty sure it's hopeless, but if you think you can find it here's the link to the repo: https://github.com/Th3Burn1nat0r/vuln. 

### Difficulty
3/10 (Easy)

### Flag
PCTF{N0_c0D3's_2VeRy_R3aLlY_G0n3}

### Hints
None

### Author
Migyaksuil (Maxime Bonnaud)

### Tester
Txnn3r (Tanner Leventry)

### Learning Objectives
This was actaully based on a real-life situation where a security researcher leaked their password in some old Github files, the only thing I changed was the password. Basic authentication is still in use by some routers to this day and is effectively equivalent to plaintext transmission for security.

### Writeup

Look at the deleted files (under commits) and look at the image. Basic authentication is literally just base64, if you decode this: YWRtaW46UENURntOMF9jMEQzJ3NfMlZlUnlfUjNhTGxZX0cwbjN9 you get admin:PCTF{N0_c0D3's_2VeRy_R3aLlY_G0n3}.
