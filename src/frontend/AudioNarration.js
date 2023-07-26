import React, { useState, useEffect } from 'react';
import { Howl, Howler } from 'howler';

const AudioNarration = ({ generatedStory }) => {
  const [audioNarration, setAudioNarration] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);

  useEffect(() => {
    if (generatedStory) {
      const sound = new Howl({
        src: [generatedStory.audioNarration],
        html5: true
      });

      setAudioNarration(sound);
    }
  }, [generatedStory]);

  const toggleAudioNarration = () => {
    if (isPlaying) {
      audioNarration.pause();
    } else {
      audioNarration.play();
    }

    setIsPlaying(!isPlaying);
  };

  return (
    <div id="audioNarrationToggle">
      <button onClick={toggleAudioNarration}>
        {isPlaying ? 'Pause Narration' : 'Play Narration'}
      </button>
    </div>
  );
};

export default AudioNarration;