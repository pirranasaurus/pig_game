import random


# Create dice roll function
def dice_roll():
    number = random.randint(1,6)
    return(number)


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

# Total for the game
target_score = score

# Create turns
while max(player_score) < target_score:
    for player_index in range(number_of_players):
        print("Player number ", player_index + 1, "turn has started.")
        print("Your total score is:" ,player_score[player_index])
        turn_score = 0

        while True:        
            turn = input("Would you like to roll?(y/n): ")
            if turn.lower() != "y":
                break 

            turn_roll = dice_roll()
            if turn_roll == 1:
                print("You rolled a 1! Turn over")
                turn_score = 0
                break
            else:    
                turn_score += turn_roll
                print("You rolled a: ", turn_roll)

            print("Your currnt turn score is: ", turn_score)

        player_score[player_index] += turn_score
        print("Your total score is: ", player_score[player_index])

winning_score = max(player_score)
winning_player = player_score.index(winning_score)

print("Player ", winning_player + 1, "is the winner! With a score of: ", winning_score)