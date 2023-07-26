import React, { useState } from 'react';
import axios from 'axios';

const UserFeedback = () => {
  const [feedback, setFeedback] = useState('');
  const [userFeedback, setUserFeedback] = useState([]);

  const handleFeedbackChange = (event) => {
    setFeedback(event.target.value);
  };

  const submitFeedback = async () => {
    try {
      const response = await axios.post('/api/feedback', { feedback });
      setUserFeedback([...userFeedback, response.data]);
      setFeedback('');
      alert('FeedbackSubmitted');
    } catch (error) {
      console.error('Error submitting feedback', error);
    }
  };

  return (
    <div id="feedbackForm">
      <h2>Your Feedback</h2>
      <textarea
        value={feedback}
        onChange={handleFeedbackChange}
        placeholder="Share your thoughts about the generated story..."
      />
      <button onClick={submitFeedback}>Submit Feedback</button>
      <h3>Previous Feedback</h3>
      <ul>
        {userFeedback.map((feedback, index) => (
          <li key={index}>{feedback}</li>
        ))}
      </ul>
    </div>
  );
};

export default UserFeedback;