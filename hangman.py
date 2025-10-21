import random

with open('dictionary', 'r', encoding='UTF-8') as file:
    content = file.read()

word_list = content.split(',')

difficulty_settings = {
    "easy": 10,
    "medium": 6,
    "hard": 4
}
