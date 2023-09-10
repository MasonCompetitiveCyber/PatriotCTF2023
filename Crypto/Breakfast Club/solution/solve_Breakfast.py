from Crypto.Hash import SHA, SHA1, MD2, MD4, MD5, SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_384, SHA3_512, TupleHash128, TupleHash256, BLAKE2s, BLAKE2b
algos = [SHA, SHA1, MD2, MD4, MD5, SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_384, SHA3_512, TupleHash128, TupleHash256, BLAKE2s, BLAKE2b]
import string
with open("BreakfastPasswords.txt", "r") as f:
    hashes = f.readlines()

flag = ""
for i in range(len(hashes)):
    algo, hash = hashes[i].split(" ")
    algo = algos[i]
    for char in string.printable:
        test_hash = algo.new()
        test_hash.update(char.encode())
        if test_hash.hexdigest() in hash:
            flag += char

print(flag)