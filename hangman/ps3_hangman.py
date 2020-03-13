# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    ret = ""
    for char in secretWord:
        if char in lettersGuessed:
            ret+=char
        else:
            ret+="_ "
    return ret



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    ret = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in lettersGuessed:
            ret+=char
    return ret

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    secretWord = chooseWord(wordlist).lower()
    lettersGuessed = []
    guesses_left = 8
    secretWordFound = False
    availableLetter = getAvailableLetters(lettersGuessed)
    guessed_word = getGuessedWord(secretWord,lettersGuessed)
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secretWord),"letters long.")
    while guesses_left!=0 and not secretWordFound:
        print("-----------")
        print("You have",guesses_left,"guesses left.")
        print("Available letters:",availableLetter)
        userinput = input("Please guess a letter: ").lower()
        if userinput not in availableLetter:
            print("Oops! You've already guessed that letter:",guessed_word)
        else:
            lettersGuessed.append(userinput)
            guessed_word = getGuessedWord(secretWord,lettersGuessed)
            availableLetter = getAvailableLetters(lettersGuessed)
            if userinput in secretWord:
                print("Good guess:",guessed_word)
                secretWordFound = isWordGuessed(secretWord,lettersGuessed)
            else:
                guesses_left-=1
                print("Oops!that letter is not in my word:",guessed_word)
    if secretWordFound:
        print("-----------")
        print("Congratulations you won!")
    else:
        print("-----------")
        print("Sorry,you ran out of guesses. The word was",secretWord,".")







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
if __name__ == '__main__':
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
