# Storing inventory data using SKUs as keys
inventory = {
    "ABC123": 7,
    "XYZ999": 0
}

# Prompt the user
sku = input("Enter SKU: ")

# Check if it exists FIRST to prevent a crash
if sku in inventory:
    # Retrieve the item quantity
    qty = inventory[sku]
    
    print("\nInventory:")
    print(f"{sku} -> {qty} units\n")
    
    # Check its quantity and produce a result
    if qty > 0:
        print("Result:\nIn stock")
    else:
        print("Result:\nOut of stock")
        
else:
    # The Failure Case handling
    print("\nResult:\nProduct not found")
