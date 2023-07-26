```python
class Monetization:
    def __init__(self):
        self.premiumAccess = False
        self.inAppPurchases = []

    def subscribePremium(self, user):
        if user.balance >= 10:  # assuming subscription cost is 10
            user.balance -= 10
            self.premiumAccess = True
            return "Subscribed"
        else:
            return "Insufficient balance"

    def makePurchase(self, user, item):
        if user.balance >= item.cost:
            user.balance -= item.cost
            self.inAppPurchases.append(item)
            return "Purchased"
        else:
            return "Insufficient balance"

class User:
    def __init__(self, balance):
        self.balance = balance
        self.monetization = Monetization()

class Item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

# Example usage
user = User(20)
print(user.monetization.subscribePremium(user))  # Subscribed
item = Item("Extra Scary Story Pack", 5)
print(user.monetization.makePurchase(user, item))  # Purchased
```