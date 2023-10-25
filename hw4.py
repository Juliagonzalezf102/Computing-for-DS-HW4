###########################################
#%%
#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively

'''
solved below as a whole
'''

#
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.

'''
solved below as a whole
'''

#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']

class Patient:
    
    def __init__(self, name: str, symptoms: list):
        self.name = name
        self.symptoms = symptoms
        self.test = {}
    
    def add_test(self, test_name: str, test_results: bool):
        self.test[test_name] = test_results
    
    def has_covid(self):
        if 'covid' in self.test and self.test['covid']:
            return 0.99
        elif 'covid' in self.test and not self.test['covid']:
            return 0.01
        else:
            prob = 0.05
            for symptom in self.symptoms:
                if symptom in ['fever', 'cough', 'anosmia']:
                    prob += 0.1
            return prob

William = Patient('William', [#'fever',
                            'cough',
                            'anosmia'
                            ])
William.add_test('covid', False)
print(William.has_covid())

#%%
######################

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.


# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.

import numpy as np

class Card:
    
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value

class Deck:
    
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                        'J', 'Q', 'K']:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        np.random.shuffle(self.cards)
    
    def draw(self):
        self.shuffle()
        card = self.cards.pop()
        #print(f'{card.value} of {card.suit}')
        return f"{card.value} of {card.suit}"

np.random.seed(168)
english_deck = Deck()

result = []
while True:
    result.append(english_deck.draw())
    if len(english_deck.cards) == 0:
        break

print(len(result))
display(result)

#%%
###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.

# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.

# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.

# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.

@PlaneFigure.register
