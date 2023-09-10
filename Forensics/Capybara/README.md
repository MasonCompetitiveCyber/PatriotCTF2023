# Capybara

### Description
What a cute picture of a capybara!

### Difficulty
2/10 (Easy)

### Flag
PCTF{d0_y0U_kN0W_h0W_t0_R34D_m0r53_C0d3?}

### Hints
1. could there Be somethINg hiding Within this imAge? very LiKely
2. What's that weird noise? Maybe a website will be able to tell me what it means.

### Author
Txnn3r (Tanner Leventry)

### Tester
None

### Given to user
capybara.jpeg

### Writeup

`binwalk -e capybara.jpeg`

`unzip audio.zip`

[morse code decoder](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)

(remove spaces) convert from hex > ascii