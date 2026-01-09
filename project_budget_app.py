"""
Budget App module.
Implements a Category class for budget management and a function
to create a spending chart by category.
"""

class Category:
    """Represents a budget category with deposit, withdraw, transfer, and balance methods."""
    def __init__(self, category):
        """Initialize the category with a name and an empty ledger."""
        self.category = category
        self.ledger = []

    def __str__(self):
        """Return a formatted string representation of the budget category."""
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0

        for entry in self.ledger:
            description = entry["description"][:23]
            amount = entry["amount"]
            items += f"{description:<23}{amount:>7.2f}\n"
            total += amount

        return title + items + f"Total: {total:.2f}"

    def deposit(self, amount, description=""):
        """Add a deposit to the ledger."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """Add a withdrawal to the ledger if funds are sufficient."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Return the current balance of the budget category."""
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, destination_category):
        """Transfer amount to another budget category if funds are sufficient."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination_category.category}")
            destination_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        """Check if there are sufficient funds for a withdrawal or transfer."""
        return amount <= self.get_balance()

def create_spend_chart(categories):
    """Create a bar chart showing percentage spent by category."""
    spent = []
    for category in categories:
        total = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent.append(total)

    total_spent = sum(spent)

    percentages = []
    for s in spent:
        percent = int((s / total_spent) * 100)
        percent -= percent % 10
        percentages.append(percent)

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in percentages:
            chart += "o  " if percent >= i else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [category.category for category in categories]
    max_length = max(len(name) for name in names)

    for i in range(max_length):
        chart += "     "
        for name in names:
            chart += f"{name[i]}  " if i < len(name) else "   "
        chart += "\n"

    return chart.rstrip("\n")

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(clothing)
