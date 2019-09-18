atbash = {'a':'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u', 'g':'t', 'h':'s', 'i':'r','j':'q','k':'p',
          'l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f',
          'v':'e','w':'d','x':'c','y':'b','z':'a'}


def encode(plain_text):
    
    cipher = ''
    plain_text = plain_text.lower()
    for i in plain_text:
        
        if i != ' ':
            
            cipher += atbash[i]
    
        elif i==' ':
            cipher += ' '
    
    return cipher

def decode(ciphered_text):
    
    plain = ''
    ciphered_text = ciphered_text.lower()
    for i in ciphered_text:
        
        if i != ' ':
            
            plain += atbash[i]
    
        elif i==' ':
            plain += ' '
    
    return plain