```python
class Customization:
    def __init__(self):
        self.userCustomizations = {}

    def customizeStory(self, prompt, characters, setting, plotTwist):
        self.userCustomizations['prompt'] = prompt
        self.userCustomizations['characters'] = characters
        self.userCustomizations['setting'] = setting
        self.userCustomizations['plotTwist'] = plotTwist

    def getUserCustomizations(self):
        return self.userCustomizations
```