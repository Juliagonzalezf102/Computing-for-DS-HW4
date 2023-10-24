# %%

# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.

# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
# 1. name (str)
# 2. symptoms (list of str)
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively

# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
# This information should be stored somehow.

# 1.3)
# Create a method called has_covid()
# which takes no parameters.
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19

# The probability should work as follows:

# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']

import math
from abc import ABC, abstractmethod
import random
from itertools import permutations
import itertools


class Patient:
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms
        self.tests = {}

    def add_test(self, test_name, results):
        self.tests[test_name] = results

    def has_covid(self):
        probability = 0.05

        for symptom in ['fever', 'cough', 'anosmia']:
            if symptom in self.symptoms:
                probability += 0.1

        if 'Covid' in self.tests:
            return 0.99 if self.tests['Covid'] == 'True' else 0.01

        for test_name, test_name in self.tests.items():
            if test_name != 'Covid':
                return probability

        return probability


# Test class for a Patient with Covid and check prob return is 0.99
patient1 = Patient('Julia', ['fever', 'cough', 'anosmia'])
patient1.add_test('Covid', 'True')
covid_probability = patient1.has_covid()
print(covid_probability)

# Test class for a Patient with Covid test with false result and check prob
# retun is 0.01
patient2 = Patient('Julia', ['fever', 'cough'])
patient2.add_test('Covid', 'False')
covid_probability = patient2.has_covid()
print(covid_probability)

# Test class for a Patient with no Covid and check prob return is 0.05 + 0.01
# for each additional symptom
patient3 = Patient('Julia', ['fever', 'cough'])
patient3.add_test('Flu', 'True')
covid_probability = patient3.has_covid()
print(covid_probability)

# %%
# 2. In this exercise you will make an English Deck class made of Card classes
# the Card class should represent each of the cards
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.

# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck
# (suits: Hearts, Diamonds, Clubs, Spades and values:
# A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create
# a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly.
# Create a method called "draw" that will draw a single card and print the suit and value.
# When a card is drawn, the card should be removed from the deck.


# %%

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck(Card):
    def __init__(self):
        super().__init__(suit=None, value=None)
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A', '2', '3', '4', '5',
                       '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.shuffled_cards = {}

    def shuffle(self):
        shuffled_cards = list(itertools.product(self.suits, self.values))
        random.shuffle(shuffled_cards)
        self.shuffled_cards = shuffled_cards

    def draw(self):
        if not self.shuffled_cards:
            print('No more cards can be drawn')
            return None

        random_draw = random.choice(self.shuffled_cards)
        self.shuffled_cards.remove(random_draw)
        return random_draw, self.shuffled_cards


deck = Deck()
deck.shuffle()

while True:
    drawn_card = deck.draw()
    if drawn_card:
        card, updated_deck = drawn_card
        print("Drawn card:", card)
    else:
        print("No more cards can be drawn.")
        break


# %%
# 3. In this exercise you will create an interface that will
# serve as template for different figures to compute their
# perimeter and surface.

# 3.1 Create an abstract class (interface) called "PlaneFigure"
# with two abstract methods:
# compute_perimeter() that will implement the formula to compute
# the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute
# the surface of the plane figure.

class PlaneFigure(ABC):  # abstract class
    # create tow abstract methods:
    def compute_perimeter(self):
        pass

    def compute_surface(self):
        pass

# 3.2 Create a child class called "Triangle" that inherits
# from "PlaneFigure" and has as parameters in the constructor
# "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2"
# the other two sides of the triangle and "h" the height). Implement
# the abstract methods with the formula of the triangle.


class Triangle(PlaneFigure):
    def __init__(self, base, c1, c2, h):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.height = h

    def compute_perimeter(self):
        return self.c1 + self.c2 + self.base

    def compute_surface(self):
        return (self.base*self.height)/2

# 3.3 Create a child class called "Rectangle" that inherits from
# "PlaneFigure" and has as parameters in the constructor "a", "b"
# (sides of the rectangle). Implement the abstract methods with the
# formula of the rectangle.


class Rectangle(PlaneFigure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_perimeter(self):
        return ((self.a)*2) + ((self.b)*2)

    def compute_surface(self):
        return (self.a * self.b)

# 3.3 Create a child class called "Circle" that inherits from
# "PlaneFigure" and has as parameters in the constructor "radius"
# (radius of the circle). Implement the abstract methods with
# the formula of the circle.


class Circle(PlaneFigure):
    def __init__(self, radius):
        self.radius = radius

    def compute_perimeter(self):
        return 2*math.pi*self.radius

    def compute_surface(self):
        return math.pi*(self.radius)**2


# Example for triangle
triangle = Triangle(3, 4, 5, 6)
triangle_perimeter = triangle.compute_perimeter()
triangle_surface = triangle.compute_surface()
print(triangle_perimeter)
print(triangle_surface)

# Example for Rectangle
Rectangle = Rectangle(3, 4)
rectangle_perimeter = Rectangle.compute_perimeter()
rectangle_surface = Rectangle.compute_surface()
print(rectangle_perimeter)
print(rectangle_surface)

# Example for Circle
circle = Circle(4)
circle_perimeter = circle.compute_perimeter()
circle_surface = circle.compute_surface()
print(circle_perimeter)
print(circle_surface)
