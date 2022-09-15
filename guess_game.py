import random
count = 0
while count < 11:
    print("Guess a number between 1 - 10")
    user_guess= int(input("===> "))
    comp_guess= random.randrange(1,10)
    print("Random number: " , comp_guess)
    if user_guess == comp_guess:
        print("You guessed right !")
        count= count+1
        print('number of trials:', count)
        break
    elif user_guess < 10  and user_guess != comp_guess :
        print("Hmm, its within range,try again!")
        count= count+1
else:
    print("You guessed wrong, out of range", count +'times')