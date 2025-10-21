import random

with open('dictionary', 'r', encoding='UTF-8') as file:
    content = file.read()

word_list = content.split(',')

difficulty_settings = {
    "easy": 10,
    "medium": 6,
    "hard": 4
}
# make a list for guessed letters
def letters_display(word,human_choice):
    verification = True
    index = word.find(human_choice)
    word[index] = human_choice
def play_hangman():

    word = random.choice(word_list)
    word_display = ['_' for letters in word]

    for letters in word:  
        correct_letters = letters
    print=("Choose the difficulty: easy / medium / hard")

    while True:
        difficulty = input("difficulty: ").lower
        if difficulty in difficulty_settings:
            break
        print("\nInvalid choice, try again")
    
    print(word_display)
    lives = difficulty_settings[difficulty]
    print("\nThe game starts 🎮!!") 

    while lives > 0 : 
        human_choice = input("Choose a letter : ").lower
        while 'a'> human_choice >'z':
            print("the character you entered is invalid, try again")
            human_choice = input("Choose a letter : ").lower
        if human_choice in correct_letters:
            letters_display(word, human_choice)


            

