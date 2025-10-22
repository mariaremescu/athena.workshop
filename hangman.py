import random

with open('dictionary.txt', 'r', encoding='UTF-8') as file:
    content = file.read()

word_list = content.split(',')

difficulty_settings = {
    'easy': 10,
    'medium': 6,
    'hard': 4
}


def play_hangman():

    word = random.choice(word_list)
    print(word)
    word_display = ['_' for letters in word]
    guessed_letters = []
    correct_letters = []
    for letters in word:
        correct_letters.append(letters)
    print("Choose the difficulty: ")

    while True:
       
        difficulty = input("difficulty: ").lower()
        print(difficulty)
        if difficulty in difficulty_settings.keys():
            break
        print("Invalid choice, try again")

    
    
    lives = difficulty_settings[difficulty]
    print("\n The game starts 🎮!!")

    while lives > 0:
        for i in word_display:
            print(i,end=" ")
        print(f"You have {lives}/n")
        human_choice = input("Choose a letter : \n").lower()
        
        while 'a' > human_choice and human_choice > 'z':
            print("/nThe character you entered is invalid, try again")
            human_choice = input("/nChoose a letter : ").lower()

        if human_choice in correct_letters:
            
            guessed_letters.append(human_choice)

            for index in range(len(word)):
                if word[index]==human_choice:
                    word_display[index] = human_choice


        else:
            lives = lives - 1
            guessed_letters.append(human_choice)
        print(f" Letters guessed {guessed_letters}")

play_hangman()           
