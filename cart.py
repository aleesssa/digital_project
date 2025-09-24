from items import items

def get_user_input():
    """Handle user selections and return a cart with items and quantities."""
    cart = {}
    while True:
        print("\nEnter the item number to add to cart (or 'q' to quit):")
        choice = input("> ").strip().lower()
        
        if choice == 'q':
            break
        
        try:
            code = int(choice)
            if code not in items:
                print("Invalid item number. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")
            continue
        
        # get quantity with validation
        try:
            quantity = int(input(f"How many {items[code][0]}s would you like? "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue
        
        cart[code] = cart.get(code, 0) + quantity
        print(f"Added {quantity} {items[code][0]} to cart.")
    
    return cart