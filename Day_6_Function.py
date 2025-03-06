from pi_art import stages, word_list,logo
import random

print (logo)
chosen_word = list(random.choice(word_list))
print(chosen_word)
lives = 6
display= []
for letter in chosen_word:
    display+= "_"
game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()
    letter=[]
    if guess in display:
      print("You have already guessed that letter")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed the letter {guess}, thats not in the word, you lose a life")
        if lives==0:
            game_over= True
            print("You Lose")
        
    if "_" not in display:
        game_over= True
        print("You Win")
    print(stages[lives])