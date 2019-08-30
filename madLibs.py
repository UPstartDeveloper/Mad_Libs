'''
def replace_blanks(blank_words, user_responses):
    for i in range(len(blank_words)):
        blank_words[i] += user_responses[i]


def print_full_story(story, responses):
    for i in range(len(story)):
        print(story[i] + responses[i])

replace_blanks(story_list, blanks)
print_full_story(story_list, blanks)
'''


def init_blanks(dict):
    list_of_keys = list(dict.keys())
    for key in list_of_keys:
        dict[key] = input(key)


def print_full_story(story):
    for line in story:
        print(line)


blanks = {
    "enter a noun: ": "",
    "enter a verb: ": "",
    "enter an adjective: ": "",
    "enter an adverb: ": "",
    "enter a preposition: ": ""
}

story_list = [
    "This is the first of my story",
    "This is the second part of my story. Please",
    "This is the third part of my story. Please"
]

init_blanks(blanks)
print_full_story(story_list)
