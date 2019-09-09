'''
Author: Zain Raza

madLibs.py:
Simulates a game of Mad Libs using Python.

Date Due: Tuesday, September 3 2019
'''
import pyfiglet  # module used for ASCII art

# dict connects user prompts for words, to the inputs by user
blanks = {
    "Enter a noun: ": "",
    "Enter a verb: ": "",
    "Enter an adjective: ": "",
    "Enter an adverb: ": "",
    "Enter a preposition: ": ""
}

# list traversal prints each line of the story
story_list = [
    "Kevin loved his home in the suburbs of ",
    "He spent everyday doing his favorite activity, ",
    "However, one day Kevin was abducted by someone who was very ",
    "Never to fear! The police took up the search for Kevin ",
    "Then Kevin was found, and joyous became the owner he was reunited "
]

list_of_keys = list(blanks.keys())  # creates a list to be used for iterating through dict using for loop


# travserses dict keys to prompt user, keys initialiazed to input
def init_blanks(diction, list):
    for key in list:
        diction[key] = input(key)
        # in case user enters invalid input
        while not diction[key].isalpha():
            print("Invalid input.")
            diction[key] = input("Please try again: ")


# displays the lines of the story filled in with user input
def print_full_story(list_of_lines, diction, dict_keys):
    key_word = ""
    for i in range(len(list_of_lines)):
        key_word = dict_keys[i]  # traverses the keys in the dictionary
        green_text = "\033[1;32;40m{}\x1b[0m".format(diction[key_word])
        list_of_lines[i] += green_text  # dict value appends list element
    for line in list_of_lines:
        sentence = line + "."  # finishes sentence with punctuation
        print(sentence)


init_blanks(blanks, list_of_keys)  # takes in user input
title = pyfiglet.figlet_format("The Search for Kevin the Dog", font="slant")  # ASCII title
print(title)
print_full_story(story_list, blanks, list_of_keys)  # user is shown their story
