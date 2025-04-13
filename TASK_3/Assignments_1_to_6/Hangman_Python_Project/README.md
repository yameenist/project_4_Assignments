# 🎮 Hangman Game

This project is a classic Hangman game where the player attempts to guess a secret word one letter at a time before running out of lives.

## 🕹️ How It Works

1. A random word is selected from a predefined list.
2. The player guesses one letter at a time.
3. If the guessed letter is in the word, it is revealed in its correct position(s).
4. If the guessed letter is not in the word, the player loses a life.
5. The player has **6 lives** to guess the word before the game ends.
6. If the player successfully guesses all the letters, they win!
7. If the player runs out of lives, they lose, and the correct word is revealed.
8. The player can choose to play again or exit.

## 📌 Example Output

```
🎮 Hangman Game
===============
Guess the word one letter at a time. You have 6 lives!

Word: _ _ _ _ _ _
Lives left: 6
Guess a letter: p
✅ The letter 'p' is in the word!

Word: p _ _ _ _ _
Lives left: 6
Guess a letter: x
❌ The letter 'x' is not in the word.

Word: p y t h o n
🎉 Congratulations! You guessed the word: python
```

## 🛠️ Code Breakdown

- **Random Word Selection:** A word is randomly chosen from a predefined list.
- **User Input Handling:** Ensures the user enters a valid single letter.
- **Game Logic:** Updates the word display and manages lives based on correct or incorrect guesses.
- **Replay Option:** The user can choose to play again or exit.

🎉 A great project to practice string manipulation, loops, and conditionals in Python!

