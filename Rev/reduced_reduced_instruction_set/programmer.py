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

def addi(f, dst, src, imm):
    f.write(b"\x0b")
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
    f.write(b"\x00")
    f.write(struct.pack("<B",imm))

def push_val(f,reg,num):
    num_factors = factors(num)[-2:]
    print(num_factors)
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
        push_val(f,reg,num-1)
        pop(f,reg,reg,b"\x00")
        addi(f,reg,reg, 1)
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
# 31636b79 7d303030

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

# 0x70637466 0x7b766d5f
# 0x72337665 0x72733369
# 0x6e475f31 0x735f7472
# 0x31636b79 0x7d303030
def main():
    print(factors(0x70637466)[-2:])
    with open("password_checker.smol", 'wb') as f:
        f.write(FILE_HEADER)

        password = {
            "first" : 0x70637466,
            "second" : 0x7b766d5f,
            "third" : 0x72337665,
            "fourth" : 0x72733369,
            "fifth" : 0x6e475f31,
            "sixth" : 0x735f7472,
            "seventh" : 0x31636b79,
            "eigth" : 0x7d303030,
        }

        for x,y in password.items():
            puts(f, "What's the {} password?\n".format(x))
            num_to_stack(f)
            push_val(f, b"\x03", y)
            pop(f,b"\x00",b"\x00",b"\x00")
            pop(f,b"\x01",b"\x00",b"\x00")
            cmp(f,b"\x00",b"\x01",0)
            jz(f,b"\x00",b"\x01",4)
            exit(f,b"\x00", b"\x00")

        puts(f, "Congrats! Passwords look good how do they fit together into the flag?\n")
        exit(f,b"\x00", b"\x00")


if __name__ == "__main__":
    main()