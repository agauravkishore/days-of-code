import random
from art import logo

# List of cards in blackjack where 11 represents Ace
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pick_card(number):
    """
    Function to allow the user to pick cards until they choose to stop or go over 21.
    Returns the total count of cards picked.
    """
    user_count = number
    while number < 21:
        choice = input("Do you want to pick another card: y or n\n").lower()
        if choice == "y":
            ucard = cards[random.randrange(0, 13)]  # Randomly pick a card from the list
            number += ucard
            print(f"You get {ucard}, New total = {number}")
        else:
            return number
    if number > 21:
        print("You Lose")
    elif number == 21:
        print("You win")
    return user_count

def dealer(count):
    """
    Function for the dealer to pick cards until their count reaches 16 or higher.
    Returns the total count of cards picked by the dealer.
    """
    dcount = count
    while dcount < 16:
        dcard = cards[random.randrange(0, 13)]  # Randomly pick a card from the list
        dcount += dcard
    return dcount

def winner(user, dealer):
    """
    Function to determine the winner based on the user's and dealer's card counts.
    Prints the result of the game.
    """
    if user > 21:
        print("You Lose")
    elif user < dealer:
        if dealer > 21:
            print("You win")
        else:
            print("You lose")
    elif user > dealer:
        print("You Win")
    elif user == dealer:
        print("That's a Draw")
    else:
        print("You lose")

def deal_cards():
    """
    Function to deal initial cards to the user and dealer, then execute the game logic.
    """
    user_count = 0
    dealcard_1 = cards[random.randrange(0, 13)]
    dealcard_2 = cards[random.randrange(0, 13)]
    ucard_1 = cards[random.randrange(0, 13)]
    ucard_2 = cards[random.randrange(0, 13)]
    user_count = ucard_1 + ucard_2
    deal_count = dealcard_1 + dealcard_2
    
    print(f"The Dealer cards are {dealcard_1} and {dealcard_2}")
    print(f"Your Cards are {ucard_1} and {ucard_2}, Total is {user_count}")
    
    final_ucount = pick_card(user_count)
    final_dcount = dealer(deal_count)
    
    print(f"Final User count = {final_ucount}")
    print(f"Final Dealer count = {final_dcount}")
    
    winner(final_ucount, final_dcount)

def game_start():
    """
    Function to start the game, asking the user if they want to play.
    """
    print(logo)
    print("Welcome to Blackjack!")
    play = input("Do you want to play Blackjack? Type 'y' or 'n': ").lower()
    if play == "y":
        deal_cards()
    else:
        print("Goodbye")

# Start the game
game_start()
