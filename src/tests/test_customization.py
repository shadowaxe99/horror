```python
import unittest
from src.customization import customizeStory

class TestCustomization(unittest.TestCase):

    def setUp(self):
        self.userCustomizations = {
            "characters": ["John", "Sarah"],
            "setting": "Haunted Mansion",
            "plotTwist": "The ghost is actually friendly"
        }

    def test_customizeStory(self):
        result = customizeStory(self.userCustomizations)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["characters"], self.userCustomizations["characters"])
        self.assertEqual(result["setting"], self.userCustomizations["setting"])
        self.assertEqual(result["plotTwist"], self.userCustomizations["plotTwist"])

    def test_invalidCustomization(self):
        with self.assertRaises(ValueError):
            customizeStory({"invalidKey": "invalidValue"})

if __name__ == '__main__':
    unittest.main()
```