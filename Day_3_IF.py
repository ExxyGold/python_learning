print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
first_choice = input('You are at a crossroad, Where do you want to go? Type "Left" or "Right"\n').lower()

if first_choice == "left":
    second_choice= input('You come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "Swim" to swim across\n').lower()
    if second_choice == "wait":
        third_choice = input("The boat came and it took you to an island unharmed. There is a temple up ahead, having three doors; Blue, Red and Yellow, Which door would you like to pass through\n").lower()
        if third_choice=="yellow":
            print("You found the lost treasure, You win.")
        elif third_choice=="blue":
            print("You entered an ice cold room and froze to death, Game over.")
        elif  third_choice=="red":
            print("You stepped into a furnance and got burnt to death, Game Over.")
        else:
            print("Game over")
    elif second_choice == "swim":
        print("Your were swallowed by a Crododile, Game over")
    else:
        print("Game over")
elif first_choice=="right":
    print("You walked into an evil forest, Game over")
else:
    print("Game Over")