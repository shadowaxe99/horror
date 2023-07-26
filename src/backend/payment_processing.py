```python
import stripe
from flask import request
from .database import UserSchema

stripe.api_key = "your_stripe_api_key"

def handle_payment():
    user_id = request.form.get('user_id')
    token = request.form.get('stripeToken')
    amount = request.form.get('amount')

    user = UserSchema.query.get(user_id)

    if not user:
        return {"error": "User not found"}, 404

    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            description='AI Horror Story Generator Premium Access',
            source=token,
        )
    except stripe.error.CardError as e:
        return {"error": str(e)}, 400

    user.premiumAccess = True
    user.save()

    return {"message": "Payment successful, premium access granted"}

def handle_in_app_purchase():
    user_id = request.form.get('user_id')
    token = request.form.get('stripeToken')
    item_id = request.form.get('item_id')

    user = UserSchema.query.get(user_id)

    if not user:
        return {"error": "User not found"}, 404

    item = get_item_by_id(item_id)

    if not item:
        return {"error": "Item not found"}, 404

    try:
        charge = stripe.Charge.create(
            amount=item.price,
            currency='usd',
            description=f'AI Horror Story Generator In-App Purchase: {item.name}',
            source=token,
        )
    except stripe.error.CardError as e:
        return {"error": str(e)}, 400

    user.inAppPurchases.append(item)
    user.save()

    return {"message": "In-app purchase successful"}

def get_item_by_id(item_id):
    # This function should return the item with the given id from your database
    pass
```