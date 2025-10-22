# athena.workshop
### 🧩 What the Project Is
**Hangman** is a classic word-guessing game built in **Python**.  
The player tries to guess the hidden word letter by letter before running out of lives.  
It runs entirely in the terminal and includes difficulty levels (easy, medium, hard), life tracking, and feedback for guessed letters.

---

## 💡 Why I Made This Project
I wanted to practice Python basics like loops, conditionals, lists, and user input, while also making something fun and interactive.  
Creating a simple game felt like the perfect mix between learning programming logic and building something people can actually play!

---

## ⚙️ How I Made It
- I used **Python 3** for all the logic.
- The list of possible words is stored in a text file called `dictionary.txt`, where each word is separated by a comma.
- The game randomly chooses one word each round.
- The player chooses a difficulty level (which changes the number of lives).
- The program keeps track of:
  - Correct guesses
  - Wrong guesses
  - Remaining lives
- The game ends when you either guess all the letters or run out of lives.
- If you lose, you can choose to play again.

## 🧠 What I Struggled With and What I Learned
At first, I had trouble with:
- Making sure invalid inputs (like numbers or multiple letters) didn’t break the game.
- Figuring out how to check if the player had won without using confusing nested loops.
- Organizing my code so it was readable and easy to restart the game.

Through this project, I learned:
- How to validate user input in Python.
- How to use lists and loops to manage game state.
- How to structure code inside functions to make it cleaner.
- The importance of user experience, even in a small terminal project.

---

## ▶️ How to Run It
### Requirements
- Python 3.8+  
- `dictionary.txt` file in the same folder as `hangman.py`

### Steps
1. Clone this repository
  
   git clone https://github.com/mariaremescu/athena.workshop
2.Run the game


3.Choose your difficulty (easy / medium / hard) and start guessing letters!

📝 Example Gameplay
Choose the difficulty: easy / medium / hard
Choose difficulty: easy

!! The game starts 🎮 !!

_ _ _ _ _
You have 10 lives
Choose a letter: e
Letters guessed: e

 Future Improvements:
    Add ASCII art for each hangman stage.
    Allow users to add their own words.
    Save scores and track performance over time.

💬 Author

Created by [Your Name]