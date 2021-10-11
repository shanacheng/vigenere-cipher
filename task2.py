print("-- Vigenère Cipher Decoder --")
e = input("Input the message to decode: ")
ckey = input("Input the given key: ")
ckey = ckey.lower()
ckey = list(ckey)
diff = len(e) - len(ckey)

if diff > 0:
    for i in range(diff):
        ckey.append(ckey[i])

index = 0
check = 0
decrypted = []
for i in range(len(e)):
    if e[i].islower():
        index = (ord(e[i])-96) - (ord(ckey[i+check])-96)
        index = (index % 26) + 97
        # print(index)
        decrypted.append(chr(index))
    elif e[i].isupper():
        index = (ord(e[i]) - 65) - (ord(ckey[i+check]) - 96)
        index = (index % 26) + 66
        # print(index)
        decrypted.append(chr(index))
    else:
        index = ord(e[i])
        check = check - 1
        decrypted.append(chr(index))

d = ""
for i in decrypted:
    d = d + i
print("Decrypted message: " + d)
