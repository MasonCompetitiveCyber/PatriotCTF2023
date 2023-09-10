with open("corrupted.jpg", "rb") as f:
    data = f.read()

corrupted = [data[i:i+1] for i in range(0, len(data))]

i=2
fixed=corrupted[0:2]
[fixed.append(corrupted[i]) for i in range(11,len(corrupted),10)]

to_write = b''.join(fixed)

with open("uncorrupted.zip", "wb") as binary_file:
    binary_file.write(to_write)

print("DONE")
