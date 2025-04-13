# 🎮 Guess the Number Game

This project is a fun and interactive number guessing game where the player tries to guess a randomly generated secret number between 1 and 10.

## 🕹️ How It Works

1. The program generates a secret number between 1 and 10.
2. The user inputs their guess.
3. The program provides feedback:
   - **If the guess is too high**, it prompts the user to guess a lower number.
   - **If the guess is too low**, it prompts the user to guess a higher number.
   - **If the guess is correct**, the game congratulates the player and displays the number of attempts taken.
4. The user is shown all hints provided during the game.
5. The user can choose to play again or exit the game.

## 📌 Example Output

```
🎮 Guess the Number Game
========================
Try to guess the secret number between 1 and 10!

Enter your guess (1-10): 5
The secret number is higher.

Enter your guess (1-10): 7
The secret number is lower.

Enter your guess (1-10): 6
🎉 Congratulations! You guessed the number **6** in 3 attempts!

💡 All Hints:
💡 Hint: The secret number is higher.
💡 Hint: The secret number is lower.

Do you want to play again? (yes/no): no
Thanks for playing! Goodbye! 🎮
```

## 🛠️ Code Breakdown

- **Random Number Generation:** The program selects a random number between 1 and 10.
- **User Input Handling:** The program ensures the user enters a valid number within the correct range.
- **Feedback System:** The game provides hints to help the user guess correctly.
- **Loop Until Correct Guess:** The game continues until the user correctly guesses the secret number.
- **Hint Tracking:** All hints are displayed at the end of the game.
- **Replay Option:** The user can choose to play again or exit.

🎉 A great beginner-friendly project to practice loops, user input handling, and logical thinking in Python!

