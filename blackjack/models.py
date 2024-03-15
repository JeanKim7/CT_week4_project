import random

class Card:
    """Class that represents a card"""

    chosen_cards = []

    def __init__(self):
        self.suit = None
        self.value = None
        self.face = None

    def __str__(self):
        return f"{self.face} of {self.suit}"
    
    def __repr__(self):
        return f"< {self.face} | {self.suit} >"
    
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
            "Ace": [1, 11]
            }
        
        self.suit = random.choice(suits)
        self.face = random.choice(list(faces.keys()))
        self.value = faces[self.face]
        if [self.suit, self.face] in Card.chosen_cards:
            self.choose_card()
        else:
            Card.chosen_cards.append([self.suit, self.face])

# ====Testing Card Class====
# lst = [Card() for i in range(1, 53)]
# empty_lst = []

# for card in lst:
#     card.choose_card()
#     empty_lst.append(card)

# print(empty_lst)

# count = 0
# for card in empty_lst:
#     if card.suit == "Hearts":
#         count+=1

# print(count)
            
class Player:
    """Object representing a player"""
    
    def __init__(self):
        self.cards = []

    def initial_card(self):
        first_card = Card()
        second_card = Card()
        self.cards.append(first_card)
        self.cards.append(second_card)

    def hit(self):
        new_card = Card()
        self.cards.append(new_card)

class Dealer:
    """Object representing a dealer"""
    
    def __init__(self):
        self.cards = []

    def initial_card(self):
        first_card = Card()
        second_card = Card()
        self.cards.append(first_card)
        self.cards.append(second_card)

    def hit(self):
        new_card = Card()
        self.cards.append(new_card)

