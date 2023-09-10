from Crypto.Hash import SHA, SHA1, MD2, MD4, MD5, SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_384, SHA3_512, TupleHash128, TupleHash256, BLAKE2s, BLAKE2b
flag = b"PCTF{H@5H_8R0WNS}"
algos = [SHA, SHA1, MD2, MD4, MD5, SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_384, SHA3_512, TupleHash128, TupleHash256, BLAKE2s, BLAKE2b]
for flag_byte, algo in zip(flag, algos):
    flag_byte = flag_byte.to_bytes(1, "big")
    hash = algo.new()
    hash.update(flag_byte)
    print(hash.hexdigest())
    print(algo.__name__)