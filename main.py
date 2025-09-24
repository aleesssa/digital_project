from items import show_menu
from cart import get_user_input
from calculate import print_receipt

# Display menu
show_menu()

# Add cart
cart = get_user_input()

# Print receipt
print_receipt(cart)
