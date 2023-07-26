```python
from flask import Flask, request, jsonify
from database import UserSchema, StorySchema
from authentication import authenticate_user
from payment_processing import process_payment
from api_routes import story_routes, user_routes, payment_routes

app = Flask(__name__)

@app.route('/api/story', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_story():
    if request.method == 'GET':
        return story_routes.get_story(request)
    elif request.method == 'POST':
        return story_routes.create_story(request)
    elif request.method == 'PUT':
        return story_routes.update_story(request)
    elif request.method == 'DELETE':
        return story_routes.delete_story(request)

@app.route('/api/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_user():
    if request.method == 'GET':
        return user_routes.get_user(request)
    elif request.method == 'POST':
        return user_routes.create_user(request)
    elif request.method == 'PUT':
        return user_routes.update_user(request)
    elif request.method == 'DELETE':
        return user_routes.delete_user(request)

@app.route('/api/payment', methods=['POST'])
def handle_payment():
    return payment_routes.process_payment(request)

@app.route('/api/authenticate', methods=['POST'])
def handle_authentication():
    return authenticate_user(request)

if __name__ == '__main__':
    app.run(debug=True)
```