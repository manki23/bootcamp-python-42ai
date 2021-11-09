import random

def print_intro():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")

number = random.randint(1, 99)
keep_playing = True
attempts = 1
print_intro()
while keep_playing:
    print("What's your guess between 1 and 99?")
    guess = input(">> ")
    if guess == 'exit':
        print("Goodbye!")
        keep_playing = False
    elif not guess.isnumeric():
        print("That's not a number.")
    elif int(guess) > number:
        print("Too high!")
    elif int(guess) < number:
        print("Too low!")
    elif attempts == 1:
        if number == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        print("Congratulations! You got it on your first try!")
        keep_playing = False
    else:
        if number == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        print("Congratulations, you've got it!")
        print("You won in {0} attempts!".format(attempts))
        keep_playing = False
    attempts += 1
