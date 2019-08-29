def replace_blanks(blank_words, user_responses):
    for i in range(len(blank_words)):
        blank_words[i] += user_responses[i]


def print_full_story(story, responses):
    for i in range(len(story)):
        print(story[i] + responses[i])


blanks = {
    "(insert noun)": "bottle",
    "(insert adjective)": "smelly",
    "(insert verb)": "run"
}

story_list = [
    "This is the first part of my story. Please",
    "This is the second part of my story. Please",
    "This is the third part of my story. Please"
]

for line in story_list:
    print(line)

replace_blanks(story_list, blanks)
print_full_story(story_list, blanks)
