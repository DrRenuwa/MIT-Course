high = 100
low = 0
guess = (high + low)//2

print("Please think of a number between 0 and 100!")
print("Is your secret number " + str(guess) + '?')

while True:
    entered = input("Enter 'h' to indicate the guess is too high. "
                "Enter 'l' to indicate the guess is too low. "
                "Enter 'c' to indicate if I guessed correctly.: ")
    if entered == 'h' :
        high = guess
        guess = (high + low)//2
        print("Is your secret number: " + str(guess) + '?')
        entered = ""
    elif entered == 'l':
        low = guess
        guess = (high + low)//2
        print("Is your secret number: " + str(guess) + '?')
        entered = ""
    elif entered == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    else: 
        print("Sorry, I did not understand your input")
        print("Is your secret number: " + str(guess) + '?')