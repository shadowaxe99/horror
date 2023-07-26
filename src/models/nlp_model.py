```python
import openai
from src.utils.data_processing import process_text

class NLPModel:
    def __init__(self, api_key):
        self.api_key = api_key
        self.model = "text-davinci-002"
        openai.api_key = self.api_key

    def generate_story(self, prompt, user_customizations, scare_intensity):
        # Process the prompt and user customizations
        processed_prompt = process_text(prompt, user_customizations, scare_intensity)

        # Generate the story using OpenAI's GPT-3 model
        response = openai.Completion.create(
            engine=self.model,
            prompt=processed_prompt,
            max_tokens=1000,
            temperature=0.7
        )

        # Extract the generated story
        generated_story = response.choices[0].text.strip()

        return generated_story
```