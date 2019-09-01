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
        key_word = dict_keys[i]
        list_of_lines[i] += dict[key_word]
    for line in list_of_lines:
        print(line)


blanks = {
    "enter a noun: ": "",
    "enter a verb: ": "",
    "enter an adjective: ": "",
    "enter an adverb: ": "",
    "enter a preposition: ": ""
}

story_list = [
    "This is the first of my story ",
    "This is the second part of my story. Please ",
    "This is the third part of my story. Please "
]

list_of_keys = list(blanks.keys())

init_blanks(blanks, list_of_keys)
print("\n --------The Curious Tale of Kevin the Dog-------- \n")
print_full_story(story_list, blanks, list_of_keys)
