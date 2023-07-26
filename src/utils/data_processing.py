```python
import json
from src.models import UserSchema, StorySchema

def load_story_prompts(file_path):
    with open(file_path, 'r') as file:
        storyPrompts = json.load(file)
    return storyPrompts

def save_generated_story(user_id, generatedStory):
    user = UserSchema.objects(id=user_id).first()
    if user:
        user.savedStories.append(generatedStory)
        user.save()
    else:
        raise ValueError("User not found")

def load_user_customizations(user_id):
    user = UserSchema.objects(id=user_id).first()
    if user:
        return user.userCustomizations
    else:
        raise ValueError("User not found")

def save_user_customizations(user_id, userCustomizations):
    user = UserSchema.objects(id=user_id).first()
    if user:
        user.userCustomizations = userCustomizations
        user.save()
    else:
        raise ValueError("User not found")

def load_user_feedback(user_id):
    user = UserSchema.objects(id=user_id).first()
    if user:
        return user.userFeedback
    else:
        raise ValueError("User not found")

def save_user_feedback(user_id, userFeedback):
    user = UserSchema.objects(id=user_id).first()
    if user:
        user.userFeedback = userFeedback
        user.save()
    else:
        raise ValueError("User not found")

def load_in_app_purchases(user_id):
    user = UserSchema.objects(id=user_id).first()
    if user:
        return user.inAppPurchases
    else:
        raise ValueError("User not found")

def save_in_app_purchases(user_id, inAppPurchases):
    user = UserSchema.objects(id=user_id).first()
    if user:
        user.inAppPurchases = inAppPurchases
        user.save()
    else:
        raise ValueError("User not found")
```