```python
import random

def select_random_prompt(storyPrompts):
    return random.choice(storyPrompts)

def generate_random_name():
    names = ["John", "Sarah", "Mike", "Emily", "Alex", "Sophie"]
    return random.choice(names)

def generate_random_location():
    locations = ["haunted mansion", "abandoned hospital", "creepy forest", "deserted town", "ancient castle", "dark cave"]
    return random.choice(locations)

def generate_random_creature():
    creatures = ["ghost", "vampire", "werewolf", "zombie", "witch", "demon"]
    return random.choice(creatures)

def generate_random_plot_twist():
    plot_twists = ["the protagonist was the villain", "the creature was a friend", "it was all a dream", "the protagonist was dead all along", "the villain was trying to help", "the protagonist becomes the creature"]
    return random.choice(plot_twists)

def adjust_intensity(scareIntensity, generatedStory):
    if scareIntensity == "low":
        return generatedStory.lower()
    elif scareIntensity == "medium":
        return generatedStory
    else:
        return generatedStory.upper()

def toggle_audio_narration(audioNarration, generatedStory):
    if audioNarration:
        return f"Audio Narration: {generatedStory}"
    else:
        return generatedStory

def check_premium_access(premiumAccess):
    if premiumAccess:
        return "Premium Access: Enabled"
    else:
        return "Premium Access: Disabled"

def check_in_app_purchases(inAppPurchases):
    if inAppPurchases:
        return "In-App Purchases: Enabled"
    else:
        return "In-App Purchases: Disabled"
```