# Blocker Journal

## 2026-08-21 09:00
### Problem
python : The term 'python' is not recognized when running `python --version` in Windows PowerShell.
### Hypothesis
Python was either not installed properly or the terminal didn't know where to find it.
### Investigation
Read the tutorial again, which suggested trying `python3 --version`. I realized my system PATH variables weren't set up.
### Finding
The Python installer requires a specific checkbox to link the program to the terminal.
### Fix
I ran the Python installer again. At the very bottom of the first screen, I checked the box that said "Add Python to PATH", finished the installation, and restarted PowerShell.
### Result
`python --version` successfully returned Python 3.13.14.
### Time spent
15 minutes

---

## 2026-08-21 09:25
### Problem
I got trapped in the nano editor. I pressed Esc and Ctrl + C, but it just typed weird characters on the screen instead of exiting.
### Hypothesis
Linux terminal text editors use different keyboard shortcuts than Windows.
### Investigation
Looked at the menu at the bottom of the terminal screen. It showed options like `^O Write Out` and `^X Exit`. I Googled "what does the up arrow mean in nano".
### Finding
The `^` symbol stands for the Ctrl key on Linux.
### Fix
Pressed `Ctrl + X` to exit. nano then asked if I wanted to save the modified buffer. I typed `Y` for Yes, and pressed Enter.
### Result
It successfully saved the file and returned me to the normal terminal prompt.
### Time spent
10 minutes

---

## 2026-08-21 09:45
### Problem
When running my script, it crashed with `NameError: name 'Python' is not defined`.
### Hypothesis
I accidentally typed the word "Python" directly into the code where it didn't belong.
### Investigation
Python pointed at the first line of the file. I Googled if I should type the name "Python" at the top of a nano file editor. I found out it should not be there.
### Finding
Python tries to execute every word in the file as code.
### Fix
Opened `nano exp1.py`, deleted the standalone word "Python", and saved.
### Result
The script ran perfectly.
### Time spent
10 minutes

---

## 2026-08-21 10:10
### Problem
Got a `SyntaxError: invalid syntax` on the line `"name:" "Mouse", "qty": 10`.
### Hypothesis
The formatting of my dictionary was incorrect.
### Investigation
I looked at the documentation and realized I forgot the curly braces `{}` around my dictionary items. When the loop tried to look up `item["name"]`, it failed because raw strings don't have "keys".
### Finding
Dictionaries require `{}` to make proper key-value pairs.
### Fix
Re-read the documentation on dictionaries and added the `{}` brackets around the data.
### Result
The loop successfully ran and printed the names.
### Time spent
15 minutes

---

## 2026-08-21 10:30
### Problem
Script crashed with `SyntaxError: expected 'except' or 'finally' block`.
### Hypothesis
I misspelled a Python keyword.
### Investigation
Because I am writing in nano, there is no spellcheck. I looked closely at my code and saw I typed `expect` instead of `except`.
### Finding
Python keywords must be spelled exactly right.
### Fix
Opened nano, changed `expect` to `except`, and saved.
### Result
Reran the script and it successfully handled the error.
### Time spent
5 minutes

---

## 2026-08-21 11:20
### Problem
Got a `XYZ999: command not found` error in Ubuntu.
### Hypothesis
I typed the SKU into the wrong place.
### Investigation
I typed the SKU directly into the terminal, and Ubuntu threw the error. I realized I was typing into the main Linux bash prompt instead of giving it to my Python program.
### Finding
The Python `input()` function only works while the Python script is actively running.
### Fix
I ran `python3 prototype.py` first, waited for the `Enter SKU:` prompt to appear on the screen, and then typed `XYZ999`.
### Result
It worked perfectly and returned "Out of stock".
### Time spent
10 minutes

---

## 2026-08-21 11:45
### Problem
My deliberately broken script crashed with `TypeError: unsupported operand type(s) for -: 'int' and 'str'`.
### Hypothesis
I cannot subtract a string from an integer.
### Investigation
I read the Traceback carefully. The terminal pointed directly to line 7. The error explicitly told me that `-` is unsupported between 'int' (integer) and 'str' (string).
### Finding
Python executes line-by-line and stops the exact millisecond a fatal error occurs. Data types matter immensely. Python does not know how to do math with words.
### Fix
This was a deliberate test to observe failure, so no code fix was applied. 
### Result
Learned that a system receiving "5" (string) from a web form will crash if it tries to do math with it unless converted to an `int` first.
### Time spent
15 minutes

---

## 2026-08-21 12:30
### Problem
When I ran `git commit -m "..."`, the terminal rejected it with `fatal: empty ident name not allowed` and asked "Please tell me who you are."
### Hypothesis
Git doesn't know my identity, so it refuses to save the commit history.
### Investigation
Read the error message provided by Git. It explicitly told me to run two `git config` commands.
### Finding
Git refuses to save a commit unless it knows exactly who is making the change, which requires an email and a name to attach to the log.
### Fix
I ran the two configuration commands in my terminal:
`git config --global user.email "myemail@example.com"`
`git config --global user.name "myname"`
### Result
I ran my `git commit` command again and it successfully saved my code. Verified with `git log --oneline`.
### Time spent
10 minutes
