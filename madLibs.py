'''
Author: Zain Raza

madLibs.py:
Simulates a game of Mad Libs using Python.

Date Due: Tuesday, September 3 2019
'''


def init_blanks(dict, list):
    for key in list:
        dict[key] = input(key)


def print_full_story(list_of_lines, dict, dict_keys):
    key_word = ""
    for i in range(len(list_of_lines)):
        key_word = dict_keys[i]  # traverses the keys in the dictionary
        list_of_lines[i] += dict[key_word]  # dict value appends list element
    for line in list_of_lines:
        sentence = line + "."
        print(sentence)


blanks = {
    "enter a noun (a place): ": "",
    "enter a verb: ": "",
    "enter an adjective: ": "",
    "enter an adverb: ": "",
    "enter a preposition: ": ""
}

story_list = [
    "Kevin loved his home in the suburbs of ",
    "He spent everyday doing his favorite activity, ",
    "However, one day Kevin was abducted by someone who was very ",
    "Never to fear! The police took up the search for Kevin ",
    "Then Kevin was found, and joyous became the owner he was reunited "
]

list_of_keys = list(blanks.keys())

init_blanks(blanks, list_of_keys)
print("\n --------The Curious Tale of Kevin the Dog-------- \n")
print_full_story(story_list, blanks, list_of_keys)
