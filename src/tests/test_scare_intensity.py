```python
import unittest
from src.scare_intensity import adjustScareIntensity

class TestScareIntensity(unittest.TestCase):

    def setUp(self):
        self.scareIntensity = 5

    def test_adjustScareIntensity(self):
        # Test increasing scare intensity
        self.scareIntensity = adjustScareIntensity(self.scareIntensity, 2)
        self.assertEqual(self.scareIntensity, 7)

        # Test decreasing scare intensity
        self.scareIntensity = adjustScareIntensity(self.scareIntensity, -3)
        self.assertEqual(self.scareIntensity, 4)

        # Test scare intensity boundaries
        self.scareIntensity = adjustScareIntensity(self.scareIntensity, -10)
        self.assertEqual(self.scareIntensity, 1)

        self.scareIntensity = adjustScareIntensity(self.scareIntensity, 10)
        self.assertEqual(self.scareIntensity, 10)

if __name__ == '__main__':
    unittest.main()
```