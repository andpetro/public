
from sys import exit

def fuck_room():
  print("You will be fucked")
  print("Choose the method")

  choice = input("> ")

  print(f"You are being fucked with {choice}")


def gold_room():
  print("This room is full of gold. How much do you take?")

  choice = input("> ")
  if "0" in choice or "1" in choice:
    how_much = int(choice)
  else:
    dead("Man learn to type a number")
  
  if how_much < 50:
    print("Nice you're not greedy. you win!")
    exit(0)
  else:
    dead("You greedy bastard!")


def bear_room():
  print("There is a bear here")
  print("The bear has a bunch of honey")
  print("The fat bear is in front of other door")
  print("Gow are you going to move the bear?")
  bear_moved = False

  while True:
    choice = input("> ")

    if choice == "take honey":
      dead("The bear looks at you then slaps your face off.")
    elif choice == "taunt bear" and not bear_moved:
      print("The bear has moved from the door")
      print("You can go thought it now")
      bear_moved = True
    elif choice == "taunt bear" and bear_moved:
      dead("The bear gets pissed off and chews your leg off.")
    elif choice == "open door" and bear_moved:
      gold_room()
    else:
      print("I got no idea what that means")


def cthulhu_room():
  print("Here you see the great evil Cthulhu.")
  print("He, it, whatever stares at you and you go insane.")
  print("Do you flee for your life or eat your head?")

  choice = input("> ")

  if "flee" in choice:
    start()
  elif "head" in choice:
    dead("Well that was tasty")
  else:
    cthulhu_room()

def dead(why):
  print(why, "Good job!")
  exit(0)

def start():
  print("You are in a dark room.")
  print("There is a door to your right and left.")
  print("You can also go up or down")
  print("Which one do you take?")

  choice = input("> ")

  if choice == "left":
    bear_room()
  elif choice == "right":
    cthulhu_room()
  elif choice == "up":
    fuck_room()
#  elif choice == "down":
#    nt_room()
  else:
    dead("You stumble around the room until you starve.")

start()






  

 
 
# i = 0
# m = 99
# n = 5
# numbers =[]

# for i in range (0, m, n):
#   print(f"At the top i is {i}")
#   numbers.append(i)

#   #i = i + 1
#   print("Numbers now: ", numbers)

#   print(f"At the bottom i is {i}")

# print("The numbers: ")

# for num in numbers:
#   print(num)










# the_count = [1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for number in the_count:
#   print (f"This is count: {number}")

# for fruit in fruits:
#   print(f"A fruit of type: {fruit}")

# for i in change:
#   print(f"I got {i}")

# elements = []

# for i in range(0, 6):
#   print(f"Adding {i} to the list")
#   elements.append(i)

# for i in elements:
#   print(f"Element was: {i}")


# test = [*range(0, 6)]
# print(test)
# print(elements)




# print("""You enter a dark room with two doors.
# Do you go through door #1 or door #2?""")

# door = input("> ")

# if door == "1":
#   print("There's a giant bear here eating a chees cake")
#   print("What do you do?")
#   print("1. Take the cake.")
#   print("2. Scream at the bear.")

#   bear = input("> ")

#   if bear == "1":
#     print("The bear eats your face off. Good job!")
#   elif bear == "2":
#     print("The bear eats your legs off. Good job!")
#   else:
#     print(f"Well, doing {bear} is probably better.")
#     print("Bear runs away.")

# elif door == "2":
#   print("You stare into the endless abyss at Cthulhu's retina.")
#   print("1. Blueberries.")
#   print("2. Yellow jacket clothespins.")
#   print("3. Understanding revlovers yelling melodies.")

#   insanity = input("> ")

#   if insanity == "1" or insanity == "2":
#     print("Your body survives powered by a mind of jello")
#     print("Good job!")
#   else:
#     print("The insanity rots your eyes into a pool of muck.")
#     print("Good job!")

# else:
#   print("You stamble around and fall on a knife and die. Good job!")




# from sys import argv

# script, people, cars, trucks = argv

# # people = 30
# # cars = 40
# # trucks = 15

# if cars > people:
#   print("We should take the cars.")
# elif cars < people:
#   print("We should not take the cars.")
# else:
#   print("We can't decide.")

