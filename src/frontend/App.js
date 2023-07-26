```javascript
import React, { useState } from 'react';
import StoryPromptSelection from './StoryPromptSelection';
import Customization from './Customization';
import AIStoryGeneration from './AIStoryGeneration';
import ScareIntensityControl from './ScareIntensityControl';
import AudioNarration from './AudioNarration';
import SaveShare from './SaveShare';
import UserFeedback from './UserFeedback';
import Monetization from './Monetization';
import './styles.css';

function App() {
  const [storyPrompt, setStoryPrompt] = useState('');
  const [customizations, setCustomizations] = useState({});
  const [generatedStory, setGeneratedStory] = useState('');
  const [scareIntensity, setScareIntensity] = useState(0);
  const [audioNarration, setAudioNarration] = useState(false);
  const [savedStories, setSavedStories] = useState([]);
  const [userFeedback, setUserFeedback] = useState('');
  const [premiumAccess, setPremiumAccess] = useState(false);
  const [inAppPurchases, setInAppPurchases] = useState([]);

  return (
    <div className="App">
      <StoryPromptSelection storyPrompt={storyPrompt} setStoryPrompt={setStoryPrompt} />
      <Customization customizations={customizations} setCustomizations={setCustomizations} />
      <AIStoryGeneration 
        storyPrompt={storyPrompt} 
        customizations={customizations} 
        setGeneratedStory={setGeneratedStory} 
      />
      <ScareIntensityControl scareIntensity={scareIntensity} setScareIntensity={setScareIntensity} />
      <AudioNarration audioNarration={audioNarration} setAudioNarration={setAudioNarration} />
      <SaveShare 
        generatedStory={generatedStory} 
        savedStories={savedStories} 
        setSavedStories={setSavedStories} 
      />
      <UserFeedback userFeedback={userFeedback} setUserFeedback={setUserFeedback} />
      <Monetization 
        premiumAccess={premiumAccess} 
        setPremiumAccess={setPremiumAccess} 
        inAppPurchases={inAppPurchases} 
        setInAppPurchases={setInAppPurchases} 
      />
    </div>
  );
}

export default App;
```