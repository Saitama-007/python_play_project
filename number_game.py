## NUMBER GAME : the user have to guess a number 
## if the guessed number is less than the number python prompts TOO low!
## if the guessed number is less than the number and the difference is 5 or less python prompts "almost there but increase "
## if the guessed number is greater than the number python prompts TOO high!
## if the guessed number is greater than the number and the difference is 5 python prompts "almost there but decrease "

## import the random module in order to input a random number without our concern
import random
## Taking a range of random numbers between 1 to 300

num = random.randrange(1,30)
## To take a user input to enter a number
guess_the_number = int(input("Enter any number: "))

while num != guess_the_number: # if the number is not equal to the input entered guess_the_number
    # if guess is smaller than n
    if guess_the_number < num:
        if (num - guess_the_number) > 5:  ## if our number(guess_the_number) is less than answer(num)
            print("Too low!")
        else:
            print("almost there but increase ")
        
        # to again ask for input
        guess_the_number = int(input("Enter number again: "))
    # if guess is greater than n
    elif guess_the_number > num:
        if (guess_the_number - num) > 5: ## if our number(guess_the_number) is greater than answer(num)
            print("Too high!")
        else:
            print("almost there but decrease ")
        # to again ask for the user input
        guess_the_number = int(input("Enter number again: "))
    # if guess gets equals to n terminate the while loop
    else:
        break
print("lets party!!")