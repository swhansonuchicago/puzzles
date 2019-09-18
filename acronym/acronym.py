def abbreviate(words):
    word_list = words.split()
    first =  [x[0] for x in word_list]
    acronym = ''.join(str(y) for y in first)
    return acronym


