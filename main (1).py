##Define recipes for different sizes of sandwiches
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slice
            "ham": 4,  # slice
            "cheese": 4,  # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  # slice
            "ham": 6,  # slice
            "cheese": 8,  # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  # slice
            "ham": 8,  # slice
            "cheese": 12,  # ounces
        },
        "cost": 5.5,
    }
}

# Define the initial resources
resources = {
    "bread": 12,  # slice
    "ham": 18,  # slice
    "cheese": 24,  # ounces
}

# Define the SandwichMachine class
class SandwichMachine:
    def __init__(self, machine_resources):
        """Initialize the machine with resources."""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Check if there are enough resources to make the sandwich."""
        for ingredient, quantity in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < quantity:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def process_coins(self):
        """Calculate the total amount of coins inserted."""
        print("Please insert coins.")
        coins = {
            "large dollar": 1,
            "half dollar": 0.5,
            "quarter": 0.25,
            "nickel": 0.05
        }
        total = 0
        for coin, value in coins.items():
            try:
                amount = int(input(f"Insert {coin}s: "))
                total += amount * value
            except ValueError:
                print("Invalid input. Please enter a number.")
        return total

    def transaction_result(self, coins, cost):
        """Check if the transaction is successful and provide change if necessary."""
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        else:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for ingredient, quantity in order_ingredients.items():
            self.machine_resources[ingredient] -= quantity
        print(f"Here is your {sandwich_size} sandwich. Bon appétit!")

# Create an instance of the SandwichMachine class
sandwich_machine = SandwichMachine(resources)

# Main loop to handle user input
while True:
    print("What would you like? (small/medium/large/off/report)")
    choice = input().lower()

    if choice in ["small", "medium", "large"]:
        order = recipes[choice]
        if sandwich_machine.check_resources(order["ingredients"]):
            print(f"The cost of the {choice} sandwich is ${order['cost']}")
            coins = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(coins, order['cost']):
                sandwich_machine.make_sandwich(choice, order["ingredients"])
    elif choice == "off":
        print("Turning off the sandwich machine. Goodbye!")
        break
    elif choice == "report":
        print("Current resources:")
        for resource, amount in sandwich_machine.machine_resources.items():
            print(f"{resource}: {amount}")
    else:
        print("Invalid choice. Please choose from small, medium, large, off, or report.")
