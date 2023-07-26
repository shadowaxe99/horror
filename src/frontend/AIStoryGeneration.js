import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AIStoryGeneration = () => {
  const [storyPrompts, setStoryPrompts] = useState([]);
  const [userCustomizations, setUserCustomizations] = useState({});
  const [generatedStory, setGeneratedStory] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Fetch story prompts from the server
    axios.get('/api/story_prompts')
      .then(response => {
        setStoryPrompts(response.data);
      })
      .catch(error => {
        console.error('Error fetching story prompts:', error);
      });
  }, []);

  const generateStory = () => {
    setLoading(true);
    axios.post('/api/generate_story', {
      prompt: storyPrompts,
      customizations: userCustomizations
    })
      .then(response => {
        setGeneratedStory(response.data.story);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error generating story:', error);
        setLoading(false);
      });
  };

  return (
    <div>
      <h1>AI Horror Story Generator</h1>
      <button onClick={generateStory} disabled={loading}>
        {loading ? 'Generating...' : 'Generate Story'}
      </button>
      {generatedStory && (
        <div>
          <h2>Your Generated Story</h2>
          <p>{generatedStory}</p>
        </div>
      )}
    </div>
  );
};

export default AIStoryGeneration;