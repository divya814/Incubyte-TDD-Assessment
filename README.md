# Incubyte-TDD-Assessment 
### String Calculator
This is a simple String Calculator implemented in Python, designed to perform addition of numbers represented in a specific string format. The project follows Test Driven Development (TDD) principles, ensuring that each feature is implemented alongside its corresponding tests.

### Table of Contents
1. Features
2. Installation
3. Usage
4. Test Cases
5. Scenarios

### Features
1. Addition of Numbers: Supports addition of numbers provided as a comma-separated string.
2. Support for New Lines: Allows for numbers to be separated by new lines in addition to commas.
3. Custom Delimiters: Users can specify custom delimiters using a specific format at the start of the string.
4. Negative Number Handling: Throws an exception for negative numbers, listing all of them in the error message.
5. Ignore Large Numbers: Numbers greater than 1000 are ignored during the summation.
6. Support for Multi-Character Delimiters: Allows for delimiters of any length and multiple delimiters in a single string.

### Installation
To use this String Calculator, ensure you have Python installed on your machine. Clone the repository and navigate to the project directory. To run the test case file, use command - python -m unittest test_string_calculator.py

### Test Cases
This project follows TDD, and the following tests are included in the test_string_calculator.py file:

1. Empty String: add("") returns 0.
2. Single Number: add("1") returns 1.
3. Two Numbers: add("1,5") returns 6.
5. Multiple Numbers: Handles addition of any number of numbers.
6. New Line Support: Handles new lines between numbers.
7. Custom Delimiter Support: Supports custom delimiters specified in the input string.
8. Negative Number Exception: Raises an exception for negative numbers.
9. Ignoring Large Numbers: Ignores numbers greater than 1000 during summation.
10. Multi-Character and Multiple Delimiter Support: Handles custom delimiters of any length and multiple delimiters.

### Scenarios
Here are some examples demonstrating the various functionalities of the String Calculator:

Empty Input:

Input: ""
Output: 0
Single Number:

Input: "1"
Output: 1
Two Numbers:

Input: "1,5"
Output: 6
New Line Support:

Input: "1\n2,3"
Output: 6
Custom Delimiter:

Input: "//;\n1;2"
Output: 3
Multiple Delimiters:

Input: "//[*][%]\n1*2%3"
Output: 6
Negative Number Exception:

Input: "1,-2,3" raises ValueError: negative numbers not allowed -2
Ignoring Large Numbers:

Input: "2,1001"
Output: 2
Multi-Character Delimiters:

Input: "//[***]\n1***2***3"
Output: 6