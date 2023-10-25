# %%
# %%
#
# 1. In this exercise we will make a "Patient" class

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
#    and increases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']

from math import pi, sqrt
import math
from abc import ABC, abstractmethod
import random
from itertools import permutations
import itertools

class Patient:
    def __init__(self, name:str, symptoms:list):
        self.name = name
        self.symptoms = symptoms
        self.tests = {}

    def add_test(self, test_name, test_result):
        self.tests[test_name] = test_result

    def has_covid(self):
        if 'covid' in self.tests:
            return 0.99 if self.tests['covid'] == True else 0.01
        else:
            probability = 0.05
            for symptom in ['fever', 'cough', 'anosmia']:
                if symptom in self.symptoms:
                    probability += 0.1
        return probability


# %%

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

class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                    for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if self.cards:
            card = self.cards.pop()
            print(f"You drew the {card.value} of {card.suit}")
        
        else:
            print("No more cards to draw.")


#%%

# 3. In this exercise you will create an interface that will serve as template
# for different figures to compute their perimeter and surface.

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimeter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.

# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.

# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.

# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.


# 3.1 Create an abstract class (interface) called "PlaneFigure"

class PlaneFigure(ABC):

    @abstractmethod
    def compute_perimeter(self):
        pass

    @abstractmethod
    def compute_surface(self):
        pass

# 3.2 Create a child class called "Triangle"


class Triangle(PlaneFigure):

    def __init__(self, base: int, c1: int, c2: int, h: int):
        if self.is_valid(base, c1, c2, h):
            self.base = base
            self.c1 = c1
            self.c2 = c2
            self.height = h
        else:
            raise ValueError("Invalid triangle dimensions")

    @staticmethod
    def is_valid(base, c1, c2, height):
        # Check if all sides and height have positive lengths
        if base > 0 and c1 > 0 and c2 > 0 and height > 0:
            # Check the triangle inequality conditions
            condition1 = base + c1 > c2
            condition2 = base + c2 > c1
            condition3 = c1 + c2 > base

            # Check the condition for height
            height_condition = height < min(c1, c2)

            # Return True if all conditions are satisfied and False otherwise
            return condition1 and condition2 and condition3 and height_condition
        else:
            return False

    def compute_perimeter(self):
        return self.base + self.c1 + self.c2

    def compute_surface(self):
        return self.base * self.height / 2

# 3.3 Create a child class called "Rectangle"


class Rectangle(PlaneFigure):

    def __init__(self, a: int, b: int):
        if self.is_valid(a, b):
            self.side_a = a
            self.side_b = b
        else:
            raise ValueError("Invalid rectangle dimensions")

    @staticmethod
    def is_valid(a, b):
        if a > 0 and b > 0:
            return True
        else:
            return False

    def compute_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def compute_surface(self):
        return self.side_a * self.side_b

# 3.4 Create a child class called "Circle"


class Circle(PlaneFigure):

    def __init__(self, radius: int):
        if self.is_valid(radius):
            self.radius = radius
        else:
            raise ValueError("Invalid circle radius")

    @staticmethod
    def is_valid(radius):
        if radius > 0:
            return True
        else:
            return False

    def compute_perimeter(self):
        return 2 * pi * self.radius

    def compute_surface(self):
        return pi * self.radius ** 2

'''
# Example Usage:
triangle = Triangle(base=3.5329, c1=4, c2=5.55, h=2)
print("Triangle Perimeter:", triangle.compute_perimeter())
print("Triangle Surface:", triangle.compute_surface())

rectangle = Rectangle(a=4.1111234, b=60.02)
print("Rectangle Perimeter:", rectangle.compute_perimeter())
print("Rectangle Surface:", rectangle.compute_surface())

circle = Circle(radius=20.56)
print("Circle Perimeter:", circle.compute_perimeter())
print("Circle Surface:", circle.compute_surface())
'''
# %%
