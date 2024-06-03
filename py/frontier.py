#!/usr/bin/python
print('Content-type: text/html\n')

import cgi#Used to get data from website
data = cgi.FieldStorage()

#HTML stuff
HTML_HEADER = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>A Game of Hangman</title>
</head>

<body>"""

HTML_FOOTER = """</body>

</html>"""


#Actual code
import random

word_bank = {'fruits': ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'lemon', 'lime', 'mango', 'melon', 'orange', 'peach', 'pear', 'plum', 'berry', 'papaya', 'guava', 'apricot', 'avocado', 'coconut', 'lychee', 'nectarine', 'persimmon', 'pineapple', 'pomegranate', 'raspberry', 'strawberry', 'blueberry', 'blackberry', 'cranberry'], 'animals': ['dog', 'cat', 'horse', 'cow', 'pig', 'sheep', 'goat', 'chicken', 'duck', 'turkey', 'rabbit', 'mouse', 'rat', 'deer', 'fox', 'wolf', 'bear', 'lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'monkey', 'ape', 'gorilla', 'panda', 'kangaroo', 'koala', 'eagle', 'hawk', 'owl', 'crow', 'raven', 'parrot', 'pigeon', 'sparrow', 'fish', 'shark', 'dolphin', 'whale', 'seal', 'otter', 'turtle', 'snake', 'lizard', 'frog', 'toad', 'bee', 'ant', 'spider', 'butterfly', 'moth', 'bat', 'camel', 'hedgehog', 'squirrel'], 'common plants': ['rose', 'tulip', 'daisy', 'lily', 'fern', 'ivy', 'bamboo', 'cactus', 'oak', 'maple', 'pine', 'palm', 'aloe', 'lavender', 'orchid', 'sunflower', 'moss', 'basil', 'mint', 'thyme', 'sage', 'rosemary', 'parsley', 'cilantro', 'jasmine', 'hibiscus', 'dandelion', 'marigold', 'hydrangea', 'azalea', 'peony', 'begonia', 'chrysanthemum', 'violet', 'daffodil', 'poppy', 'clover', 'elm', 'birch', 'willow', 'geranium', 'ficus'], 'electronics': ['phone', 'laptop', 'tablet', 'monitor', 'keyboard', 'mouse', 'printer', 'scanner', 'camera', 'speaker', 'microphone', 'headphone', 'smartwatch', 'router', 'modem', 'television', 'console', 'drone', 'projector', 'amplifier', 'receiver', 'thermostat', 'smartwatch', 'e-reader', 'server', 'harddrive', 'processor', 'motherboard', 'joystick', 'webcam', 'camcorder', 'walkie-talkie', 'earbuds', 'charger'], 'kitchenware': ['knife', 'fork', 'spoon', 'plate', 'bowl', 'cup', 'glass', 'mug', 'pot', 'pan', 'skillet', 'grater', 'peeler', 'whisk', 'ladle', 'spatula', 'tongs', 'colander', 'sieve', 'kettle', 'toaster', 'blender', 'mixer', 'oven', 'stove', 'microwave', 'juicer', 'strainer', 'cuttingboard', 'rollingpin', 'measuringcup', 'measuring spoon', 'bakingdish', 'casserole', 'saucepan', 'pressurecooker', 'slowcooker', 'airfryer', 'breadmaker', 'coffeemaker', 'teapot', 'pitcher', 'thermos', 'tray'], 'common words': ['the', 'and', 'of', 'to', 'a', 'in', 'that', 'is', 'it', 'was', 'for', 'as', 'with', 'on', 'he', 'she', 'at', 'by', 'this', 'we', 'you', 'not', 'but', 'from', 'have', 'they', 'his', 'her', 'which', 'or', 'what', 'can', 'all', 'their', 'there', 'if', 'will', 'up', 'one', 'about', 'who', 'out', 'some', 'then', 'into', 'them', 'these', 'no', 'time', 'its', 'two', 'more', 'do', 'has', 'like', 'only', 'see', 'could', 'make', 'first', 'any', 'well', 'after', 'where', 'over', 'years', 'old'], 'condiments': ['salt', 'pepper', 'ketchup', 'mustard', 'mayonnaise', 'vinegar', 'soy', 'hot sauce', 'barbecue sauce', 'salsa', 'relish', 'honey', 'jam', 'chutney', 'ranch', 'pesto'], 'geometry': ['point', 'line', 'angle', 'triangle', 'square', 'rectangle', 'circle', 'sphere', 'cube', 'pyramid', 'cylinder', 'cone', 'polygon', 'vertex', 'edge', 'face', 'perimeter', 'area', 'volume', 'diameter', 'radius', 'circumference'], 'careers': ['doctor', 'nurse', 'teacher', 'engineer', 'scientist', 'programmer', 'artist', 'musician', 'writer', 'chef', 'baker', 'architect', 'carpenter', 'plumber', 'electrician', 'mechanic', 'pilot', 'firefighter', 'police officer', 'lawyer', 'judge', 'accountant', 'banker', 'entrepreneur', 'manager', 'receptionist', 'secretary', 'librarian', 'farmer', 'gardener', 'veterinarian', 'dentist', 'pharmacist', 'therapist', 'social worker', 'psychologist', 'actor', 'director', 'producer', 'dancer', 'athlete', 'coach'], 'meat': ['beef', 'pork', 'chicken', 'turkey', 'lamb', 'duck', 'venison', 'rabbit', 'veal', 'goat', 'bison', 'elk', 'ostrich', 'quail', 'goose', 'pheasant'], 'everyday objects': ['chair', 'table', 'bed', 'desk', 'book', 'pen', 'pencil', 'computer', 'phone', 'television', 'remote', 'clock', 'mirror', 'lamp', 'shoes', 'socks', 'clothes', 'bag', 'wallet', 'key']}

#selecting word
n0 = list(word_bank.keys())
r = random.randrange(len(n0))
hint = n0[r]
n1 = word_bank[hint]
r = random.randrange(len(n1))
word = n1[r]    

#other necessary things
repeats = []
clue = "_ " * len(word)
print('This is a Hangman Game(without the Hangman). You will be given a hint and the amount of letters in the word. Your objective is to correctly guess the word in 10 tries. Right guesses will not be counted towards the number of tries. To guess, use the guess func: guess("x"). Replace x with any letter or word. Limit your input to only alphabetical letters and only lowercase letters.\nHint:', hint, '\n', clue)
chance = 10

def index(s, g):
    s = list(s)
    i = 0
    n = []
    for e in s:
        if e == g:
            n += [i]
        i += 1
    return n

def guess(s):
    global repeats
    global word
    global clue
    global chance
    if len(s) > 1:
        if s == word:
            print(word)
            print('You Win!')
        else:
            print('Incorrect')
            print(clue)
            print('Chances:', chance)
    else:
        if not(s >= 'a' and s <= 'z'):
            print('ERROR')
        elif s in repeats:
            print('REPEAT')
        elif s in word:
            x = index(word, s)
            for e in x:
                clue = clue[:e * 2] + s + clue[(e * 2) + 1:]
            print(clue)
        else:
            chance -= 1
            if chance == 0:
                print('GAME OVER')
                print('The word is:', word)
            else:
                print('not in word')
                print('Chance:', chance)
                print(clue)
        if not("_" in clue):
            print("You Win!")
    repeats += [s]
