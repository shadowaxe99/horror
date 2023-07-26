import React, { useState } from 'react';

const Customization = () => {
  const [userCustomizations, setUserCustomizations] = useState({
    characters: '',
    setting: '',
    plotTwist: '',
  });

  const handleInputChange = (event) => {
    setUserCustomizations({
      ...userCustomizations,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Call the customizeStory function from the backend
    // customizeStory(userCustomizations);
  };

  return (
    <div id="customizationForm">
      <h2>Customize Your Horror Story</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Characters:
          <input
            type="text"
            name="characters"
            value={userCustomizations.characters}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Setting:
          <input
            type="text"
            name="setting"
            value={userCustomizations.setting}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Plot Twist:
          <input
            type="text"
            name="plotTwist"
            value={userCustomizations.plotTwist}
            onChange={handleInputChange}
          />
        </label>
        <button type="submit">Generate Story</button>
      </form>
    </div>
  );
};

export default Customization;