# if trucks > cars:
#   print("That's too many trucks.")
# elif trucks < cars:
#   print("Maybe we could take the trucks.")
# else:
#   print("We still can't decide.")

# if people < trucks:
#   print("Alright, let's just take the trucks.")
# else:
#   print("Fine, let's stay home then.")





# people = 20
# cats = 30
# dogs = 15

# if people < cats:
#   print("Too many cats! The world is doomed!")

# if people > cats:
#   print("Not many cats! The worlds is saved!") 

# if people < dogs:
#   print("The world is drooled on!")

# if people > dogs:
#   print("The world is dry")

# dogs += 5

# if people >= dogs:
#   print("People are greater than dogs or equal to dogs")

# if people <= dogs:
#   print("People are less than dogs or equal to dogs")

# if people == dogs:
#   print("People are dogs")





# import pandas
# import json

# excel = pandas.read_excel('DSL_Profile.xlsx', sheet_name='ADSL_AxJ_Profile_für_BNG')

# json_str = excel.to_json()

# y = json.loads(json_str)

# print(y)

# """XLS -> json converter
# first:
#   $ pip install xlrd
# then:
#   $ cat in.xls
# date, temp, pressure
# Jan 1, 73, 455
# Jan 3, 72, 344
# Jan 7, 52, 100
# convert:
#   $ python xls_to_json.py in.xls Sheet1 out.json
# finally:
#   $ cat out.json
# {
#   'data': [
#     {'date': 'Jan 1', 'temp': 73, 'pressure': 455},
#     {'date': 'Jan 3', 'temp': 72, 'pressure': 344},
#     {'date': 'Jan 7', 'temp': 52, 'pressure': 100},
#   ]
# }
# """
# import json
# import sys

# import xlrd


# workbook = xlrd.open_workbook('./DSL_Profile.xlsx')
# worksheet = workbook.sheet_by_name('ADSL_AxJ_Profile_für_BNG')

# data = []
# keys = [v.value for v in worksheet.row(0)]
# for row_number in range(worksheet.nrows):
#     if row_number == 0:
#         continue
#     row_data = {}
#     for col_number, cell in enumerate(worksheet.row(row_number)):
#         row_data[keys[col_number]] = cell.value
#     data.append(row_data)

# with open('sample.json', 'w') as json_file:
#     json_file.write(json.dumps({'data': data}))








# #with open('sample.json', 'w') as json_file:
# #    json.dump(json_str, json_file)


# print("Let's practice everyhting")
# print('You\'d need to know \'bout escapes with \\ that do:')
# print('\n newLines and \t tabs.')

# poem = """
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explanation
# \n\t\twhere there is none
# """

# print('-----------------------')
# print(poem)
# print('-----------------------')

# five = 10- 2 + 3 -6
# print(f"This should be five: {five}")

# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100
#     return jelly_beans, jars, crates

# start_point = 10000

# beans, jars, crates = secret_formula(start_point)

# print("with a starting point of: {}".format(start_point))

# print(f"We have {beans} beans, {jars} jars, {crates} crates.")

# start_point = start_point / 10

# print("We can also do this way:")

# formula = secret_formula(start_point)

# print("We'd have {} beans, {} jars, and {} crates".format(*formula))


# def break_words(stuff):
#     """ this function will breal up words for us"""
#     words = stuff.split(' ')
#     return words


# def sort_words(words):
#     """ Sorts the words. """
#     return sorted(words)


# def print_first_word(words):
#     """ Prints the first word after popping it off. """
#     word = words.pop(0)
#     print(word)


# def print_last_word(words):
#     """ Prints the last word after popping it off. """
#     word = words.pop(-1)
#     print(word)


# def sort_sentence(sentence):
#     """ Takes in a full sentence and returns the sorted words"""
#     words = break_words(sentence)
#     return sort_words(words)


# def print_first_and_last(sentence):
#     """Prints the first and last words of the sentence."""
#     words = break_words(sentence)
#     print_first_word(words)
#     print_last_word(words)


# def print_first_and_last_sorted(sentence):
#     """Sorts the words then prints the first and last one."""
#     words = sort_sentence(sentence)
#     print_first_word(words)
#     print_last_word(words)



