low=1
high=100
print("guess a number between 1 to 100")
while True:
    guess=(low+high)//2
    print("my guess is", guess)
    answer=input("enter yes/greater/lesser:")
    if answer == "yes":
        print("correct guess")
        break
    elif answer == "greater":
        low=guess+1
    elif answer == "lesser":
        high=guess-1