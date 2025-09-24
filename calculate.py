from items import items 

def calculate_total(cart):
#to calculate the total price of items in cart
    total = 0.0
    for code, qty in cart.items():
        if code in items:
            _, price = items[code]
            total += price * qty
    return round(total, 2)


def print_receipt(cart):
#print receipt 
    grand_total = calculate_total(cart)
    print("\n===== Receipt =====")
    for code, qty in cart.items():
        if code in items:
            name, price = items[code]
            subtotal = price * qty
            print(f"{name:<25} x{qty:<2} RM{subtotal:.2f}")
    print("===================")
    print(f"Total: RM{grand_total:.2f}")
    print("Thank you for shopping with us!")


#self test purpose
# if __name__ == "__main__":
#     test_cart = {1: 2, 3: 1}  
#     print_receipt(test_cart)