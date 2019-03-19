# Brian Sheridan And Samuel Pearce
# CST 205 
# Lab 10

# WARM UP
def repeat():
  name = requestString("What is your name?")
  print "Your name is %s" %name
# WORKING WITH WHILE LOOP  
def parrot():
  text = ""
  while (text != 'stop'):
    text = requestString("Enter a word. Type stop to quit")
    print "You typed: %s" % text
  print "Thanks for playing"
  
# Hangman Game
def hangman():
# Initialize variables
  word, dashWord, chr, incChr, guesses,status = wordSelect(),"","","","",""
  k = 0
  win,incorrect = False,True
# Create the underscores and reconfigure word
  dashWord = underScore(dashWord,word)
    
# Print game instructions  
  print("This is the game of hangman\n"
        "you have 6 guesses to correctly solve\n"
        "the word\n%s")%(dashWord)
# Cycle through the guesses        
  while (k < 6):
# Get user input  
    chr,  = letter(k,guesses)
# Fill in underscores and check to see if correct
# or user has won.
    dashWord, win = fill(dashWord,word,chr)  
# Save all guesses    
    guesses += chr
# Break while loop if won 
    if win:
      break
# set flags       
    incorrect = True  
    status = "Correct!"
# Set letter in incorrect letter if not in word
    for i in range(len(word)):
      if chr.upper() == word[i] or chr.lower() == word[i] :
        incorrect = False
    if incorrect == True:    
      incChr += chr
      incorrect = True
      status = "Incorrect!"
      k +=1  
# Print current status of game   
    if len(incChr)  == 0:
      print("\n%s\nWord so far:\n%s\nYou have used 0 of you 6 guesses.") %(status,dashWord)
    else:
      print("\n%s\nWord so far:\n%s\nIncorrect guesses:\n%s") %(status,dashWord,incChr)
# Print message based on completion      
  if win:
    print "Congrats! You solved the word:  %s." %word
  else:
    print "You Lost! Please try again"
   
    
# -----------------------------------------------------------
# Supporting Functions
# -----------------------------------------------------------
# Enter word to be used for hangman
def wordSelect():
  return "Kaleidoscope"

# Request letter from user
# Letters can be upper or lower case
# produce error when a char is not a letter
# or the letter has already been selected    
def letter(count,guesses):
  flag = False
  while(count < 6):
    flag = False
    letter = requestString("Enter a letter:")
    for i in range(len(guesses)):
      if letter.upper() == guesses[i] or letter.lower() == guesses[i]:
        flag = True
    if flag == True:
      print "You already selected that letter. Try again."
    elif len(letter) == 1 and letter.isalpha():
      return letter
    else:
      print " Incorrect entry please try again."

# Create underscores for the word followed by a space            
def underScore(target, word):
  for i in range(len(word)):
    target += "_ "
  return target
  
# Check to see if letter matches the word and fill in that space
def fill(source,word,chr):
# Local Variables
  temp = ""
  flag = True
# remove spaces to compare
  for i in range(len(source)):
    if source[i] != " ":
      temp += source[i]
  source = temp
  temp = ""
# Enter letter where a underscore is if correct  
  for i in range(len(word)):
    if (chr.upper() == word[i] or chr.lower() == word[i]):
      temp += chr
    else:
      temp += source[i]
  flag = True
# Check to see if the user won  
  for i in range(len(word)):
    if temp[i].lower() != word[i].lower() or temp[i].upper() != word[i].upper():
      flag = False
  source = temp
  temp = ""
# Add spaces in for display  
  for i in range(len(source)):
    temp += source[i] + " "
  return [temp, flag]

    
  
      