from pi_art import treasure_art

print(treasure_art)
print("Welcome to Treasure Island.\n Your Mission is to find the treasure.")

first_choice = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'.\n")

if first_choice == "left":
    second = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if second == "wait":
        third = input("You arrived ath the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if third == "yellow":
            print("You win, You found the")
        elif third == "blue":
            print("Game Over, you entered a room and freezed to death")
        elif third == "red":
            print("Game, over, you entered a fiery furnance")
    else:
        print("Game Over, you were swallowed by Crocs")


else:
    print("Game Over, you walked into the desert")
