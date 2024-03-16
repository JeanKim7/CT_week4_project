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
            "Ace": 0
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
        self.count = 0
        self.ace_count = 0
        self.money = 0
        self.current_bet = 0

    def place_bet(self):
        bet_amount =input("How much would you like to bet? $")
        while float(bet_amount) == False:
            print("Please enter a number only!")
            bet_amount =input("How much would you like to bet? $")
        while float(bet_amount) >self.money:
            print(f"You can't bet more than the amount you cashed in!")
            bet_amount =input("How much would you like to bet? $")
        self.current_bet = bet_amount

    def initial_cards(self):
        first_card = Card()
        second_card = Card()
        first_card.choose_card()
        second_card.choose_card()
        self.cards.append(first_card)
        self.cards.append(second_card)
        for card in self.cards:
            if card.face == "A" and self.ace_count == 0:
                card.value = 11
                self.ace_count += 1
            elif card.face == "A" and self.ace_count >=1:
                card.value = 1
                self.ace_count += 1
        self.count += (first_card.value +second_card.value)

    def hit(self):
        new_card = Card()
        new_card.choose_card()
        self.cards.append(new_card)
        if self.count <= 10:
            if new_card.face == "A" and self.ace_count == 0:
                new_card.value = 11
                self.ace_count += 1
            elif new_card.face == "A" and self.ace_count >=1:
                new_card.value = 0
                self.ace_count+= 1
        else:
            if new_card.face == "A":
                new_card.value = 0
                self.ace_count+= 1
        self.count += new_card.value


class Dealer:
    """Object representing a dealer"""
    
    def __init__(self):
        self.cards = []
        self.count = 0
        self.ace_count = 0

    def initial_cards(self):
        first_card = Card()
        second_card = Card()
        first_card.choose_card()
        second_card.choose_card()
        self.cards.append(first_card)
        self.cards.append(second_card)
        for card in self.cards:
            if card.face == "A" and self.ace_count == 0:
                card.value = 11
                self.ace_count += 1
            elif card.face == "A" and self.ace_count >=1:
                card.value = 1
                self.ace_count += 1
        self.count += (first_card.value +second_card.value)

    def hit(self):
        new_card = Card()
        self.cards.append(new_card)
        if self.count <= 10:
            if new_card.face == "A" and self.ace_count == 0:
                new_card.value = 11
                self.ace_count += 1
            elif new_card.face == "A" and self.ace_count >=1:
                new_card.value = 1
                self.ace_count+= 1
        else:
            if new_card.face == "A":
                new_card.value = 1
                self.ace_count+= 1
        self.count += new_card.value

