import random

with open('dictionary', 'r', encoding='UTF-8') as file:
    content = file.read()

word_list = content.split(',')

difficulty_settings = {
    "easy": 10,
    "medium": 6,
    "hard": 4
}

def play_hangman():
    word = random.choice(word_list)
    print=("Choose the difficulty: easy / medium / hard")
    while True:
        difficulty = input("difficulty: ").lower
        if difficulty in difficulty_settings:
            break
        print("\nInvalid choice,try again")
    lives = difficulty_settings[difficulty]
    print("\nThe game starts 🎮!!") 
    while lives > 0 : 

