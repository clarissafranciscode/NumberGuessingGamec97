import random 
number= random.randint(1,9)
chances = 0
while chances < 5: 
    guess = int(input("enter your guess"))
    if guess == number: 
        print("Congrats! You won!")
        break 
    elif guess < number: 
        print("your guess was too LOW, guess a higher number")
    else: 
        print("your guess was too HIGH, guess a lower number")
    chances +=1 
if not chances < 5:
    print("you lost!")        
print("Number guessing game")
