```python
import unittest
from src.save_share import saveStory, shareStory

class TestSaveShare(unittest.TestCase):

    def setUp(self):
        self.story = "It was a dark and stormy night..."
        self.user = "testUser"

    def test_saveStory(self):
        result = saveStory(self.user, self.story)
        self.assertEqual(result, True, "The story should be saved successfully.")

    def test_shareStory(self):
        result = shareStory(self.user, self.story)
        self.assertEqual(result, True, "The story should be shared successfully.")

if __name__ == '__main__':
    unittest.main()
```