import os
import random

rootPath = os.path.dirname(__file__)
news = open(os.path.join(rootPath,"news.txt"),"r")

text = news.read()
words = text.split()

wordSwapIndexes = []

#get some random words
while (len(wordSwapIndexes) < 7):
  r = random.randint(0,len(words))
  if r not in wordSwapIndexes:
    wordSwapIndexes.append(r)

for i in range(len(wordSwapIndexes)):
    #input = requestString("\nEnter a word: ")
    input = raw_input("\nEnter a word: ")
    if(input==None):
        continue
    words[wordSwapIndexes[i]] = input

story = ""
for word in words:
    story = story + " " + word

print(story)
