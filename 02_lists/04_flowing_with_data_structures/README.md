# Mutable List Modification Example

## Description
This program demonstrates the concept of mutability in Python. It showcases how changes made to mutable data types, such as lists, persist even when modifications are performed inside a function without returning the modified object.

## Problem Statement
In Python, immutable data types (e.g., numbers, strings) do not retain changes made within functions unless explicitly returned. However, mutable data types (e.g., lists, dictionaries) store changes even if the function does not return them.

This program implements a function `add_three_copies(my_list, data)`, which adds three copies of the provided data to a given list without returning anything.

## Features
- Demonstrates list mutability.
- Uses a helper function to modify the list.
- Compares the list before and after function execution.

## Installation & Usage
1. Ensure you have Python installed (Python 3 recommended).
2. Save the script as `app.py`.
3. Run the script:
   ```sh
   python app.py
   ```
4. Enter a message when prompted.

## Example Run
```
Enter a message to copy: Hello world!
List before: []
List after: ['Hello world!', 'Hello world!', 'Hello world!']
```

## Notes
- Lists in Python are mutable, meaning they retain modifications even if they are not returned from a function.
- Be mindful of modifying lists inside functions as changes persist.
- Different programming languages have different mutability rules.

Enjoy exploring the concept of mutability in Python! 🚀

