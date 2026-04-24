import random
#generate random number 
number = random.randint(1,100)
print("welcome to the number gussingg game")

guess = 0 

while guess != number :
    guess = int(input("guess a no between 1 to 100 : "))
    if guess < number :
        print("too low")
    elif guess >number :
        print("too high")
    else :
        print("congratulations you gussed the number !")
                