#!/usr/bin/env python3
round = 0
while(True):
    round = round +1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input()
    answer = str(answer.upper())
    if (answer == 'BRIAN'):
        print('Correct')
        break
    elif (answer == 'SHRUBBERY'):
        print('You gave the super secret answer!')
        break
    elif(round==3):
        print('Sorry, the answer was Brian.')
        break
    else:
        print('Sorry! Try again!')