# Defining a reusable function
def add_stock(amount):
	try:
		# We try to convert the input to a number
		new_qty = int(amount)
		print(f"Added {new_qty} to stock.")
	except ValueError:
		# If it fails (like typing a word), we handle the error safely
		print("Error: Quantity must be a valid number!")

# Testing the function twice
add_stock(5)
add_stock("five")
