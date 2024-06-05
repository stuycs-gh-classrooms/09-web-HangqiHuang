#!/usr/bin/python
print('Content-type: text/html\n')

import cgi#Used to get data from website
data = cgi.FieldStorage()


#Actual code
import random

word_bank = {'fruits': ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'lemon', 'lime', 'mango', 'melon', 'orange', 'peach', 'pear', 'plum', 'berry', 'papaya', 'guava', 'apricot', 'avocado', 'coconut', 'lychee', 'nectarine', 'persimmon', 'pineapple', 'pomegranate', 'raspberry', 'strawberry', 'blueberry', 'blackberry', 'cranberry'], 'animals': ['dog', 'cat', 'horse', 'cow', 'pig', 'sheep', 'goat', 'chicken', 'duck', 'turkey', 'rabbit', 'mouse', 'rat', 'deer', 'fox', 'wolf', 'bear', 'lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'monkey', 'ape', 'gorilla', 'panda', 'kangaroo', 'koala', 'eagle', 'hawk', 'owl', 'crow', 'raven', 'parrot', 'pigeon', 'sparrow', 'fish', 'shark', 'dolphin', 'whale', 'seal', 'otter', 'turtle', 'snake', 'lizard', 'frog', 'toad', 'bee', 'ant', 'spider', 'butterfly', 'moth', 'bat', 'camel', 'hedgehog', 'squirrel'], 'common plants': ['rose', 'tulip', 'daisy', 'lily', 'fern', 'ivy', 'bamboo', 'cactus', 'oak', 'maple', 'pine', 'palm', 'aloe', 'lavender', 'orchid', 'sunflower', 'moss', 'basil', 'mint', 'thyme', 'sage', 'rosemary', 'parsley', 'cilantro', 'jasmine', 'hibiscus', 'dandelion', 'marigold', 'hydrangea', 'azalea', 'peony', 'begonia', 'chrysanthemum', 'violet', 'daffodil', 'poppy', 'clover', 'elm', 'birch', 'willow', 'geranium', 'ficus'], 'electronics': ['phone', 'laptop', 'tablet', 'monitor', 'keyboard', 'mouse', 'printer', 'scanner', 'camera', 'speaker', 'microphone', 'headphone', 'smartwatch', 'router', 'modem', 'television', 'console', 'drone', 'projector', 'amplifier', 'receiver', 'thermostat', 'smartwatch', 'server', 'harddrive', 'processor', 'motherboard', 'joystick', 'webcam', 'camcorder', 'earbuds', 'charger'], 'kitchenware': ['knife', 'fork', 'spoon', 'plate', 'bowl', 'cup', 'glass', 'mug', 'pot', 'pan', 'skillet', 'grater', 'peeler', 'whisk', 'ladle', 'spatula', 'tongs', 'colander', 'sieve', 'kettle', 'toaster', 'blender', 'mixer', 'oven', 'stove', 'microwave', 'juicer', 'strainer', 'cuttingboard', 'rollingpin', 'measuringcup', 'bakingdish', 'casserole', 'saucepan', 'pressurecooker', 'slowcooker', 'airfryer', 'breadmaker', 'coffeemaker', 'teapot', 'pitcher', 'thermos', 'tray'], 'common words': ['the', 'and', 'of', 'to', 'a', 'in', 'that', 'is', 'it', 'was', 'for', 'as', 'with', 'on', 'he', 'she', 'at', 'by', 'this', 'we', 'you', 'not', 'but', 'from', 'have', 'they', 'his', 'her', 'which', 'or', 'what', 'can', 'all', 'their', 'there', 'if', 'will', 'up', 'one', 'about', 'who', 'out', 'some', 'then', 'into', 'them', 'these', 'no', 'time', 'its', 'two', 'more', 'do', 'has', 'like', 'only', 'see', 'could', 'make', 'first', 'any', 'well', 'after', 'where', 'over', 'years', 'old'], 'condiments': ['salt', 'pepper', 'ketchup', 'mustard', 'mayonnaise', 'vinegar', 'soy', 'salsa', 'relish', 'honey', 'jam', 'chutney', 'ranch', 'pesto'], 'geometry': ['point', 'line', 'angle', 'triangle', 'square', 'rectangle', 'circle', 'sphere', 'cube', 'pyramid', 'cylinder', 'cone', 'polygon', 'vertex', 'edge', 'face', 'perimeter', 'area', 'volume', 'diameter', 'radius', 'circumference'], 'careers': ['doctor', 'nurse', 'teacher', 'engineer', 'scientist', 'programmer', 'artist', 'musician', 'writer', 'chef', 'baker', 'architect', 'carpenter', 'plumber', 'electrician', 'mechanic', 'pilot', 'firefighter', 'lawyer', 'judge', 'accountant', 'banker', 'entrepreneur', 'manager', 'receptionist', 'secretary', 'librarian', 'farmer', 'gardener', 'veterinarian', 'dentist', 'pharmacist', 'therapist', 'psychologist', 'actor', 'director', 'producer', 'dancer', 'athlete', 'coach'], 'meat': ['beef', 'pork', 'chicken', 'turkey', 'lamb', 'duck', 'venison', 'rabbit', 'veal', 'goat', 'bison', 'elk', 'ostrich', 'quail', 'goose', 'pheasant'], 'everyday objects': ['chair', 'table', 'bed', 'desk', 'book', 'pen', 'pencil', 'computer', 'phone', 'television', 'remote', 'clock', 'mirror', 'lamp', 'shoes', 'socks', 'clothes', 'bag', 'wallet', 'key']}

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
instructions = 'Instruction: This is a Hangman Game(without the Hangman). You will be given a hint and the amount of letters in the word. Your objective is to correctly guess the word in 10 tries. Right guesses will not be counted towards the number of tries. To guess, use the guess func: guess("x"). Replace x with any letter or word. Limit your input to only alphabetical letters and only lowercase letters.<br>'
chance = 10

#guessing
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
            x = word + '<br>You Win!'
        else:
            x = 'Incorrect<br>' + clue + '<br>Chances: ' + chance
    else:
        if not(s >= 'a' and s <= 'z'):
            x = 'ERROR'
        elif s in repeats:
            x= 'REPEAT'
        elif s in word:
            y = index(word, s)
            for e in y:
                clue = clue[:e * 2] + s + clue[(e * 2) + 1:]
            x = clue
        else:
            chance -= 1
            if chance == 0:
                x = 'GAME OVER<br>The word is: ' + word
            else:
                x = 'Not in word<br>Chance: ' + str(chance) + '<br>' + clue
        if not("_" in clue):
            x = 'You Win!'
    repeats += [s]
    return x

#user-end things
if 'input' in data:
    clue = guess(data.getvalue('input'))
if 'word' in data:
    z = data.getvalue('word')
    if z != '0':
        word = z
        clue = "_ " * len(word)
        hint = data.getvalue('hint')


#HTML stuff
HTML_HEADER = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>A Game of Hangman</title>
</head>

<body>

"""

HTML_FOOTER = """</body>

</html>"""

#more html stuff
html = HTML_HEADER
html += """<h1>A Game of Hangman</h1>""" + "\n"
html += "<p>\n" + instructions + 'hint: ' + hint + "\n</p>" + "\n"
html += clue + "\n" + "<br>"
html += """<form>
    <input type="text" name="input" value="">
    <input type="hidden" name="word" value='"""
html += str(word)
html += """'>
    <input type="hidden" name="hint" value='"""
html += str(hint)
html += """'>
    <input type="submit" name="submit" value="Guess!">
</form>"""
print(html)
