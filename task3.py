print("-- Vigenère Cipher Decoder --")
ciphertext = input("Input the message to decode: ")
original = ciphertext

caps = [0] * len(ciphertext)
for i in range(len(ciphertext)):
    if ord(ciphertext[i]) >= 65 and ord(ciphertext[i]) <= 90:
        caps[i] = 1

# print(caps)

keylen = int(input("Input the length of the key: "))


# http://cs.wellesley.edu/~fturbak/codman/letterfreq.html
genfreq = {'a': 0.0820011, 'b': 0.0106581, 'c': 0.0344391, 'd': 0.0363709, 'e': 0.124167, 'f': 0.0235145, 'g': 0.0181188,
           'h': 0.0350386, 'i': 0.0768052, 'j': 0.0019984, 'k': 0.00393019, 'l': 0.0448308, 'm': 0.0281775, 'n': 0.0764055,
           'o': 0.0714095, 'p': 0.0203171, 'q': 0.0009325, 'r': 0.0668132, 's': 0.0706768, 't': 0.0969225, 'u': 0.028777,
           'v': 0.0124567, 'w': 0.0135225, 'x': 0.00219824, 'y': 0.0189182, 'z': 0.000599}


# genfreq={'a': 8.17, 'b':1.29 , 'c': 2.78, 'd': 4.25, 'e':12.70, 'f': 2.23, 'g': 2.02,
#          'h': 6.09, 'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75,
#          'o': 7.51, 'p': 1.93, 'q': 0.10, 'r': 5.99, 's':6.33, 't': 9.06, 'u': 2.76,
#          'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07}

#genfreq = sorted(genfreq.items(), key=lambda x:x[1], reverse = True)
#print (genfreq)
ciphertext = ciphertext.lower()

# splitting
sections = []
for i in range(keylen):
    sections.append([])
count = 0
for i in ciphertext:
    if ord(i) >= 65 and ord(i) <= 90:
        if count == keylen:
            count = 0
        sections[count].append(i)
        count = count + 1
    elif ord(i) >= 97 and ord(i) <= 122:
        if count == keylen:
            count = 0
        sections[count].append(i)
        count = count + 1

# print(sections)

caesars = []
for i in range(keylen):
    caesars.append([])
    for j in range(26):
        caesars[i].append([])

# caesar
# FIX SPACES AND PUNCUTATION AND OTHER CHARS
for i in range(keylen):
    for j in range(26):
        translated = ""
        for k in sections[i]:
            ck = ord(k) - j  # shift by j
            if ck < 97:
                ck = ck + 26
            translated = translated+chr(ck)
        # print(translated)
        caesars[i][j] = translated
# print("caesars")
# print(caesars)


# DICTIONARIES
dictionaries = []
for i in range(keylen):
    dictionaries.append([])
    for j in range(26):
        dictionaries[i].append({})


for i in range(keylen):
    for j in range(26):
        dictionaries[i][j] = dict((chr(key), 0) for key in range(97, 123))


for i in range(keylen):
    for j in range(26):
        for k in caesars[i][j]:
            dictionaries[i][j][k] = dictionaries[i][j][k] + 1
        #dictionaries[i][j] = sorted(dictionaries[i][j].items(), key=lambda x: x[1], reverse=True)

# print(dictionaries)

sums = []
for i in range(keylen):
    sums.append([])
    for j in range(26):
        sums[i].append([])


# chi
for i in range(keylen):
    for j in range(26):
        sum = 0
        for k in dictionaries[i][j]:
            # print(dictionaries[i][j][k]) freq
            # print(k) letter
            caesarlength = len(caesars[i][j])
            gf = genfreq[k]
            chi = dictionaries[i][j][k] - (caesarlength*gf)
            chi = chi ** 2
            chi = chi / (caesarlength*gf)
            sum = sum + chi
        # print(sum)
        sums[i][j] = sum

# print(sums)
ckey = ""
for i in range(keylen):
    low = sums[i].index(min(sums[i]))
    sums[i] = chr(low+97)
    ckey = ckey+sums[i]

# print(ckey)
# print(sums)

diff = len(ciphertext) - len(sums)

if diff > 0:
    for i in range(diff):
        sums.append(sums[i])

# print(sums)


index = 0
check = 0
decrypted = []
for i in range(len(ciphertext)):
    if ciphertext[i].islower():
        index = (ord(ciphertext[i])-96) - (ord(sums[i+check])-96)
        index = (index % 26) + 97
        decrypted.append(chr(index))
    elif ciphertext[i].isupper():
        index = (ord(ciphertext[i]) - 65) - (ord(sums[i+check]) - 96)
        index = (index % 26) + 66
        decrypted.append(chr(index))
    else:
        index = ord(ciphertext[i])
        check = check - 1
        decrypted.append(chr(index))

d = ""
for i in decrypted:
    d = d + i

ckey = ckey.upper()
print("Found Key: " + ckey)
final = ""
print("Decrypted message: ")
for i in range(len(d)):
    if caps[i] == 1:
        print(d[i].upper(), end="")
    else:
        print(d[i], end="")
