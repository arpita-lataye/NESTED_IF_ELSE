

winning_number=17
num1=int(input("guess a number between 1 and 100:"))
num2=int(num1)
if num1 == winning_number:
    print("you win !!!")
else:
    if num1 < winning_number:
        print("too low")
    else:
        print("too high")