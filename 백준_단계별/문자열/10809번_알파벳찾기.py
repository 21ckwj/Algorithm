word = input()
alphabet = [i for i in range(97,123)]

for x in alphabet:
    print(word.find(chr(x)))
