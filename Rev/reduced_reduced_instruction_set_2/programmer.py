import struct
FILE_HEADER = b"SMOL"

def exit(f, dst, src):
    f.write(b"\x0c")
    f.write(dst)
    f.write(src)
    f.write(b"\x00")

def mov(f, dst, src):
    f.write(b"\x00")
    f.write(dst)
    f.write(src)
    f.write(b"\x00")

def add(f, dst, src, imm):
    f.write(b"\x01")
    f.write(dst)
    f.write(src)
    f.write(struct.pack("<B",imm))

def addi(f, dst, src, imm):
    f.write(b"\x0b")
    f.write(dst)
    f.write(src)
    f.write(struct.pack("<B",imm))

def subi(f, dst, src, imm):
    f.write(b"\x12")
    f.write(dst)
    f.write(src)
    f.write(struct.pack("<B",imm))

def movi(f, dst, src, imm):
    f.write(b"\x04")
    f.write(dst)
    f.write(src)
    f.write(struct.pack("<B",imm))

def prnt_reg(f, dst, src):
    f.write(b"\x03")
    f.write(dst)
    f.write(src)
    f.write(b"\x00")

def push(f, dst, src, imm):
    f.write(b"\x05")
    f.write(dst)
    f.write(src)
    f.write(b"\x00")

def pop(f, dst, src, imm):
    f.write(b"\x06")
    f.write(dst)
    f.write(src)
    f.write(b"\x00")

def mul(f, dst, src, imm):
    f.write(b"\x0a")
    f.write(dst)
    f.write(src)
    f.write(imm)

def write_ins(f, imm):
    f.write(b"\x09")
    f.write(b"\x00")
    f.write(b"\x00")
    f.write(struct.pack("<B",imm))

def getnum(f, dst, src, imm):
    f.write(b"\x0d")
    f.write(b"\x00")
    f.write(b"\x00")
    f.write(struct.pack("<B",imm))

def cmp(f, dst, src, imm):
    f.write(b"\x07")
    f.write(dst)
    f.write(src)
    f.write(struct.pack("<B",imm))

def jz(f, dst, src, imm):
    f.write(b"\x08")
    f.write(b"\x00")
    f.write(struct.pack("<B",(imm >> 8))) # imm >> 8
    f.write(struct.pack("<B",(imm & 0xFF)))

def getchar(f, dst, src, imm):
    f.write(b"\x10")
    f.write(dst)
    f.write(b"\x00")
    f.write(struct.pack("<B",imm))

def shl(f, dst, src, imm):
    f.write(b"\x11")
    f.write(dst)
    f.write(b"\x00")
    f.write(struct.pack("<B",imm))

def xor(f, dst, src, imm):
    f.write(b"\x0e")
    f.write(dst)
    f.write(src)
    f.write(struct.pack("<B",imm))

def mod(f, dst, src, imm):
    f.write(b"\x13")
    f.write(dst)
    f.write(src)
    f.write(struct.pack("<B",imm))

def push_val(f,reg,num):
    num_factors = factors(num)[-2:]
    # print(num_factors)
    # print(factors(num))
    if num < 0xFF:
        movi(f,reg,reg,num)
        push(f,reg,reg, 0)
    # elif num < (0xFF*0xFF):
    elif num_factors[0] < 0xFF and num_factors[1] < 0xFF:
        # num_factors = factors(num)[-2:]
        # print(num_factors)
        movi(f,b"\x00",b"\x00",num_factors[0])
        movi(f,b"\x01",b"\x01",num_factors[1])
        mul(f,b"\x00",b"\x01",b"\x00")
        # mov(f,reg,b"\x00")
        push(f,reg,reg, 0)
    elif (num_factors[1] == num):
        num_factors = factors(num-1)[-2:]
        # print(num_factors)
        # print(num)
        push_val(f,reg,num+1)
        pop(f,reg,reg,b"\x00")
        # addi(f,reg,reg, 1)
        subi(f,reg,reg, 1)
        push(f,reg,reg, 0)
    else:
        # num_factors = factors(num)[-2:]
        push_val(f,b"\x00",num_factors[0])
        push_val(f,b"\x00",num_factors[1])
        pop(f,b"\x02",b"\x00", b"\x00")
        pop(f,b"\x03",b"\x00", b"\x00")
        mul(f,b"\x02",b"\x03",b"\x00")
        mov(f,reg,b"\x02")
        push(f,reg,reg, 0)

# pctf {vm_ r3ve rs3i nG_1 s_tr 1cky }000
# pctf{vm_r3vers3inG_1s_tr1cky}000

# 70637466 7b766d5f
# 72337665 72733369
# 6e475f31 735f7472
# 7d303030

# msg = "What's the password?\n"
def puts(f, msg):
    for x in range(0, len(msg), 4):
        chunk = msg[x:x+4]
        chunk = chunk[::-1]
        chunk_hex = chunk.encode().hex()
        chunk_num = int(chunk_hex,16)
        push_val(f, b"\x00", chunk_num)
        write_ins(f, 4)
        pop(f, b"\x04",b"\x04",b"\x00")

def num_to_stack(f):
    getnum(f, b"\x00", b"\x00", 0)
    push(f,b"\x00",b"\x00", 0)

