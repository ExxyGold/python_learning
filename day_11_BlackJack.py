import random
from pi_art import clear, blackjack_logo


# play = input("Would you like to play BlackJack? Type 'y' if yes and 'n' if no: ")

def deal_card():
    """Returns a random card from the deck of cards"""
    cards= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deal = random.choice(cards)
    return deal

def calculate_score(deck):
    score = sum(deck)
    if score == 21 and len(deck) == 2:
        return 0
    if score > 21 and 11 in deck:
        deck.append(1)
        deck.remove(11)
    score = sum(deck)
    return score

def compare(deckC, deckU):
    if deckC == deckU:
        return "It is a draw"
    elif deckC == 0:
        return "You Lose, Your opponent has a BlackJack"
    elif deckU == 0:
        return "You Win, You got a BlackJack"
    elif deckU > 21:
        return "You Lose, Beyond 21"
    elif deckC> 21:
        return "Congrats, Computer Lost Beyond 21"
    else:
        if deckC> deckU:
            return "YOu lose, your opponent has higher value"
        else:
            return "Congrats, You Win with higher value"

def play():
    print(blackjack_logo)
    computer = []
    user = []
    for numbers in range(2):
        user.append(deal_card())
        computer.append(deal_card())




    cont = False
    while cont == False:
        comp_score = calculate_score(computer)
        user_score = calculate_score(user)

        print(f"Your Card: {user}, Current Score is {user_score}")
        print(f"Computer's first card is {computer[0]}")

        if user_score < 21 and user_score != 0 and comp_score != 0:
            decision = input("Do you want to continue? 'y' or 'n': ")
            if decision == 'y':
                user.append(deal_card())
            elif decision == 'n':
                cont = True
        else:
            cont = True
    while comp_score < 17 and comp_score != 0:
        computer.append(deal_card())
        comp_score = calculate_score(computer)


    print(f"Your final deck of cards is {user}, Current Score is {user_score}")
    print(f"Computer's final card is {computer}, its final deck of card is {comp_score}")
    print(compare(comp_score, user_score))


while input("Do you want to play a game of Black Jack 'y' or 'n' ") == 'y':
    clear()
    play()




