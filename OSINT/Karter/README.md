### Challenge Name
karter

### Description
In 2021, Flipkart added a new director. Your task is to find:

    1. his last name (UPPERCASE)
    2. his Director Identification Number
    3. And the URL of the primary source (URL format: scheme://subdomain.rootdomain.tld) paths excluded

Flag Format: PCTF{LASTNAME_IdentificationNumber_Url}

### Difficulty
5/10

### Flag
PCTF{COLLINS_09075331_https://www.mca.gov.in}

### Hints
N/A

### Author
Kiran Ghimire

### Tester
Tested by <>

### Writeup
1. Find the Flipkart CIN number from footer: https://www.flipkart.com/
2. CIN: U51109KA2012PTC066107
3. Go to: https://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do
4. Click on Master Data -> View Company/LLP Master Data
5. Put the CIN number and submit
6. Scroll
7. The director who joined in 2021 is "JONATHAN MARSHALL COLLINS"




