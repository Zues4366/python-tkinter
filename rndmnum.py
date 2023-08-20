import random

play = True
while play == True:
    min = 1
    max = 6
    roll = input('Would you like to start the roll? yes or no ')
    if roll != 'yes' and roll != 'no':
        print('Invalid input.')
        print(roll)
    if roll == 'no':
        play = False
    while roll == 'yes':
        print('Rolling....')
        print(random.randint(min,max))
        roll = input('Roll Again? ')
        if roll != 'yes' and roll != 'no':
            print('Invalid input.')
            print(roll)
        if roll == 'no':
            play = False
