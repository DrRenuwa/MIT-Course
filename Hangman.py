# Hangman game
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "Python\MIT\hangman.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    j = 0

    for i in range(len(secretWord)):
        while j != (len(lettersGuessed)):
            if secretWord[i] == lettersGuessed[j]:
                count += 1
                j = 0
                break
            else:
                j += 1
    
            
    if count == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ""
    j = 0
    if len(lettersGuessed) == 0:
        word += len(secretWord) * "_ "
    else:
        for i in range(len(secretWord)):
            while True:
                if secretWord[i] == lettersGuessed[j]:
                    word += lettersGuessed[j] + " "
                    j = 0
                    break
                else:
                    j += 1
                    if j == (len(lettersGuessed)):    
                        j = 0
                        word += "_ "
                        break
    return word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = ""
    alphabet = string.ascii_lowercase
    j = 0
    count = 0
    
    if len(lettersGuessed) == 0:
        available = alphabet
    else:
        for i in range(len(alphabet)):
            for j in range(len(lettersGuessed)):
                if lettersGuessed[j] != alphabet[i]:
                    count += 1
                    if count == len(lettersGuessed):
                        available += alphabet[i]
                        count = 0
                        break
                else:
                    count = 0
                    break
               
    return available
    

def hangman(secretWord):

    lettersGuessed = []
    progress = getGuessedWord(secretWord, lettersGuessed)
    number_of_guesses = 8
    won_string = "Congratulations, you won! The word was " + secretWord + " ."
    lose_string = ("Sorry, you ran out of guesses. The word was " + secretWord + " .")

    print("--------------------------------------------")
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")

    while isWordGuessed(secretWord, lettersGuessed) == False:
        if number_of_guesses == 0:
            print(lose_string)
            break
        else:
            print("You have " + str(number_of_guesses) + " guesses left " 
                  + getGuessedWord(secretWord, lettersGuessed))
            print("Available letters: " + getAvailableLetters(lettersGuessed))
            guess = input("Please guess a letter: ")
            
            while guess.isalpha() == False or len(guess) > 1 or guess == " ":
                if guess.isalpha() == False:
                    print("--------------------------------------------")
                    print("You have " + str(number_of_guesses) + " guesses left " 
                          + getGuessedWord(secretWord, lettersGuessed))
                    print("Available letters: " + getAvailableLetters(lettersGuessed))
                    guess = input("Please enter a LETTER: ")
                    getGuessedWord(secretWord, lettersGuessed) 
                elif len(guess) > 1 or guess == " ":
                    print("--------------------------------------------")
                    print("You have " + str(number_of_guesses) + " guesses left " 
                          + getGuessedWord(secretWord, lettersGuessed))
                    print("Available letters: " + getAvailableLetters(lettersGuessed))
                    guess = input("Please enter ONE letter: ")
                    getGuessedWord(secretWord, lettersGuessed)
                    
            for j in range(len(lettersGuessed)):
                while True:
                    if lettersGuessed[j] == guess:
                        print("--------------------------------------------")
                        print("You've already guessed that letter: ")
                        print("You have " + str(number_of_guesses) + " guesses left " 
                              + getGuessedWord(secretWord, lettersGuessed))
                        print("Available letters: " + getAvailableLetters(lettersGuessed))
                        guess = input("Please guess a letter: ")
                        lettersGuessed += guess.lower()
                        getGuessedWord(secretWord, lettersGuessed)                        
                    else:
                        break      
                        
            lettersGuessed += guess.lower()
            getGuessedWord(secretWord, lettersGuessed)
            
            if progress == getGuessedWord(secretWord, lettersGuessed):
                print("--------------------------------------------")
                print("Wrong guess")
                progress = getGuessedWord(secretWord, lettersGuessed)
                number_of_guesses -= 1
            else:
                print("--------------------------------------------")
                print("Correct guess!")
                progress = getGuessedWord(secretWord, lettersGuessed)
        
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print(won_string)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)