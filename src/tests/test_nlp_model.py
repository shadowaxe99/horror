```python
import unittest
from src.models.nlp_model import NLPModel

class TestNLPModel(unittest.TestCase):

    def setUp(self):
        self.nlp_model = NLPModel()

    def test_generate_story(self):
        story_prompt = "A haunted house on a hill"
        user_customizations = {
            "characters": ["John", "Sarah"],
            "setting": "A small town in the 1800s",
            "plot_twist": "The house is not haunted, the town is"
        }
        generated_story = self.nlp_model.generate_story(story_prompt, user_customizations)
        self.assertIsInstance(generated_story, str)

    def test_generate_story_with_invalid_prompt(self):
        story_prompt = 12345  # Invalid prompt, should be a string
        user_customizations = {
            "characters": ["John", "Sarah"],
            "setting": "A small town in the 1800s",
            "plot_twist": "The house is not haunted, the town is"
        }
        with self.assertRaises(TypeError):
            self.nlp_model.generate_story(story_prompt, user_customizations)

    def test_generate_story_with_invalid_customizations(self):
        story_prompt = "A haunted house on a hill"
        user_customizations = "Invalid customizations"  # Should be a dictionary
        with self.assertRaises(TypeError):
            self.nlp_model.generate_story(story_prompt, user_customizations)

if __name__ == '__main__':
    unittest.main()
```