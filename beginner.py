print("hello world")
print("       /|")
print("      / |")
print("     /  |")
print("    /___|")
name = "Naa"
sweet = "Kitkat"
print("Hello")
print("my name is " + name + ",")
print("I like " + sweet + ".")
print("Giraffe\n academy")

phrase = "Giraffe Academy"
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("f"))
print(phrase.replace("Giraffe", "Elephant"))

from math import *
my_num = 3
print(str(my_num) + " is my fav number")
my_num = -5
print(abs(my_num))
print(pow(4, 6))
print(min(2, 6))
print(max(2, 7))
print(round(3.7))
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))

# Getting input from user
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + " You are " + age)

# Calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)

# Lists
lucky_numbers = [4, 8, 7, 5, 6]
friends = ["kevin", "Karen", "Jim"]
print(friends[-1])
print(friends[0])
print(friends[0:1])
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(2, "Kelly")
friends.remove("Jim")
friends.pop()
lucky_numbers.sort()
lucky_numbers.reverse()
friends2 = friends.copy()
print(friends2)
print(lucky_numbers)
print(friends)
print(friends.index("kevin"))
print(friends.count("Kelly"))

# Tuples
coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates[0])

# Functions
def sayhi():
    print("Hello User")

sayhi()

def say_hi(name):
    print("Hello" + name)

say_hi(" Mike")
say_hi(" Steve")

#Return Statement
def cube(num):
    return num*num*num

result = cube(4)
print(cube(3))
print(result)

#If statements
is_male = True
is_tall = True

if is_male:
    print("You are a male")
else:
    print("You are not male")    

#If statements and comparisons
def max_num(num1, num2, num3):
    if num1>= num2 and num1>= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(3, 4, 5))  

#Advanced calculator
num1 = float(input("Enter first number:"))
operator = float(input("Enter operator:"))
num2 = float(input("Enter second number:"))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2) 
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    ("Invalid Operator") 

#Dictionaries
          