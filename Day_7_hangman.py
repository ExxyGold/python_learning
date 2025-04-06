import random
from pi_art import hang_logo,stages,word_list
 
print (hang_logo)

chosen_word = random.choice(word_list)

display = []

word_len= len(chosen_word)

lives = 6

for _ in range(word_len):
    display += "_"

gameover = False

while not gameover:

    guess= input("Choose a letter\n").lower()
    

    for n in range(word_len):
        letter = chosen_word[n]
        if guess == letter:
            display[n] = letter
            
    letter_display = ""
    for n in display:
        letter_display += n
        letter_display += " "

    if guess not in chosen_word:
        lives-=1 
        print(f"{letter_display}\n you got it wrong, you have {lives} lives left")
    else:
        print(f"{letter_display}\n you got it Right, you have {lives} lives left")
    if lives == 0:
        gameover = True
        print("You Lose")

    if "_" not in display:
        gameover = True
        print("You Win")   
    print(stages[lives])