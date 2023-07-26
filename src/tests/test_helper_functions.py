```python
import unittest
from src.utils.helper_functions import selectPrompt, customizeStory, generateStory, adjustScareIntensity, toggleAudioNarration, saveStory, shareStory, submitFeedback, subscribePremium, makePurchase

class TestHelperFunctions(unittest.TestCase):

    def setUp(self):
        self.storyPrompts = ["Haunted House", "Paranormal Encounter", "Mysterious Creature"]
        self.userCustomizations = {"characters": "John and Mary", "setting": "Abandoned Mansion", "plotTwist": "The ghost is friendly"}
        self.scareIntensity = 5
        self.audioNarration = True
        self.premiumAccess = False
        self.inAppPurchases = []

    def test_selectPrompt(self):
        prompt = selectPrompt(self.storyPrompts)
        self.assertIn(prompt, self.storyPrompts)

    def test_customizeStory(self):
        customizations = customizeStory(self.userCustomizations)
        self.assertEqual(customizations, self.userCustomizations)

    def test_generateStory(self):
        story = generateStory(self.userCustomizations)
        self.assertIsInstance(story, str)

    def test_adjustScareIntensity(self):
        intensity = adjustScareIntensity(self.scareIntensity)
        self.assertEqual(intensity, self.scareIntensity)

    def test_toggleAudioNarration(self):
        narration = toggleAudioNarration(self.audioNarration)
        self.assertEqual(narration, self.audioNarration)

    def test_saveStory(self):
        saved = saveStory("A spooky story")
        self.assertTrue(saved)

    def test_shareStory(self):
        shared = shareStory("A spooky story")
        self.assertTrue(shared)

    def test_submitFeedback(self):
        feedback = submitFeedback("Great app!")
        self.assertTrue(feedback)

    def test_subscribePremium(self):
        subscribed = subscribePremium(self.premiumAccess)
        self.assertTrue(subscribed)

    def test_makePurchase(self):
        purchase = makePurchase("Extra Scary Story Pack")
        self.assertIn(purchase, self.inAppPurchases)

if __name__ == '__main__':
    unittest.main()
```