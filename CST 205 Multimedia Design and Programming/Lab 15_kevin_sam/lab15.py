#CST205
#Lab 17
#Kevin Bentley, Samuel Pearce
import os
import datetime
import calendar
import random

def printDie(num):
    if(num < 1 or num > 6):
        print('Invalid die!')
    if(num==1):
        print('''
.-------.
|       |
|   O   |
|       |
'-------' \n''')
    elif(num==2):
        print('''
.-------.
|   O   |
|       |
|   O   |
'-------' \n''')
    elif(num==3):
        print('''
.-------.
| O     |
|   O   |
|     O |
'-------' \n''')
    elif(num==4):
        print('''
.-------.
| O   O |
|       |
| O   O |
'-------' \n''')
    elif(num==5):
        print('''
.-------.
| O   O |
|   O   |
| O   O |
'-------' \n''')
    elif(num==6):
        print('''
.-------.
| O   O |
| O   O |
| O   O |
'-------' \n''')
    
def playerRoll():
    die1 = random.randint(1,6)
    print("Player Rolled " + str(die1))
    printDie(die1)
    die2 = random.randint(1,6)
    print("Player Rolled " + str(die2))
    printDie(die2)
    return die1 + die2

def playCraps():
    print('''Welcome to Craps!\n
                    ______
        .-------.  /\     \ 
       /   o   /| /o \  o  \ 
      /_______/o|/   o\_____\ 
      | o     | |\o   /o    / 
      |   o   |o/ \ o/  o  / 
      |     o |/   \/____o/ 
      '-------' \n
'''      )
    first = True
    point = 0
    while(True):
        raw_input("Press enter to roll...")
        value = playerRoll()
        print("You rolled " + str(value) + ".")
        if(first):
            if(value in (7,11)):
                print("You win!")
                return
            if(value in (2,3,12)):
                print("You Lose!")
                return
            if(value in (4,5,6,8,9)):
                point = value
                print("Keep rolling until you get " + str(point) + " but watch out for 7!")
        else:
            if(value == point):
                print("You win!")
                return
            if(value == 7):
                print("You lose!")
                return
        first = False

def problem2():
    print("Kevin's Birth Month\n")
    cndr = calendar.TextCalendar(calendar.SUNDAY)
    print(cndr.formatmonth(1973,2))
    today = datetime.date.today()
    nextBday = datetime.date(2019,2,2)
    days = (nextBday - today).days
    print("Kevin's next birthday is in " + str(days) + " days.\n")

    doi = datetime.date(1776,07,04)
    # We're doing this the hard way because strftime doesn't support years before 1900
    print("The declaration of independence was signed on a " + calendar.day_name[doi.weekday()] + 
          " " + calendar.month_name[doi.month] + " " + str(doi.day) + ", " + str(doi.year))

problem2()
playCraps()