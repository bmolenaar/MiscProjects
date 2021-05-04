from random import randrange

#Get the player's name from input and print greeting message
plyrName = str(input("Please enter your name: "))
print("Hi, " + plyrName + "!")

numToGuess = randrange(1, 101)
numOfGuesses = randrange(1, 7)


#Function to verify that the player's guess is within the bounds and display the appropriate message and call
#the read/write functions
def checkGuess():
    amtOfGuesses = 0
    win = ""
    while amtOfGuesses <= numOfGuesses:
        guess = int(input("Guess a whole number between 1 and 100!"))
        if guess < 100 and guess > 0:
            if guess < numToGuess:
                print("Too low, bro. You have " + str((numOfGuesses - amtOfGuesses)) + " guesses left!")
                win = "loss"
            elif guess > numToGuess:
                print("Too high, guy. You have " + str((numOfGuesses - amtOfGuesses)) + " guesses left!")
                win = "loss"
            else:
                print("You guessed it!")
                amtOfGuesses += 1
                win = "win"
                break
        else:
            print("Your number is out of range")

        amtOfGuesses += 1
    writeScores(plyrName, win, amtOfGuesses)
    print(readScores())


#Function to write the player's name, result and amount of guesses to a text file
def writeScores(name, result, guesses):
    txt = open("Statistics.txt", "a")
    txt.write(str(name) + " | " + str(result) + " | " + str(guesses) + "\n")
    txt.close()


#Function to read the results written to the text file
def readScores():
    txt = open("Statistics.txt", "r")
    scores = txt.read()
    return scores

checkGuess()
input("Press enter to close")