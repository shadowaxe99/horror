```python
from flask import request
from src.models import UserSchema

user_schema = UserSchema()

def submit_feedback():
    user_feedback = request.json.get('feedback', None)
    if user_feedback:
        user_id = request.json.get('user_id', None)
        user = user_schema.load({'id': user_id})
        if user:
            user.feedback.append(user_feedback)
            user_schema.dump(user)
            return {"message": "Feedback submitted successfully."}, 200
        else:
            return {"message": "User not found."}, 404
    else:
        return {"message": "No feedback provided."}, 400
```