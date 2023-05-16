from flask import Flask, render_template, request
import stripe

app = Flask(__name__)

# Set up Stripe
stripe.api_key = '<your_secret_key>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charge', methods=['POST'])
def charge():
    # Get the amount and description from the form
    amount = request.form['amount']
    description = request.form['description']

    # Convert the amount to cents
    amount_cents = int(float(amount) * 100)

    # Create a Stripe payment intent
    intent = stripe.PaymentIntent.create(
        amount=amount_cents,
        currency='usd',
        description=description
    )

    # Render the charge template with the payment intent ID
    return render_template('charge.html', client_secret=intent.client_secret)

if __name__ == '__main__':
    app.run(debug=True)
