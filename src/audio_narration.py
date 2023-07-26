```python
import pyttsx3

class AudioNarration:
    def __init__(self):
        self.engine = pyttsx3.init()

    def set_audio_parameters(self):
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate-50)
        volume = self.engine.getProperty('volume')
        self.engine.setProperty('volume', volume+0.25)

    def narrate_story(self, generatedStory):
        self.set_audio_parameters()
        self.engine.say(generatedStory)
        self.engine.runAndWait()

audioNarration = AudioNarration()
```