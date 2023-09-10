#!/usr/bin/env python
enc_msg = """A Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code, 
or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type 
of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number 
of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would 
become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
pctf{vM_r3v3rs1ng_g0t_a_l1ttl3_harder}
The Vigenere cipher is a method of encrypting alphabetic text where each letter of the plaintext 
is encoded with a different Caesar cipher, whose increment is determined by the corresponding 
letter of another text, the key.
The Vigenere cipher is therefore a special case of a polyalphabetic substitution."""

print(enc_msg[::-1], end="")