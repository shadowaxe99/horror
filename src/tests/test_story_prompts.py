```python
import unittest
from src.story_prompts import selectPrompt, storyPrompts

class TestStoryPrompts(unittest.TestCase):

    def setUp(self):
        self.storyPrompts = storyPrompts

    def test_selectPrompt(self):
        selectedPrompt = selectPrompt()
        self.assertIn(selectedPrompt, self.storyPrompts)

    def test_storyPromptsNotEmpty(self):
        self.assertTrue(len(self.storyPrompts) > 0)

if __name__ == '__main__':
    unittest.main()
```