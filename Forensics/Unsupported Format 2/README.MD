# Unsupported Format 2

### Description
Who doesn't love the classic Windows background!

### Difficulty
7/10 (Hard)

### Flag
PCTF{00ps_1_L1ed_Th3r3_1s_4_Fl4g}

### Hints
Hint 1: It can't be that easy... right? 

Hint 2: I wonder what ways a flag could be hidden inside of an image?

### Author
Txnn3r (Tanner Leventry)

### Tester
None yet

### Writeup

First let's remove those pesky "CORRUPTED" bytes at the top of the hex data.
![image](https://user-images.githubusercontent.com/101006959/227111212-7506d39d-0d02-4056-b954-d63a16694426.png)

After doing so we should see the windows 95 background but still no flag.
![image](https://user-images.githubusercontent.com/101006959/227111235-251224d1-4973-4154-9d6c-99ba3c2f29fa.png)

If we scroll down towards the bottom of the hex dump (or run strings) we can see that there is still multiple "CORRUPTED" bits at the bottom.
If we find the top of the "CORRUPTED" section, we can see a "PK" right before the first set of "CORRUPTED" bytes, looking in-between the "CORRUPTED" bytes, we can see more header info.
aha! this must be a hidden .zip file (header = 50 4B 03 04).
Let's remove everything before the zip file header and see if we can find a way to uncorrupt it.
![image](https://user-images.githubusercontent.com/101006959/227111281-576e620b-5a72-411c-9dfe-6297b392d4f3.png)

There doesn't seem to be any easy way to remove the bits manually, we might have to write a script to do this for us. Luckily I have included "uncorrupt_solution.py" for this very purpose!

![image](https://user-images.githubusercontent.com/101006959/227111664-d45c8b87-b0ab-46ce-9383-b18f0dfeeb64.png)

Running the script will give us the output file "uncorrupted.zip", and extracting the zipped contents we can see another jpeg image, "Monitor.jpg"!
![image](https://user-images.githubusercontent.com/101006959/227111461-47637fc3-bcf8-4cb5-b9ac-51e21d44acfa.png)

Not a flag? UGH. That can't be right, was this all just a red herring? Nope! (sorry!). Let's test your steg knowledge.
With a little trial and error, we can find the right tool for the job, in this case it's stegsolve.jar (https://github.com/zardus/ctf-tools/blob/master/stegsolve/install).
If we scroll through the RBG planes we can see that there is most definetly something hidden in the image, on the monitor.
![image](https://user-images.githubusercontent.com/101006959/227111501-920ed232-d788-421c-a07f-d6851c7ed55f.png)

Finally: Scrolling to "Blue plane 2" will give us a clear view of the flag!
