# Secret Wall Code

### Description
We found this werid symbol language in a secret backroom wall. We have scanned the symbols and need your help figuring what it means. We were able to figure out one symbol.


### Difficulty
6/10 (Medium)

### Flag
pctf{fnaf_is_pretty_insane}
not case sensitive

### Hints
Riddle to help find the key
We found papers scattered around with writing on them. It seems to be some sort of riddle.
Alpha Z, 6 groups
Reverse 5 3 1
Then Z to E
Start at end, Alternate Back, Loop

### Author
ShadowBringer007 (Ryan Wong)

### Tester
txnn3r (Tanner Leventry)

### Writeup
The Security Breach Secret Wall Code does not have an online decoder. You will have to find reddit post or youtube videos to find the Key. 
Links are here:
https://www.youtube.com/watch?v=bYXi9evimPs
https://www.reddit.com/r/GameTheorists/comments/ro9yi1/fnaf_security_breach_coded_wall_message_solved/
https://www.reddit.com/r/fivenightsatfreddys/comments/rnwxa6/can_someone_explain_how_that_letter_means_e_from/
https://www.youtube.com/watch?v=eQZSSRImJdw

Manual Solving:
Steps to get the Key if cannot find on the internet
Step One:
Break Alphabet into 6 Groups with Z on its own
A B C D E | 
F H G I J | 
K L M N O | 
P Q R S T | 
U V W X Y | 
Z

Step Two:
Every other Row Reverse
E D C B A | 
F G H I J | 
O N M L K | 
P Q R S T | 
Y X W V U | 
Z

Step Three:
Reverse The Entire time
Z | 
U V W X Y | 
T S R Q P | 
K L M N O | 
J I H G F | 
A B C D E | 

Step Four:
Start at end, Alternate Back, Loop
E C A G I | 
O M K Q S | 
Y W U D B | 
F H J N L | 
P R T X V | 
Z

Create a variation of the pigpen cipher using hexagon
From the links above should be able to see the pattern.
Then it becomes a substitution cipher

