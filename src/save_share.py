```python
import json
from src.models import UserSchema, StorySchema

savedStories = []

def saveStory(user_id, story_id):
    """
    Save the generated story to the user's saved stories.
    """
    user = UserSchema.objects.get(id=user_id)
    story = StorySchema.objects.get(id=story_id)
    user.saved_stories.append(story)
    user.save()
    savedStories.append(story)
    print(f"Story {story_id} saved successfully for user {user_id}.")

def shareStory(story_id, platform):
    """
    Share the generated story on the specified platform.
    """
    story = StorySchema.objects.get(id=story_id)
    story_json = json.dumps(story.to_mongo().to_dict())
    
    if platform == "facebook":
        # Code to share story on Facebook
        pass
    elif platform == "twitter":
        # Code to share story on Twitter
        pass
    elif platform == "email":
        # Code to share story via Email
        pass
    else:
        print("Invalid platform. Please choose from 'facebook', 'twitter', or 'email'.")
    
    print(f"Story {story_id} shared successfully on {platform}.")
```