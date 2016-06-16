# https://www.codecademy.com/learn/python
#------------------------------------------------------------------------------
# CHAPTER 0
# My first program in Python
#------------------------------------------------------------------------------
monty = True
python = 1.234
monty_python = python ** 2


#------------------------------------------------------------------------------
# CHAPTER 1
# Assign the variable total on line 8!
#------------------------------------------------------------------------------
meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%0.2f" % total)


#------------------------------------------------------------------------------
# CHAPTER 2
# Srings
#------------------------------------------------------------------------------
pi = 3.14
print str(pi)

ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()

#--------------------------------------
print "The value of pi is around " + str(3.14)

#--------------------------------------
string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

#--------------------------------------
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)


#------------------------------------------------------------------------------
# CHAPTER 3
# Date and Time
#------------------------------------------------------------------------------
from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)


#------------------------------------------------------------------------------
# CHAPTER 4
# Conditionals and Control Flow
#------------------------------------------------------------------------------
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

#--------------------------------------
# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = 1 == 1 and 2 == 2

# Make me false!
bool_three = 1 == 2 or 3 == 4

# Make me true!
bool_four = not 1 == 2 or 3 == 4

# Make me true!
bool_five = not 1 == 2 or 3 == 4

#--------------------------------------
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)


#------------------------------------------------------------------------------
# CHAPTER 5
# PygLatin - move first word to last and add 'ay' after it
#------------------------------------------------------------------------------
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:]
else:
    print 'empty'


#------------------------------------------------------------------------------
# CHAPTER 6
# Functions - Importing Modules, type()
#------------------------------------------------------------------------------
def cube(number):
    return number ** 3
    
def by_three(number):
    if (number % 3) == 0:
        return cube(number)
    else:
        return False

#--------------------------------------
def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

#--------------------------------------
from math import *
print sqrt(13689)

#--------------------------------------
def distance_from_zero(arg):
    if type(arg) == int:
        return abs(arg)
    elif type(arg) == float:
        return abs(arg)
    else:
        return "Nope"
        

#------------------------------------------------------------------------------
# CHAPTER 7
# Plan Your Trip - Functions and Calculation
#------------------------------------------------------------------------------
def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if (city == "Charlotte"):
        return 183
    elif (city == "Tampa"):
        return 220
    elif (city == "Pittsburgh"):
        return 222
    elif (city == "Los Angeles"):
        return 475
        
def rental_car_cost(days):
    if (days >= 7):
        return (days * 40) - 50
    elif (days >= 3):
        return (days * 40) - 20
    else:
        return days * 40
        
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
      
print trip_cost("Los Angeles", 5, 600)


#------------------------------------------------------------------------------
# CHAPTER 8
# Lists
#------------------------------------------------------------------------------
numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
print numbers[1] + numbers[3]

#--------------------------------------
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
zoo_animals[3] = "lion"

#--------------------------------------
suitcase = [] 
suitcase.append("sunglasses")

suitcase.append("shirt")
suitcase.append("shoe")
suitcase.append("vest")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

#--------------------------------------
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]               # Third and fourth items (index two and three)
last   = suitcase[4:6]               # The last two items (index four and five)

#--------------------------------------
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]              # The fourth through sixth characters
frog = animals[6:]  

#--------------------------------------
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]

duck_index = animals.index("duck")
animals.insert(duck_index, "cobra")

print animals # Observe what prints after the insert operation

#--------------------------------------
start_list = [5, 3, 1, 2, 4]
square_list = []

for item in start_list:
    square_list.append(item ** 2)

square_list.sort()
print square_list


#------------------------------------------------------------------------------
# CHAPTER 9
# DICTIONARIES
#------------------------------------------------------------------------------
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

print residents["Sloth"]

print residents["Burmese Python"]

#--------------------------------------
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

menu["rasam"] = 5
menu["rice"] = 10.2
menu["bajji"] = 60


print "There are " + str(len(menu)) + " items on the menu."
print menu

#--------------------------------------
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'bla bla'

#--------------------------------------
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = 50 + inventory['gold']

#------------------------------------------------------------------------------
# CHAPTER 10
# A Day at SuperMarket
#------------------------------------------------------------------------------
prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

total = 0
for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    
    prodPrice = prices[key] * stock[key]
    print "total: %s" % prodPrice
    total = total + prodPrice

print total

#--------------------------------------
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] = stock[item] - 1
    return total

#------------------------------------------------------------------------------
# CHAPTER 11
# Student Becomes The Teacher
#------------------------------------------------------------------------------
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

def average(numbers):
    total = float(sum(numbers))
    return total / len(numbers)
    
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    
    return ((0.1 * homework) + (0.3 * quizzes) + (0.6 * tests))
    
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
        
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
        
    return average(results)

students = [lloyd, alice, tyler]
class_average = get_class_average(students)
print class_average
print get_letter_grade(class_average)


#------------------------------------------------------------------------------
# CHAPTER 12
# Lists and Functions
#------------------------------------------------------------------------------
n = [1, 3, 5]

# Append the number 4 here
n.append(4)

# Remove the first item in the list here
n.pop(0)
n.remove(3)
del(n[2])

print n

#--------------------------------------
n = [3, 5, 7]

def print_list(x):
    for i in x:
        print i

    for i in range(0, len(x)):
        print x[i]
        
def double_list(x):
    for i in range(0, len(x)):
        x[i] *= 2
    return x
        
print double_list(n)

print_list(n) 

#--------------------------------------
range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(3)) # Add your range between the parentheses!

#--------------------------------------
n = [3, 5, 7]

def total(numbers):
    result = 0
    
    for n in numbers:
        result += n
    return result

n = ["Michael", "Lieberman"]
# Add your function here

def join_strings(words):
    result = ""
    
    for i in range(0, len(words)):
        result += words[i]
    
    return result
    
print join_strings(n)

#--------------------------------------
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x, y):
    return x + y

print join_lists(m, n)

#--------------------------------------
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
    results = []
    for l in lists:
        results = results + l

    for numbers in lists:
        for n in numbers:
            results.append(n)
    return results

print flatten(n)

#--------------------------------------

#--------------------------------------

#--------------------------------------

#--------------------------------------

#--------------------------------------

#--------------------------------------



