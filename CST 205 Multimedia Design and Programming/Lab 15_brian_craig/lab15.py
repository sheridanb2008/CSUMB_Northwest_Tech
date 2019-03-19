# CST 205
# Module 6: Lab 15
# Craig Calvert, Brian Sheridan

import calendar
import datetime
from datetime import timedelta
import random


# Returns a random value for one die.
def roll_die():
    return random.randint(1, 6)


def play_craps():
    # Variables
    die_one = roll_die()
    die_two = roll_die()
    dice_roll = die_one + die_two
    roll_number = 1

    print('\nEVERYONE PLACE YOUR BETS!\nIt\'s your turn ... roll those bones!')
    print('\n*** Roll #' + str(roll_number) + ' ***')
    # On first roll if player rolls a 7 or 11 they win.
    if dice_roll == 7 or dice_roll == 11:
        print('You rolled a ' + str(die_one) + ' and a ' + str(die_two) +
              ' for a total of ' + str(dice_roll) + '. You win!')
    # On first roll if player rolls a 2, 3, or 12 they lose
    elif dice_roll == 2 or dice_roll == 3 or dice_roll == 12:
        print('You rolled a ' + str(die_one) + ' and a ' + str(die_two) +
              ' for a total of ' + str(dice_roll) + '. You lose!')
    # If the player rolls any other number that number becomes the point.
    # Player continues to roll dice until they roll point (win) or a 7 (lose).
    else:
        # Assign first dice role to point variable.
        point = dice_roll
        print('You rolled a ' + str(die_one) + ' and a ' + str(die_two) + ' for a total of ' + str(dice_roll) + '\n')
        while roll_number >= 1:
            die_one = roll_die()
            die_two = roll_die()
            dice_roll = die_one + die_two
            roll_number += 1
            print('*** Roll #' + str(roll_number) + ' ***')
            if dice_roll == point:
                print('You rolled a ' + str(die_one) + ' and a ' + str(die_two) + ' for a total of ' + str(dice_roll) +
                      '. You win!')
                break
            elif dice_roll == 7:
                print('You rolled a ' + str(die_one) + ' and a ' + str(die_two) + ' for a total of ' + str(dice_roll) +
                      '. You lose!')
                break
            else:
                print('You rolled a ' + str(die_one) + ' and a ' + str(die_two) + ' for a total of ' + str(dice_roll) +
                      '\n')

    # Prompt the player and ask them if they would like to play again.
    play_again = input('\nWould you like to try your luck again? (Y/N): ')
    reply = play_again.lower()
    if reply == 'y':
        play_craps()
    elif reply == 'n':
        print('\n\"If you must play, decide upon three things at the start: \n the rules of the game, the stake, and '
              'the quitting time.” \n  – Chinese Proverb')
    else:
        print('Sorry, could you please try that again.')


def calendar_fun():
    # Prompt user to input name and date of birth.
    name = input('\nPlease type in your first name: ')
    dob = input('Please type in your date of birth (MMDDYYYY): ')
    month = int(dob[:2])
    day = int(dob[2:4])
    year = int(dob[4:])
    # Display the calendar month for when the user was born.
    calendar.setfirstweekday(calendar.SUNDAY)
    your_calendar = calendar.month(year, month)
    print('\n' + name + ', this is what the month looked like when you were born.\n\n' + your_calendar)
    # Find how many days it will be until the user's next birthday
    today = datetime.date.today()
    birthday = datetime.date(today.year, month, day)
    if birthday > today:
        print(birthday - today)
    else:
        birthday = birthday + timedelta(days = 365)
        print('You have to wait ' + str(abs(birthday - today).days) + ' days until your next birthday.')
    # Displays the day the the Declaration of Independence was ratified.
    independence_day = datetime.date(1776,7,4)
    print('\nThe Declaration of Independence was ratified on ' + calendar.day_name[independence_day.weekday()] +
          ', ' + calendar.month_name[independence_day.month] + ' ' + str(independence_day.day) + ', ' +
          str(independence_day.year) + '.')

play_craps()
#calendar_fun()