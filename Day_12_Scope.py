# enemy_level = 4
# enemies =["Skeleton", "Zombies", "Monsters"]

# if enemy_level > 3:
#     new_enemy = enemies[2]

# print (new_enemy)

import random

print("Welcome to Number Guessing Game")
print("Im thinking of a number between 1 and 100.")



actual_number = random.randint(1, 100)

attempts = [5, 10]
def set_difficulty():
    difficulty = input("Choose a Difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        user_gets = attempts[1]
    elif difficulty == "hard":
        user_gets = attempts[0]
    return user_gets


level = set_difficulty()

game_over = False


print(f"You have {level} attempts remaining to get the number")

while not game_over:
    guess = int(input("Make a guess: "))

    if guess > actual_number:
        level -= 1
        print(f" Too High\n Guess again.\n You have {level} attemts remaining to get the number")
    elif guess < actual_number:
        level -= 1
        print(f" Too Low\n Guess again.\n You have {level} attemts remaining to get the number")
    else:
        print(f"You Got it, the answer is {actual_number}")
        game_over = True

    if level == 0:
        print("You have run out of guesses, You lose.")
        game_over = True