def factors(x):
    # We will store all factors in `result`
    result = []
    i = 1
    # This will loop from 1 to int(sqrt(x))
    while i*i <= x:
        # Check if i divides x without leaving a remainder
        if x % i == 0:
            result.append(i)
            # Handle the case explained in the 4th
            if x//i != i: # In Python, // operator performs integer/floored division
                result.append(x//i)
        i += 1
    # Return the list of factors of x
    return result

def make_flag(password):

    encoded_flag = []
    for x,char in enumerate(password):
        if x != 0:
            val = ord(char) ^ encoded_flag[x-1]
            # val = ord(char) ^ ord(encoded_flag[x-1])
            temp = x % 0xFF
            val = val + temp
            val = val % 0xFF
            # val = (val + (x % 0xFF)) % 0xFF
        else:
            val = (ord(char) + (x % 0xFF)) % 0xFF
        encoded_flag.append(val)
    # print("".join(encoded_flag))
    return encoded_flag

def read_len(f, count):
    for x in range(count):
        getchar(f, b"\x00", b"\x00", 0)
        # shl(f, b"\x00", b"\x00", (64-8))
        push(f, b"\x00", b"\x00", 0)

def write_char(f, count):
    for x in range(count):
        write_ins(f, 4)
        # pop(f, b"\x00", b"\x00", 0)
# pctf{vM_r3v3rs1ng_g0t_a_l1ttl3_harder}
def main():
    # key = "pctf{vM_r3v3rs1ng_g0t_a_l1ttl3_harder}"
    enc_text = """A Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code, 
or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type 
of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number 
of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would 
become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
pctf{vM_r3v3rs1ng_g0t_a_l1ttl3_harder}
The Vigenere cipher is a method of encrypting alphabetic text where each letter of the plaintext 
is encoded with a different Caesar cipher, whose increment is determined by the corresponding 
letter of another text, the key.
The Vigenere cipher is therefore a special case of a polyalphabetic substitution."""
# The Vigenère cipher is therefore a special case of a polyalphabetic substitution."""
    print(len(enc_text))
    encoded_flag = make_flag(enc_text)
    with open("password_checker2.smol", 'wb') as f:
        f.write(FILE_HEADER)

        # Rolling XOR

        # puts(f, "The Vigenère cipher is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher, whose increment is determined by the corresponding letter of another text, the key.\n")
        # puts(f, "Wrong!") # 288 -4
        # exit(f,b"\x00", b"\x00") # 292 -4

        puts(f, "Can you figure out what I'm saying?\n")
        read_len(f, len(encoded_flag))
        print("If you're recreating this problem this step takes a HOT minute.")
        for x in range(len(encoded_flag)):
            pop(f,b"\x00",b"\x00",b"\x00")
            push(f,b"\x00",b"\x00",0)
            # mov(f,b"\x04",b"\x00")
            if x != 0:
                movi(f,b"\x01",b"\x01",encoded_flag[x-1])
                # prnt_reg(f, b"\x00", b"\x04")
                # prnt_reg(f, b"\x01", b"\x04")
                xor(f, b"\x00", b"\x01",0) # val = ord(char) ^ encoded_flag[x-1]
                movi(f,b"\x02",b"\x02",x % 0xFF) # tmp = x % 0xFF
                add(f, b"\x00", b"\x02", 0) # val += tmp
                movi(f,b"\x01",b"\x01",0xFF) 
                mod(f,b"\x00",b"\x01",0) # val = val % 0xFF
            else:
                movi(f,b"\x02",b"\x02",x % 0xFF)
                add(f, b"\x00", b"\x02", 0)
                movi(f,b"\x01",b"\x01",0xFF)
                mod(f,b"\x00",b"\x01",0)
            movi(f, b"\x01",b"\x00", encoded_flag[x])

            # pop(f,b"\x04",b"\x00",b"\x00")
            # Right label
            # prnt_reg(f, b"\x04", b"\x04")

            cmp(f,b"\x00",b"\x01",0)
            jz(f,b"\x00",b"\x01",288)
            # jz(f,b"\x00",b"\x01",288)
            # Wrong label
            puts(f, "Wrong!") # 288 -4
            exit(f,b"\x00", b"\x00") # 292 -4
            write_ins(f,4)
            pop(f,b"\x04",b"\x00",b"\x00")
            # Right label
            # prnt_reg(f, b"\x04", b"\x04")
        puts(f, "That's Correct!\n")
        exit(f,b"\x00", b"\x00")

        # write_char(f, 20)
        # getchar(f, b"\x00", b"\x00", 0)
        # push(f, b"\x00", b"\x00", 0)
        # pop(f,b"\x01",b"\x01",b"\x00")
        # prnt_reg(f, b"\x01",b"\x01")
        
        # for x,y in password.items():
        #     puts(f, "What's the {} password?\n".format(x))
        #     num_to_stack(f)
        #     push_val(f, b"\x03", y)
        #     pop(f,b"\x00",b"\x00",b"\x00")
        #     pop(f,b"\x01",b"\x00",b"\x00")
        #     cmp(f,b"\x00",b"\x01",0)
        #     jz(f,b"\x00",b"\x01",4)
        #     exit(f,b"\x00", b"\x00")

        # puts(f, "Congrats! Passwords look good how do they fit together into the flag?\n")
        # exit(f,b"\x00", b"\x00")


if __name__ == "__main__":
    main()