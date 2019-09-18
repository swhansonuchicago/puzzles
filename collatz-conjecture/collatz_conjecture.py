def steps(number):
    number = float(number)
    #print(number)
    if number<=0:
        return("Invalid input")
    while (number % 2)==0:  
        #print(number)
        number=number/2
    if number==1:
        print(number)
        return(number)
    number=(number*3+1)/2
    steps(number)
    