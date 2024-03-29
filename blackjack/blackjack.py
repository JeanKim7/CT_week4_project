# ## Python Blackjack
# For this project you will make a Blackjack game using Python. Click <a href="http://www.hitorstand.net/strategy.php">here</a> to familiarize yourself with the the rules of the game. You won't be implementing every rule "down to the letter" with the game, but we will doing a simpler version of the game. This assignment will be given to further test your knowledge on object-oriented programming concepts.

# ### Rules:

# `1. ` The game will have two players: the Dealer and the Player. The game will start off with a deck of 52 cards. The 52 cards will consist of 4 different suits: Clubs, Diamonds, Hearts and Spades. For each suit, there will be cards numbered 1 through 13. <br>
# **Note: No wildcards will be used in the program**

# `2. ` When the game begins, the dealer will shuffle the deck of cards, making them randomized. After the dealer shuffles, it will deal the player 2 cards and will deal itself 2 cards from. The Player should be able to see both of their own cards, but should only be able to see one of the Dealer's cards.
 
# `3. ` The objective of the game is for the Player to count their cards after they're dealt. If they're not satisfied with the number, they have the ability to 'Hit'. A hit allows the dealer to deal the Player one additional card. The Player can hit as many times as they'd like as long as they don't 'Bust'. A bust is when the Player is dealt cards that total more than 21.

# `4. ` If the dealer deals the Player cards equal to 21 on the **first** deal, the Player wins. This is referred to as Blackjack. Blackjack is **NOT** the same as getting cards that equal up to 21 after the first deal. Blackjack can only be attained on the first deal.

# `5. ` The Player will never see the Dealer's hand until the Player chooses to 'stand'. A Stand is when the player tells the dealer to not deal it anymore cards. Once the player chooses to Stand, the Player and the Dealer will compare their hands. Whoever has the higher number wins. Keep in mind that the Dealer can also bust. 

import time 
from models import Player, Dealer, Card

class BlackJack:

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()

    # function to add initial amount of money
    def cash_in(self):
        cashin = input("How much would you like to cash in for? \n$")
        self.player.money = float(cashin)

    # Deal first 2 cards and print hands
    def shuffle_deal(self):
        self.player.place_bet()
        print("\nShuffling and dealing cards...\n")
        time.sleep(2)
        self.player.initial_cards()
        self.dealer.initial_cards()
        print(f"The dealer has\n=== the {self.dealer.cards[0]} and another face-down card. ===\n"
              f"\nYou have the\n=== {self.player.cards[0]} and {self.player.cards[1]} ===\n")
        if self.player.count == 21:
            self.stand()

    # function if player wants to hit    
    def hit_player(self):
        self.player.hit()
        print(f"\nYou now have:\n")
        print("====")
        for card in self.player.cards:
            print(card)
        print("====\n")
        # Check dealer's hand if player's hand is 21
        if self.player.count == 21:
            self.stand()
        # Lost if player's hand is over 21
        elif self.player.count > 21:
            print("You got over 21 and busted!")
            self.__lost()

    # deduct money if player loses and reset all hands and cards taken out of deck
    def __lost(self):
        self.player.money -= self.player.current_bet
        self.__reset()
        print(f"Sorry, you lost! You now have ${self.player.money:.2f}\n")

    # clear player's and ealer's hands and make sure no cards have been chosen to simulate a new deck
    def __reset(self):
        Card.chosen_cards = []
        self.player.cards = []
        self.player.count = 0
        self.player.ace_count = 0
        self.player.current_bet = 0
        self.dealer.cards = []
        self.dealer.count = 0
        self.dealer.ace_count = 0

    # function for when the player's hand is finished
    def stand(self):
        print(f"\nThe dealer has a count of {self.dealer.count} and has\n==== the {self.dealer.cards[0]} and the {self.dealer.cards[1]} ====\n")
        # compare dealer's and player's hands if dealer's initial hand is 17 or higher, dealer does not need to hit
        if self.dealer.count >= 17 and self.dealer.count<=21:
            if self.player.count > self.dealer.count:
                self.player.money += self.player.current_bet
                print(f"Congratulations, you won! Your count is higher than the dealer's! You now have ${self.player.money:.2f}\n")
                self.__reset()
            elif self.player.count < self.dealer.count:
                print("You have a count lower than the dealer!")
                self.__lost()
            # reset hand if player and dealer draw
            else:
                print("It's a draw. Place another bet to play again!\n")
                self.__reset()
        # dealer hits if their hand has a count less than 17
        elif self.dealer.count<17:
            # keep hitting until dealer's hand count is over 17
            while self.dealer.count<17:
                self.dealer.hit()
                print("The dealer hits.")
                print(f"The dealer has a count of {self.dealer.count} has:")
                print("\n====")
                for card in self.dealer.cards:
                    print(card)
                print("====\n")
            # compare dealer and player's hand after dealer hits and count is over 17 but does not bust
            if self.dealer.count >= 17 and self.dealer.count<=21:
                if self.player.count > self.dealer.count:
                    self.player.money += self.player.current_bet
                    print(f"Congratulations, you won! Your count is higher than the dealer's! You now have ${self.player.money:.2f}\n")
                    self.__reset()
                elif self.player.count < self.dealer.count:
                    print("You got a count lower than the dealer!")
                    self.__lost()
                else:
                    print("It's a draw. Place another bet to play again!\n")
                    self.__reset()
            # Player wins money if the dealers busts
            else:
                self.player.money += self.player.current_bet
                print(f"Congratulations, you won! You now have ${self.player.money:.2f}")
                self.__reset()
                
            

    
        


