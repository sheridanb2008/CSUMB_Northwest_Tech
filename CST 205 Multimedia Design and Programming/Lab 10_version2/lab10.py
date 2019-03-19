#CST205 
#Lab 10
#Craig Calvert and Kevin Bentley

#warm Up

def warmUpB():
  prompt = "Enter stop to stop"
  str = requestString(prompt)
  while(str!='stop'):
    str = requestString(prompt)
  
  
def getInstructions():
  return """
  Hangman is a word guessing game. 
  Each time you choose a letter that appears in the word
  you will see the word with all of the letters you correctly
  guessed filled in. If you use up the six incorrect guesses,
  you will be hanged and lose the game!
  """
  
  
#Print the currently guessed word
#If the word has been completely guessed, return True
def printWord(secretWord,correctGuesses):
  print("Word so far:")
  allGuessed = True
  for i in range(len(secretWord)):
    if(secretWord[i] in correctGuesses):
      print(secretWord[i] + " "),
    else:
      allGuessed = False
      print("_ "),
  print "" # newline
  return allGuessed
    
def printIncorrectGuesses(wrong, maxIncorrectGuesses):
  print("Incorrect guesses:")
  for ltr in wrong:
    print(ltr),
  print "" # newline
  print("You have used " + str(len(wrong)) + " of " + str(maxIncorrectGuesses) + " guesses")
  
def getLetter():
  prompt = "Select a single letter between a-z"
  ltr = requestString(prompt)
  #If more or less than one character is entered or
  #the character entered is not a letter keep prompting
  while(ltr == None or len(ltr)!=1 or (not ltr.isalpha())):
    print("Letters only please!")
    ltr = requestString(prompt)
  return ltr.lower()

def hangman():
  print(getInstructions())
  maxWrongGuesses = 6
  secretWord = "hangman"
  secretLength = len(secretWord)
  guessedWord = ""
  correctGuesses = []
  wrongGuesses = []
  ltr = ''
  printWord(secretWord,correctGuesses)
  while(len(wrongGuesses) < maxWrongGuesses):
    ltr = getLetter()
    if (ltr in secretWord):
      correctGuesses.append(ltr)
      print("Correct!")
    else:
      print("Incorrect!")
      if(ltr not in wrongGuesses):
        wrongGuesses.append(ltr)
    if(printWord(secretWord,correctGuesses)):
      print "Congratulations you win!"
      return
    printIncorrectGuesses(wrongGuesses, maxWrongGuesses)
  print("Sorry, you lose.  Better luck next time!")