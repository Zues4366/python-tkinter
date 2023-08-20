import random

play = True
while play == True:
    user = input("What is your choice? 'r' for rock, 's' for scissors, 'p' for paper ")
    computer = random.choice(['r', 's', 'p'])
    if user != 'r' and user != 'p' and user != 's':
        print('Invalid Entry')
    if user == computer:
        print('It\'s a draw')
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        print('You Win!')
    if (computer == 'r' and user == 's') or (computer == 's' and user == 'p') or (computer == 'p' and user == 'r'):
        user = input('You Lose! Presss Enter to Continue')
    again = input('Want to play again? yes or no ')
    if again == 'no':
        play = False
