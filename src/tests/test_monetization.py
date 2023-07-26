```python
import unittest
from src.monetization import subscribePremium, makePurchase

class TestMonetization(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.premiumAccess = False
        self.inAppPurchases = []

    def test_subscribePremium(self):
        self.premiumAccess = subscribePremium(self.user_id)
        self.assertTrue(self.premiumAccess)

    def test_makePurchase(self):
        purchase_item = "Extra Scary Story Pack"
        self.inAppPurchases = makePurchase(self.user_id, purchase_item)
        self.assertIn(purchase_item, self.inAppPurchases)

if __name__ == '__main__':
    unittest.main()
```