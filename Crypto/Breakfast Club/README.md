# Breakfast club
As the sysadmin for your college, you're responsible for overseeing the security of all the clubs. One of the on campus orginizations is a breakfast club with their own personal website that the leader insured you was "unhackable". He was so sure of this, that he sent you an example of how hashes are stored in the database, something about "changing the hash type multiple times for each password" or something like that. Can you crack the password and prove him wrong?

## Difficulty: 4/10
## Flag: PCTF{H@5H_8R0WNS}
## Matthew Johnson #meatball5201
## Write Up Time
For this challenge, the user is given a txt file containing a list of hashes they must crack. Each hash is a single letter of the flag, and the respective hash type is listed before it. To solve the challenge, it's easiest to load the file using a python script, and brute force each hash with the pycryptodome library. An example of this is in the file solution/solve_breakfast.py