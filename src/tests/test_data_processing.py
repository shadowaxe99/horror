```python
import unittest
from src.utils.data_processing import process_story_data, process_user_data

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        self.story_data = {
            "prompt": "Haunted House",
            "customizations": {
                "characters": ["John", "Sarah"],
                "setting": "Abandoned Mansion",
                "plotTwist": "The house is not haunted, the characters are."
            },
            "scareIntensity": 8
        }

        self.user_data = {
            "username": "horrorFan101",
            "savedStories": [],
            "premiumAccess": False,
            "inAppPurchases": []
        }

    def test_process_story_data(self):
        processed_data = process_story_data(self.story_data)
        self.assertIsInstance(processed_data, dict)
        self.assertIn('prompt', processed_data)
        self.assertIn('customizations', processed_data)
        self.assertIn('scareIntensity', processed_data)

    def test_process_user_data(self):
        processed_data = process_user_data(self.user_data)
        self.assertIsInstance(processed_data, dict)
        self.assertIn('username', processed_data)
        self.assertIn('savedStories', processed_data)
        self.assertIn('premiumAccess', processed_data)
        self.assertIn('inAppPurchases', processed_data)

if __name__ == '__main__':
    unittest.main()
```