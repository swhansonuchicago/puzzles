def is_valid(isbn):
    countsofar = 0
    total = 0
    for letter in isbn:
        if countsofar > 9:
            print("Characters after 10th digit")
            return
        try:
            letterint = int(letter)
            total += (10-countsofar)*letterint
            countsofar += 1
        except ValueError:
            if letter != "X" and letter != "-":
                print("Invalid Character: " + letter)
                return
            if letter == "X" and countsofar < 9:
                print("X before 10th digit")
                return
            elif letter == "X" and countsofar == 9:
                total += 10
                countsofar += 1
    total = total%11
    return(total)
