# 🤖 Joke Telling Program

This project is a simple Python program that tells a joke when prompted by the user. If the user asks for anything else, the program apologizes.

## 📝 How It Works

1. The program prompts the user with:
   ```
   What do you want? 
   ```
2. The user can enter a response.
3. If the response is **"joke"** (case insensitive), the program prints a joke.
4. If the response is anything else, the program responds with an apology.

## 📌 Example Output

### CLI Version
#### **User requests a joke**
```
What do you want? joke
Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'
```

#### **User asks for something else**
```
What do you want? advice
Sorry I only tell jokes.
```

## 🛠️ Code Breakdown
- Uses a constant `PROMPT` to display the user prompt.
- Defines `JOKE` and `SORRY` messages as constants.
- Takes user input, normalizes it (strips whitespace and converts it to lowercase).
- Checks if the input is "joke" and prints the appropriate response.

🎉 Have fun with this simple joke-telling bot!

