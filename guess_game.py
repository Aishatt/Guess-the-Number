import random

print("Guess a number between 1 - 10")
user_guess= int(input("===> "))
comp_guess= random.randrange(1,10,2)
print("Random number: " , comp_guess)
if user_guess == comp_guess:
    print("You guessed right !")
elif user_guess < 10  and user_guess != comp_guess :
    print("Hmm, its within range,try again!")
else:
    print("You guessed wrong, out of range")