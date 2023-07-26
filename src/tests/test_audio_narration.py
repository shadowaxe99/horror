```python
import unittest
from src.audio_narration import toggleAudioNarration

class TestAudioNarration(unittest.TestCase):

    def setUp(self):
        self.audioNarration = False

    def test_toggleAudioNarration(self):
        # Test toggling audio narration on
        self.audioNarration = toggleAudioNarration(self.audioNarration)
        self.assertEqual(self.audioNarration, True)

        # Test toggling audio narration off
        self.audioNarration = toggleAudioNarration(self.audioNarration)
        self.assertEqual(self.audioNarration, False)

if __name__ == '__main__':
    unittest.main()
```