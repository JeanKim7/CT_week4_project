# ## Python Blackjack
# For this project you will make a Blackjack game using Python. Click <a href="http://www.hitorstand.net/strategy.php">here</a> to familiarize yourself with the the rules of the game. You won't be implementing every rule "down to the letter" with the game, but we will doing a simpler version of the game. This assignment will be given to further test your knowledge on object-oriented programming concepts.

# ### Rules:

# `1. ` The game will have two players: the Dealer and the Player. The game will start off with a deck of 52 cards. The 52 cards will consist of 4 different suits: Clubs, Diamonds, Hearts and Spades. For each suit, there will be cards numbered 1 through 13. <br>
# **Note: No wildcards will be used in the program**

# `2. ` When the game begins, the dealer will shuffle the deck of cards, making them randomized. After the dealer shuffles, it will deal the player 2 cards and will deal itself 2 cards from. The Player should be able to see both of their own cards, but should only be able to see one of the Dealer's cards.
 
# `3. ` The objective of the game is for the Player to count their cards after they're dealt. If they're not satisfied with the number, they have the ability to 'Hit'. A hit allows the dealer to deal the Player one additional card. The Player can hit as many times as they'd like as long as they don't 'Bust'. A bust is when the Player is dealt cards that total more than 21.

# `4. ` If the dealer deals the Player cards equal to 21 on the **first** deal, the Player wins. This is referred to as Blackjack. Blackjack is **NOT** the same as getting cards that equal up to 21 after the first deal. Blackjack can only be attained on the first deal.

# `5. ` The Player will never see the Dealer's hand until the Player chooses to 'stand'. A Stand is when the player tells the dealer to not deal it anymore cards. Once the player chooses to Stand, the Player and the Dealer will compare their hands. Whoever has the higher number wins. Keep in mind that the Dealer can also bust. 

import time, Player, Dealer, Card

class BlackJack:

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()

    def cash_in(self):
        cashin = input("How much would you like to cash in for? \n$")
        self.player.money = float(cashin)

    def shuffle_deal(self):
        self.player.place_bet()
        print("Shuffling and dealing cards...")
        time.sleep(2)
        self.player.intial_cards()
        self.dealer.intial_cards()
        print(f"The dealer has the {self.dealer.cards[0]} and another face-down card.\n"
              f"\nYou have the {self.player.cards[0]} and {self.player.cards[1]}")
        if self.player.count == 21:
            self.stand()

        
    def hit_player(self):
        self.player.hit()
        print(f"You now have a count of {self.player.count}:")
        for card in self.player.cards:
            print(card)
        if self.player.count == 21:
            self.stand()
        elif self.player.count > 21:
            self.__lost()
    
    def __lost(self):
        self.player.money -= self.player.current_bet
        self.__reset()
        print(f"Sorry, you got over 21, you busted! You now have ${self.player.money:.2f}")

    def __reset(self):
        Card.chosen_cards = []
        self.player.cards = []
        self.player.count = 0
        self.player.ace_count = 0
        self.player.current_bet = 0
        self.dealer.cards = []
        self.dealer.count = 0
        self.dealer.ace_count = 0

    def stand(self):
        print(f"The dealer's hand is {self.dealer.cards[0]} and {self.dealer.cards[1]}.")
        if self.dealer.count >= 17 and self.dealer.count<=21:
            if self.player.count > self.dealer.count:
                self.player.money += self.player.bet
                print(f"Congratulations, you won! You now have ${self.player.money:.2f}")
                self.__reset()
            elif self.player.count < self.dealer.count:
                self.__lost()
            else:
                print("It's a draw. Place another bet to play again!")
                self.__reset()
        elif self.dealer.count<17:
            while self.dealer.count<17:
                self.dealer.hit()
                print(f"The dealer has a count of {self.dealer.count}:")
                for card in self.dealer.cards:
                    print(card)
            if self.dealer.count >= 17 and self.dealer.count<=21:
                if self.player.count > self.dealer.count:
                    self.player.money += self.player.bet
                    print(f"Congratulations, you won! You now have ${self.player.money:.2f}")
                    self.__reset()
                elif self.player.count < self.dealer.count:
                    self.__lost()
                else:
                    print("It's a draw. Place another bet to play again!")
                    self.__reset()
            else:
                self.player.money += self.player.bet
                print(f"Congratulations, you won! You now have ${self.player.money:.2f}")
                self.__reset()
                
            

    
        


