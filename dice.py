## Sic bo (Chinese Dice rolling game) ##
## Roll three dice and player bet on the odds that it will land on the choice ##
import random
num1 = 0 
num2 = 0
num3 = 0
start = " "
user = " "
choice = " "
options = ["triple", "double", "big", "small"]
# Game Values #
def game(start):
    ## 1st dice roll ##
    num1 = random.randrange(1,6,1)
    ## 2nd dice roll ##
    num2 = random.randrange(1,6,1)
    ## 3rd dice roll ##
    num3 = random.randrange(1,6,1)
    print (num1,num2,num3)
    ## Dice results ##
    if num1 == num2 == num3:
        return "Triple"
    elif ((num1 == num2) and (num1 != num3)) or ((num2 == num3) and (num2 != num1)) or ((num1 == num3) and (num1 != num2)):
        return "Double"
    elif (num1 + num2 + num3) >= 11:
        return "Big"
    elif (num1 + num2 + num3) <= 10:
        return "Small"
## Code that will use Player input ##
def player_choice(choice):
    if choice in options:
        return game(start)
## Player Input ##
start = input("Do you want to play? Enter yes or no: ")
if start != 'yes' or start != 'no' or start == 'no':
    play = False
if start == 'yes':
    print("Make your guess with the four options:")
    print("Triple")
    print("Double")
    print("Big")
    print("Small")
    user = input("What is your guess? ")
    if user in options:
        choice = user
        print(player_choice(choice))
    else:
        print('Not a Choice..... Ending')
again = input('Would you like to play again? yes or no: ')
if again == 'no':
    play = False
