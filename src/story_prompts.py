```python
# src/story_prompts.py

storyPrompts = [
    "A group of friends decide to explore an abandoned mansion in their town.",
    "A family moves into a new house, only to discover that it's haunted.",
    "A paranormal investigator is called to a small town to investigate a series of unexplained occurrences.",
    "A hiker gets lost in the woods and stumbles upon an ancient, malevolent entity.",
    "A scientist's experiment goes horribly wrong, unleashing a monstrous creature into the world.",
    "A town is plagued by a mysterious creature that only comes out at night.",
    "A person starts to experience terrifying visions after finding an old artifact.",
    "A group of teenagers accidentally awaken an ancient evil during a camping trip.",
    "A detective investigates a series of gruesome murders, only to discover a horrifying truth.",
    "A person starts to suspect that their neighbor is a vampire.",
    "A writer moves to a secluded cabin to work on their novel, but strange things start to happen.",
    "A group of explorers discover a hidden, underground city that's not abandoned."
]

def selectPrompt(prompt_index):
    try:
        return storyPrompts[prompt_index]
    except IndexError:
        return "Invalid prompt index. Please select a valid index."
```