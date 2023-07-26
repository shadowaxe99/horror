import React, { useState } from 'react';

const ScareIntensityControl = () => {
  const [scareIntensity, setScareIntensity] = useState(5);

  const handleIntensityChange = (event) => {
    setScareIntensity(event.target.value);
  };

  return (
    <div id="scareIntensitySlider">
      <label htmlFor="scareIntensity">Scare Intensity:</label>
      <input
        type="range"
        id="scareIntensity"
        name="scareIntensity"
        min="1"
        max="10"
        value={scareIntensity}
        onChange={handleIntensityChange}
      />
      <p>{`Scare Intensity: ${scareIntensity}`}</p>
    </div>
  );
};

export default ScareIntensityControl;