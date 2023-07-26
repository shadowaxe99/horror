```python
import unittest
from src.user_feedback import submitFeedback

class TestUserFeedback(unittest.TestCase):

    def setUp(self):
        self.feedback = {
            "user_id": 1,
            "story_id": 1,
            "rating": 4,
            "comments": "Great story, but could be scarier."
        }

    def test_submit_feedback(self):
        response = submitFeedback(self.feedback)
        self.assertEqual(response["status"], 200)
        self.assertEqual(response["message"], "Feedback submitted successfully.")

    def test_invalid_feedback(self):
        invalid_feedback = self.feedback.copy()
        invalid_feedback["rating"] = 6  # Rating should be between 1 and 5
        response = submitFeedback(invalid_feedback)
        self.assertEqual(response["status"], 400)
        self.assertEqual(response["message"], "Invalid feedback.")

    def test_missing_feedback_fields(self):
        incomplete_feedback = self.feedback.copy()
        del incomplete_feedback["rating"]  # Rating is a required field
        response = submitFeedback(incomplete_feedback)
        self.assertEqual(response["status"], 400)
        self.assertEqual(response["message"], "Missing required feedback fields.")

if __name__ == "__main__":
    unittest.main()
```