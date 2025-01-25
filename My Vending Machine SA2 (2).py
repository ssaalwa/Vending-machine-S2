
class VendingMachine:
    def __init__(My):
        # Stock the vending machine with items and their prices
        My.items = {
            '1': {'name': 'water', 'price': 0.30, 'category': 'Drinks'},
            '2': {'name': 'Juice', 'price': 1.00, 'category': 'Drinks'},
            '3': {'name': 'Ice Tea', 'price': 1.30, 'category': 'Drinks'},
            '4': {'name': 'Chocolate', 'price': 1.00, 'category': 'Snacks'},
            '5': {'name': 'Cookies', 'price': 1.20, 'category': 'Snacks'},
            '6': {'name': 'Latte', 'price': 2.00, 'category': 'Hot Drinks'},
            '7': {'name': 'Coffee', 'price': 2.50, 'category': 'Hot Drinks'},
            '8': {'name': 'Tea', 'price': 2.00, 'category': 'Hot Drinks'},
        }

    def display_menu(My):
        # Display the menu of items
        print("Items Available:")
        for code, item in My.items.items():
            # Print each items code, name, price, and category
            print(f"{code}: {item['name']} - ${item['price']} ({item['category']})")

    def insert_money(My, amount):
        # Inform the customer to insert money
        if amount <= 0:
            # Check if the inserted amount is positive 
            print("Kindly insert a valid amount of money.")
            return #  Exit the method if the amount is not valid
        print(f"You have inserted ${amount:.2f}.") # Confirn the amount is inserted

    def select_item(My, code, amount):
        # Select an item based on the code
        if code in My.items:
            item = My.items[code]
            if amount >= item['price']:
                # Check if the inserted amount is sufficiant to purchase the item
                print(f"Delivering {item['name']}.") # Deliver the item
                change = amount - item['price'] # Calculate the change
                if change > 0:
                    # Inform the user, if there is change to return
                    print(f"Returning change: ${change:.2f}")
                # Suggest additional items from the same category
                My.suggest_additional_items(item['category'], item['name'])
            else:
                # Inform the user if the inserted amount is unsufficient 
                print("Not enough money. kindly insert the right amount of money.")
        else:
            # Inform the user if the item code is not valid
            print("Invalid choice. Kindly choose a valid item code.")

    def suggest_additional_items (My, category, purchased_item_name):
        # Suggest additional items based on the category of the purchased item
        suggestions = [item for item in My.items.values() if item['category'] == category and item['name'] != purchased_item_name]
        if suggestions:
            # Check if there are items to suggest
            print("You might also like to buy:")
            for item in suggestions:
                print(f"- {item['name']} - ${item['price']}")

def main():
    # Create an instance of the vending machine class
    vending_machine = VendingMachine()
    
    print("Welcome to my Vending Machine!")  # Welcome message
    
    while True:
        # Display the menu of items
        vending_machine.display_menu()  # Display items first
        # Ask the user to select an item code
        item_code = input("Select an item by entering the item code (or type '0' to exit): ")
        if item_code == '0':
            # Thank the user and break the loop, if the user wants to exit
            print("Thank you for using My vending machine!:D")
            break
        # Ask the user to insert money for the item selected
        money = float(input("Insert money for the item you selected: "))
        vending_machine.insert_money(money)
        vending_machine.select_item(item_code, money)
# Entery point of the program
if __name__ == "__main__":
    main() # Call the main function to start the program

