def steps(number):
    number = float(input("Enter a number here:"))
    if number<=0:
        print("Invalid input")
    if number==1:
        print("1")
    while (number % 2)==0:   
        number=number/2
        print(number)
    number=(number*3+1)/2
    return number
