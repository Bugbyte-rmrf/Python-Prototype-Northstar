# Python Prototype Northstar

## Purpose
This prototype exists as a reconnaissance mission to validate my local development environment (Ubuntu/Git) and learn fundamental Python syntax before attempting to build the actual Northstar Day 3 service.

## Objective
The objective was to learn how to write, execute, and debug basic Python scripts in a Linux terminal, specifically focusing on dictionaries, if-statements, user input, and error handling.

## What the prototype does
It is a tiny, command-line inventory checker. It asks the user for a product SKU, looks that SKU up against a hardcoded data dictionary, and returns whether the item is in stock, out of stock, or doesn't exist.

## How to run it
Run this command in the Ubuntu terminal from the project folder:
`python3 prototype.py`

## Example
**Input:**
Enter SKU: ABC123

**Result:**
Inventory:
ABC123 -> 7 units
Result:
In stock

## What I learned
1. **Indentation is syntax:** Unlike other languages, Python uses whitespace (spaces) to define what code belongs inside a loop or function.
2. **Data types are strict:** Python will immediately crash if you try to do math between a String and an Integer. You must convert types (e.g., using `int()`).
3. **Dictionary safety:** Looking up a key that doesn't exist in a dictionary causes a fatal `KeyError`. You must check `if key in dictionary:` first.
4. **Environment isolation:** Typing terminal commands (like `cd`) inside the Python shell causes errors. You must know whether you are talking to Linux or talking to Python.

## Known limitations
This is not a production system. It does not have a database, it does not connect to the internet, there is no web API, and the inventory data is completely hardcoded into the script.
