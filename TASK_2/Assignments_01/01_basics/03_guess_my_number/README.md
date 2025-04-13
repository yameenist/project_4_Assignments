# 🔢 Number Guessing Game

This project is a simple Python game where the user tries to guess a randomly generated number between 1 and 99.

## 📝 How It Works

1. The program generates a random number between **1 and 99**.
2. It asks the user to input a guess.
3. If the guess is too low, the program prints **"Your guess is too low"**.
4. If the guess is too high, the program prints **"Your guess is too high"**.
5. The user keeps guessing until they find the correct number.
6. Once the correct number is guessed, the program prints **"Congrats! The number was: [number]"**.

## 📌 Example Output

```
I am thinking of a number between 1 and 99...
Enter a guess: 50
Your guess is too high

Enter a new guess: 25
Your guess is too low

Enter a new guess: 37
Congrats! The number was: 37
```

## 🛠️ Code Breakdown
- Uses the `random.randint(1, 99)` function to generate a random number.
- Takes user input and converts it to an integer.
- Uses a `while` loop to keep prompting the user until they guess correctly.
- Prints hints to guide the user toward the correct number.

🎉 Great for practicing loops, conditionals, and user input handling in Python!

