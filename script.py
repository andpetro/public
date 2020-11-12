






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



