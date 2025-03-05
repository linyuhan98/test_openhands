# Palindrome Finder

This repository contains a Python script to find all palindromic substrings in a given string.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/linyuhan98/test_openhands.git
   cd test_openhands
   ```

2. Run the script:
   ```bash
   python3 palindrome_finder.py
   ```

## Functionality

The script defines a function `find_palindromic_substrings` that takes a string `s` as input and returns a list of all unique palindromic substrings found in `s`.

### Example

For the input string `"ababa"`, the output will be:
```
Palindromic substrings: ['a', 'b', 'ababa', 'bab', 'aba']
```

## How It Works

The function uses the "expand around center" technique to find all palindromic substrings. It considers each character (and each pair of consecutive characters) as the center of a potential palindrome and expands outwards as long as the characters on both sides are equal.

Feel free to modify the `test_string` variable in the script to test with different input strings.