import random

class Card:
    """Class that represents a card"""

    #List of cards that have been drawn already
    chosen_cards = []

    def __init__(self):
        self.suit = None
        self.value = None
        self.face = None

    def __str__(self):
        return f"{self.face} of {self.suit}"
    
    def __repr__(self):
        return f"< {self.face} | {self.suit} >"
    
    # Assign value to random card
    def choose_card(self):
        suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
        faces = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10,
            # Assign ace value as 11 but change it in later functions to 1 if needed
            "Ace": 11
            }
        
        self.suit = random.choice(suits)
        self.face = random.choice(list(faces.keys()))
        self.value = faces[self.face]

        # Choose another card if card has been chosen already
        if [self.suit, self.face] in Card.chosen_cards:
            self.choose_card()
        # Add new card to chosen cards list
        else:
            Card.chosen_cards.append([self.suit, self.face])

class Player:
    """Object representing a player"""
    
    def __init__(self):
        self.cards = []
        self.count = 0
        self.ace_count = 0
        self.money = 0
        self.current_bet = 0

    # Input to see how much money is in a bet
    def place_bet(self):
        bet_amount =input("How much would you like to bet?\n$")
        # Reprint input if inputs are incorrect
        while float(bet_amount) == False:
            print("Please enter a number only!")
            bet_amount =input("How much would you like to bet?\n$")
        while float(bet_amount) >self.money:
            print(f"You can't bet more than the amount you cashed in!")
            bet_amount =input("How much would you like to bet?\n$")
        self.current_bet = float(bet_amount)

    # Deal first two cards
    def initial_cards(self):
        first_card = Card()
        second_card = Card()
        first_card.choose_card()
        second_card.choose_card()
        self.cards.append(first_card)
        self.cards.append(second_card)

        #Assign first ace value of 11 and subsequent aces are value of 1
        for card in self.cards:
            if card.face == "Ace" and self.ace_count == 0:
                card.value = 11
                self.ace_count += 1
            elif card.face == "Ace" and self.ace_count >= 1:
                card.value = 1
                self.ace_count += 1
        self.count += (first_card.value +second_card.value)

    # If player hits, add new card to hand
    def hit(self):
        new_card = Card()
        new_card.choose_card()
        self.cards.append(new_card)

        # Assign ace value of 11 only if current count is less than or equal to 10
        if self.count <= 10:
            if new_card.face == "Ace" and self.ace_count == 0:
                new_card.value = 11
                self.ace_count += 1
            elif new_card.face == "Ace" and self.ace_count >=1:
                new_card.value = 1
                self.ace_count+= 1
        
        # Assign ace value of 1 if count is over 10 to prevent automatic bust
        else:
            if new_card.face == "Ace":
                new_card.value = 1
                self.ace_count+= 1
        self.count += new_card.value

        # Assign first ace value of 1 if count is over 21 to prevent busting uneccesarily
        if self.count > 21 and "Ace" in [card.face for card in self.cards]:
            for card in self.cards:
                if card.face == "Ace":
                    card.value = 1
                    # break since only first ace value will have to be changed
                    break
            self.count = 0
            for card in self.cards:
                self.count += card.value



class Dealer:
    """Object representing a dealer"""
    
    def __init__(self):
        self.cards = []
        self.count = 0
        self.ace_count = 0

    # Same as player class
    def initial_cards(self):
        first_card = Card()
        second_card = Card()
        first_card.choose_card()
        second_card.choose_card()
        self.cards.append(first_card)
        self.cards.append(second_card)
        for card in self.cards:
            if card.face == "Ace" and self.ace_count == 0:
                card.value = 11
                self.ace_count += 1
            elif card.face == "Ace" and self.ace_count >= 1:
                card.value = 1
                self.ace_count += 1
        self.count += (first_card.value +second_card.value)

    # same as player class
    def hit(self):
        new_card = Card()
        new_card.choose_card()
        self.cards.append(new_card)
        if self.count <= 10:
            if new_card.face == "Ace" and self.ace_count == 0:
                new_card.value = 11
                self.ace_count += 1
            elif new_card.face == "Ace" and self.ace_count >=1:
                new_card.value = 1
                self.ace_count+= 1
        else:
            if new_card.face == "Ace":
                new_card.value = 1
                self.ace_count+= 1
        self.count += new_card.value
        if self.count > 21 and self.ace_count >=1:
            for card in self.cards:
                if card.face == "Ace":
                    card.value = 1
                    break
            self.count = 0
            for card in self.cards:
                self.count += card.value