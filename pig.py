import random


# Create dice roll function
def dice_roll():
    number = random.randint(1,6)
    print(number)


# Need to know the number of players
try:
    number_of_players = int(input("How many players are there?(2-4) : " ))
except ValueError:
    print("Please enter a number")

if number_of_players < 2:
    print("Can't play by yourself!")
elif number_of_players > 4:
    print("Too many players!")

try:
    score = int(input("What score will you play to? : "))
except ValueError:
    print("Please enter a number.")

# Create players scores
player_score = [0 for i in range (number_of_players)]

print(player_score)

# Total for the game
target_score = score


# Create turns
while max(player_score) < target_score:
    
    print("Your score is:" , ) #need to work out player score
    turn = input("Would you like to roll?(y/n): ")
    if turn.lower() != "y":
        break
    else:
        turn_roll = dice_roll()
    
