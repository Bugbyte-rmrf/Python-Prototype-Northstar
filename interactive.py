# Lists, Dictionaries, Strings, Numbers
inventory = [
    {"name": "Coffee", "qty": 10},
    {"name": "Mug", "qty": 0}
]

# Functions
def run_store():
    print("--- Welcome to the Store ---")
    
    # Loops, Booleans (True is a boolean)
    while True:
        # The input() function pauses the program and waits for the user to type
        action = input("Do you want to (view), (add), or (quit)? ")
        
        # If statements
        if action == "quit":
            print("Goodbye!")
            break  # This breaks us out of the while loop
            
        elif action == "view":
            for item in inventory:
                print(f"- {item['name']}: {item['qty']} in stock")
                
        elif action == "add":
            item_name = input("Enter product name: ")
            qty_input = input("Enter quantity to add: ")
            
            # Exceptions/Errors
            try:
                # Variables
                new_qty = int(qty_input)
                inventory.append({"name": item_name, "qty": new_qty})
                print(f"Added {new_qty} {item_name} to inventory!")
            except ValueError:
                print("Error: You must type a valid number for the quantity!")
                
        else:
            print("I don't understand that command.")

# Call the function to start the program
run_store()
