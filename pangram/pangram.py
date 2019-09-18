from string import *
def is_pangram(sentence):
    letters = []
    sentence = str.lower(sentence)
    letterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u"]
    letterlist.append("v")
    letterlist.append("w")
    letterlist.append("x")
    letterlist.append("y")
    letterlist.append("z")
    for letter in sentence:
        if (letter not in letters) and (letter in letterlist):
            letters.append(letter)
    print(letters)
    if len(letters) == 26:
        print("This is a pangram!")
    else:
        print("This is not a pangram :(")

