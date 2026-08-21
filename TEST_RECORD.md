# Manual Test Record
**Target:** `day2_prototype.py`

### TEST 1: Existing SKU with quantity > 0
* **Action:** Ran the program and entered `SKU001`.
* **Expected:** In stock
* **Result:** Pass. The program correctly retrieved 15 units and printed "In stock".

### TEST 2: Existing SKU with quantity = 0
* **Action:** Entered `SKU002`.
* **Expected:** Out of stock
* **Result:** Pass. The program correctly retrieved 0 units and printed "Out of stock".

### TEST 3: Unknown SKU
* **Action:** Entered `SKU009` (not in dictionary).
* **Expected:** Unknown product
* **Result:** Pass. The program safely caught the missing key and printed "Unknown product" without crashing.

### TEST 4: Invalid input (Blank)
* **Action:** Pressed Enter without typing anything (blank input).
* **Expected:** Controlled response
* **Result:** Pass. The program printed "Error: SKU cannot be blank. Please try again." and restarted the loop.

### TEST 5: Invalid input (System Interrupt)
* **Action:** Pressed `Ctrl + C` while the program was waiting for input.
* **Expected:** Controlled response instead of a Python Traceback error.
* **Result:** Pass. The `except KeyboardInterrupt` block triggered, printed "Force quit detected. Exiting safely...", and gracefully closed the program.
