# CST 205
# Module 6: Lab 13
# Craig Calvert, Samuel Pearce


import os
import textwrap


def mad_libs():
    # dictionary of questions and position where returned answers need to be inserted
    questions = {
        'Enter a famous Steve\'s last name: ': 16,
        'Enter an adjective: ': 17,
        'Enter the name of a movie: ': 29,
        'Enter another adjective: ': 40,
        'Enter one more adjective: ': 61,
        'Enter a movie genre: ': 65,
        'Enter a type of fish: ': 76,
        'Enter another type of fish: ': 104,
        'Enter the first name of an actor: ': 111,
        'Enter the last name of same actor: ': 112,
        'Enter the actor\'s last name again: ': 124,
        'Enter an action: ': 127,
        'Enter a nickname for the actor: ': 134,
        'Enter a movie rating: ': 172,
        'Enter the next to last adjective for this Mad Lib: ': 211,
        'Enter one last adjective: ': 215,
        'Enter a television channel: ': 216
    }

    rootPath = os.path.dirname(__file__)
    txt_file = open(os.path.join(rootPath, "movie_review.txt"), "r")
    # read the input file and split into individual words
    text = txt_file.read().split()
    print("\nWelcome to Northwestern Technology's Mad Libs!")
    print("-----------------------------------------------")
    # user is prompted for input to a question, answer then replaces the
    # word at the position value associated with the question in the dictionary
    for key, value in questions.items():
        while True:
            user_input = input(key)
            if user_input == '':
                print("Sorry, could you please try that again.")
                continue
            else:
                break
        text[value] = user_input
    # after all questions have been answered join the words back together
    my_new_string = " ".join(text)
    print("\n************************************************************")
    print(textwrap.fill(my_new_string, 80))
    # prompt user if they would like to play again
    while True:
        play_again = input('\n\nWould you like to try again? (Y/N): ')
        reply = play_again.lower()
        if reply == 'y':
            mad_libs()
        elif reply == 'n':
            print("Thank you for playing!")
            break
        else:
            print('Sorry, could you please try that again.')
            continue


mad_libs()
