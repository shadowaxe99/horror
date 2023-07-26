import React, { useState, useEffect } from 'react';

const StoryPromptSelection = ({ storyPrompts, selectPrompt }) => {
  const [selectedPrompt, setSelectedPrompt] = useState('');

  useEffect(() => {
    if (storyPrompts.length > 0) {
      setSelectedPrompt(storyPrompts[0]);
    }
  }, [storyPrompts]);

  const handlePromptChange = (event) => {
    setSelectedPrompt(event.target.value);
    selectPrompt(event.target.value);
  };

  return (
    <div id="storyPromptSelection">
      <label htmlFor="storyPrompt">Select a Story Prompt:</label>
      <select name="storyPrompt" value={selectedPrompt} onChange={handlePromptChange}>
        {storyPrompts.map((prompt, index) => (
          <option key={index} value={prompt}>
            {prompt}
          </option>
        ))}
      </select>
    </div>
  );
};

export default StoryPromptSelection;