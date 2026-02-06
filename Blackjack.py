import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
def calculate_score(cards):
    """Takes a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        #Blackjack
        return 0
    if 11 in cards and sum(cards) > 21 :
        #Ace handling
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack!"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print(logo)
    choices = True
    users_card = []
    computer_card = []
    computer_score = 0
    users_score = 0
    for i in range(2):
        users_card.append(deal_card())
        computer_card.append(deal_card())
    while choices:
        users_score = calculate_score(users_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {users_card}, current score: {users_score}")
        print(f"Computer's first card [{computer_card[0]}]")
        if users_score > 21 or users_score == 0 or computer_score == 0:
            choices = False
        else:
            answer=input("Type 'y' to get another card, type 'n' to pass: ")
            if answer == "y":
                users_card.append(deal_card())
            elif answer == "n":
                choices = False
            else:
                print("Invalid choice!")
                choices = False
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {users_card}, final score: {users_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(users_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n"*100)
    play_game()
