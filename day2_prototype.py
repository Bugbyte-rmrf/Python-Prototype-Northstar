# A. Multiple products
inventory = {
    "SKU001": 15,
    "SKU002": 0,
    "SKU003": 8
}

print("--- Northstar Inventory System ---")
print("Type 'quit' to exit.\n")

while True:
    # D. Error handling: try/except catches unexpected system errors like Ctrl+C
    try:

        # B. User interaction
        # .strip() removes accidental spaces at the start/end
        sku = input("Enter SKU: ").strip()
        
        # Allow the user a safe way to exit the loop
        if sku.lower() == "quit":
            print("Exiting system. Goodbye!")
            break
            
        # D. Error handling: Prevent empty/blank inputs
        if sku == "":
            print("Error: SKU cannot be blank. Please try again.\n")
            continue 
            

        # C. Correct results
        if sku in inventory:
            qty = inventory[sku]
            print(f"\nInventory:\n{sku} -> {qty} units")
            
            if qty > 0:
                print("Result:\nIn stock\n")
            else:
                print("Result:\nOut of stock\n")
        else:
            print("\nResult:\nUnknown product\n")
            
    except KeyboardInterrupt:
        # D. Error handling: If the user presses Ctrl+C, exit gracefully
        print("\nForce quit detected. Exiting safely...")
        break
