```python
from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['horror_story_db']

    def get_user(self, user_id):
        return self.db.users.find_one({"_id": user_id})

    def save_user(self, user_data):
        self.db.users.update_one({"_id": user_data["_id"]}, {"$set": user_data}, upsert=True)

    def get_story(self, story_id):
        return self.db.stories.find_one({"_id": story_id})

    def save_story(self, story_data):
        self.db.stories.update_one({"_id": story_data["_id"]}, {"$set": story_data}, upsert=True)

    def get_user_stories(self, user_id):
        return self.db.stories.find({"user_id": user_id})

    def get_user_feedback(self, user_id):
        return self.db.feedback.find({"user_id": user_id})

    def save_feedback(self, feedback_data):
        self.db.feedback.insert_one(feedback_data)

    def get_purchases(self, user_id):
        return self.db.purchases.find({"user_id": user_id})

    def save_purchase(self, purchase_data):
        self.db.purchases.insert_one(purchase_data)

database = Database()
```