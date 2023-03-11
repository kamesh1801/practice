import random
n= random.randrange(1,100)
guess= int(input("enter the number:"))
while n!=guess:
    if guess<n:
        print("too low")
        guess= int(input("enter the number:"))
    elif guess>n:
        print("too high")
        guess= int(input("enter the number:"))
    else:
        break
print("you guessed right")