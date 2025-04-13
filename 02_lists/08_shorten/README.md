# List Shortener Project

## Description
This project allows users to enter a list of values and shortens it to a maximum length of 3. Users interact with the program via a command-line interface (CLI).

## Features
- Collects user input as a list.
- Removes extra elements beyond the maximum allowed length.
- Displays the removed and final lists.

## Installation & Usage

### CLI Version
1. Ensure Python is installed.
2. Save the script as `app.py`.
3. Run the script:
   ```sh
   python app.py
   ```
4. Enter values one by one, and press Enter on an empty input to display the shortened list.

## Example Output (CLI)
```
Enter an element: apple
Enter an element: banana
Enter an element: cherry
Enter an element: date
Removed: date
Here's the final list: ['apple', 'banana', 'cherry']
```

## Notes
- The CLI version runs in the terminal and collects input interactively.
- The default maximum list length is set to 3, but this can be modified in the code.

Enjoy coding! 🚀

