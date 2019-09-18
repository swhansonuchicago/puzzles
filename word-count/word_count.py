from string import *
def count_words(sentence):
    sentence = str.lower(sentence)
    current = ""
    dlist = {}
    wlist = []
    notletters = [" ", ",", ".", ":", ";"]
    lastletter = " "
    adder = 0
    for letter in sentence:
        if letter in notletters and lastletter not in notletters:
            adder = 0
            if current in wlist:
                dlist[current] += 1
            else:
                wlist.append(current)
                dlist[current] = 1
            current = ""
        elif letter not in notletters:
            adder += 1
            current = current + letter
        lastletter = letter
    if adder != 0:
        if current in wlist:
            dlist[current] += 1
        else:
            wlist.append(current)
            dlist[current] = 1
    for word in wlist:
        print(word + ": " + str(dlist[word]))
