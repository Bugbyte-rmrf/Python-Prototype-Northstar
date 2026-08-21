current_stock = "five"
target_stock = 10

print("Calculating order amount...")

# This logic is broken. You cannot subtract a string from an integer.
order_amount = target_stock - current_stock

print(f"You need to order {order_amount} units.")
