from string import *
def rotate(text, key):
    cyphertext = ""
    for letter in text:
        letterint = ord(letter) - 96 
        if letterint > 0 and letterint < 27:
            if letterint + key != 26:
                cyphertext = cyphertext + chr(((letterint + key)%26)+96)
            else:
                cyphertext = cyphertext + chr(((letterint + key))+96)
        elif letterint > -32 and letterint < -5:
            letterint = letterint + 33
            if letterint + key != 26:
                cyphertext = cyphertext + chr(((letterint + key)%26)+63)
            else:
                cyphertext = cyphertext + chr(((letterint + key))+63)
        else:
            cyphertext = cyphertext + letter
    return(cyphertext)
