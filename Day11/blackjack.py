import random
import art

# BlackJack Project
# Variables 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_in_progress = True
winner = False

# Function to deal starting hand
def deal_hand():
    return [cards[random.randrange(0, len(cards))], cards[random.randrange(0, len(cards))]]

# Check for bust
def bust_check(score):
    if score > 21:
        return True
    else:
        return False
    
# Add a card to hand
def draw_card(hand):
    hand.append(cards[random.randrange(0, len(cards))])

# Calculate score
def calculate_score(cards):
    # If blackjack return 0 else return score
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # If user has an ace and goes over 21 replace the value with 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Blackjack check
def blackjack_check(computer_score, player_score):
    if computer_score == 0:
        print(f"Your hand is {player_cards} and the Dealer's hand is {computer_cards}")
        print("Dealer has 21! You lose!")
        return True
    elif player_score == 0:
        print(f"Your hand is {player_cards} and the Dealer's hand is {computer_cards}")
        print("You have 21! You win!")
        return True
    else:
        return False
    
# Gameplay
while game_in_progress:
    # Logo
    print(art.logo)
    
    # Deal hands
    computer_cards = deal_hand()
    player_cards = deal_hand()

    # Sum of cards
    computer_score = calculate_score(computer_cards)
    player_score = calculate_score(player_cards)

    # Check for blackjack
    winner = blackjack_check(computer_score, player_score)

    # Player hit or stay
    while not bust_check(player_score) and not winner:
        # Input validation
        while True:
            try:
                print(f"Your hand is {player_cards} and the Dealer's first card is {computer_cards[0]}")
                another_card = input("Would you like another card? y/n ").lower()
                # New line for console
                print("\n")   
                # Hit or stay
                if another_card == "y":
                    draw_card(player_cards)
                    player_score = calculate_score(player_cards)
                    if player_score == 0:
                        print("You have 21! You win!")
                        winner = True
                    break
                elif another_card == "n":
                    break
                else:
                    print("Please input 'y' or 'n'.")
            except ValueError:
                print("Please input 'y' or 'n'.")
        
        if another_card == "n":
            break

        
    
    # Bust check for player
    if bust_check(player_score):
        print(f"Your hand is {player_cards} and the Dealer's hand is {computer_cards}")
        print("You have bust! You lose!")
        winner = True


    # Computer plays
    while computer_score < 17 and not winner:
        draw_card(computer_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Dealer hits. Dealer's hand is {computer_cards}")

        if computer_score == 0:
            print("Dealer has 21! You lose!")
            winner = True
        
        if bust_check(computer_score):
            print("Dealer has bust! You win!")
            winner = True

    # Decide the winner
    if not winner:
        print(f"Your final hand is {player_cards} and the Dealer's final hand is {computer_cards}.")
        if player_score > computer_score:
            print(f"You have {player_score} and the Dealer has {computer_score}! You win!")
        elif player_score == computer_score:
            print(f"You have {player_score} and the Dealer has {computer_score}! It's a push!")
        else:
            print(f"You have {player_score} and the Dealer has {computer_score}! Dealer wins!")
        
        winner = True

    # Input validation
    while True:
        try:
            play_again = input("Would you like to play again? y/n ").lower()

            if play_again == "y":
                winner = False
                # Clear the console
                print("\033c", end="", flush=True)
                break
            elif play_again == "n":
                game_in_progress = False
                break
            else:
                print("Please input 'y' or 'n'.")
        except ValueError:
            print("Please input 'y' or 'n'.")
