

winning_number = 27
user=int(input("guess a number between 1 and 100:"))
user=int(user)
if user==winning_number:
    print("you win !!!")
else:
    if user<winning_number:
        print("too low")
    if user>winning_number:
        print("too high")