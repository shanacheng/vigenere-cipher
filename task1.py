print("-- Vigenère Cipher Encoder --")
plaintxt = input("Input the message you want to encode: ")
ckey = input("Input the key you want to use to encode your message: ")
ckey = ckey.lower()
ckey = list(ckey)
diff = len(plaintxt) - len(ckey)

if diff > 0:
    for i in range(diff):
        ckey.append(ckey[i])

# print(ckey)
encrypted = []
index = 0
check = 0

for i in range(len(plaintxt)):
    if plaintxt[i].islower():
        index = (ord(plaintxt[i]) - 96) + (ord(ckey[i+check]) - 96)
        # print(index)
        index = (index % 26) + 95
        if (index < 97):
            index = index + 26
        encrypted.append(chr(index))
    elif plaintxt[i].isupper():  # uppercase
        index = (ord(plaintxt[i]) - 65) + (ord(ckey[i+check]) - 96)
        # print(index)
        encrypted.append(chr(index + 64))
    else:
        index = ord(plaintxt[i])
        check = check - 1
        encrypted.append(chr(index))

# print(encrypted)
e = ""
for i in encrypted:
    e = e + i
print("Encrypted message: " + e)
