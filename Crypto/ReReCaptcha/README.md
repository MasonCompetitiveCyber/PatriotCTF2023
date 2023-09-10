# ReReCaptcha
Boy these captcha's are getting out of hand! First it was some numbers and letters, then they wanted me to find all the crosswalks and stoplights, now, I just got these 4 images in a zip file as the captcha.

## Difficulty: 3/10
## Flag: PCTF{I_H0P3_U_U53D_0CR!}
## Hints:
- Rivest, Shamir, and Adleman love this challenge
## Matthew Johnson #meatball5201
## Tester: TBD
## Write Up Time
The goal for this challenge is to decrpyt the RSA cipher text contained in the images. Each image is named after the respective variable needed to solve the cipher text, P, Q, E, and the cipher text itself.
While you could in theory manually copy down the numbers in the images, it's far easier to use an OCR (Optical Character Recognition) program like Tesseract. Using the command `tesseract [input.png] out`, all of the numbers from the images can be converted text files. From there, all thats needed is a bit of manual clean up, then they're ready to go.

The next part is just standard RSA decryption and can be found on the [wikipedia page](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Decryption) for RSA.
Using the P, Q, and E values, the CT can be decrypted to the flag `PCTF{I_H0P3_U_U53D_0CR!}`. Python code for this decryption can be found in the solveocr.py
