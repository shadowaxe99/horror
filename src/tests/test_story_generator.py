```python
import unittest
from src.story_generator import generateStory, selectPrompt, customizeStory

class TestStoryGenerator(unittest.TestCase):

    def setUp(self):
        self.prompt = selectPrompt()
        self.customizations = customizeStory()

    def test_generateStory(self):
        story = generateStory(self.prompt, self.customizations)
        self.assertIsInstance(story, str)
        self.assertGreater(len(story), 0)

    def test_selectPrompt(self):
        self.assertIsInstance(self.prompt, str)
        self.assertGreater(len(self.prompt), 0)

    def test_customizeStory(self):
        self.assertIsInstance(self.customizations, dict)
        self.assertGreater(len(self.customizations), 0)

if __name__ == '__main__':
    unittest.main()
```