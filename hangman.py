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
    word_display = ['_' for letters in word]
    guessed_letters = []
    correct_letters = []

    for letters in word:
        correct_letters.append(letters)
    print("Choose the difficulty: easy / medium / hard")

    while True:
        difficulty = input("Choose difficulty: ").lower()
        if difficulty in difficulty_settings.keys():
            break
        print("\nInvalid choice, try again")
    lives = difficulty_settings[difficulty]
    print("\n!! The game starts 🎮!!")
    variable = False
    while lives > 0 and variable == False:
        for i in word_display:
            print(i, end=" ")
        print(f"\nYou have {lives} lives\n")
        human_choice = input("Choose a letter : \n").lower()
        while len(human_choice) != 1:
            print("Too much characters, try again \n")
            human_choice = input("Choose a letter : \n").lower()

        while "a" > human_choice or "z" < human_choice:
            print("\nThe character you entered is invalid, try again")
            human_choice = input("\nChoose a letter : ").lower()

        if human_choice in correct_letters:
            guessed_letters.append(human_choice)
            for index in range(len(word)):
                if word[index] == human_choice:
                    word_display[index] = human_choice
                    variable = True
                    for i in range(len(word_display)):
                        if '_' in word_display[i]:
                            variable = False
                    if variable == True:
                        print("You won!!🎉🎉✨")
                        break

        else:
            lives = lives - 1
            guessed_letters.append(human_choice)
        print(f" Letters guessed {guessed_letters}")

    if variable == False:
        print("You lost😞😞")
        choice = input("Do you want to play again😊?? Y/N ").lower()
        if choice == 'n':
            print("💔")
        elif choice == 'y':
            play_hangman()


play_hangman()
