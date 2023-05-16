# An_Online_Shop
An eCommerce website with payment processing.
Let's build an eCommerce website with payment processing in Python. We'll use the Flask framework for building the web application and Stripe for payment processing.

Here's a step-by-step guide to building the website:

Step 1: Install Flask and Stripe
-------------------------------
Make sure you have Flask and Stripe installed. You can install them using pip:

```
pip install flask stripe
```

Step 2: Set up Stripe
---------------------
Create a Stripe account at https://stripe.com/ and get your API keys. You'll need your API keys to process payments.

Step 3: Create a new Flask app
------------------------------
Create a new Python file, let's call it `app.py`, and add the following code:

```python
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
```

Step 4: Create the HTML templates
---------------------------------
Create a new folder called `templates` and within it, create two files: `index.html` and `charge.html`. Add the following code to the `index.html` file:

```html
<!DOCTYPE html>
<html>
<head>
    <title>eCommerce Website</title>
</head>
<body>
    <h1>Welcome to our eCommerce website</h1>
    <form action="/charge" method="post">
        <label for="amount">Amount:</label>
        <input type="text" name="amount" id="amount"><br>
        <label for="description">Description:</label>
        <input type="text" name="description" id="description"><br>
        <button type="submit">Pay with Stripe</button>
    </form>
</body>
</html>
```

Add the following code to the `charge.html` file:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Payment Processing</title>
    <script src="https://js.stripe.com/v3/"></script>
</head>
<body>
    <h1>Payment Processing</h1>
    <form id="payment-form">
        <div id="card-element">
        </div>
        <button id="submit-button" type="submit">Submit Payment</button>
    </form>

    <script>
        var stripe = Stripe('<your_publishable_key>');

        // Set up the Stripe.js elements
        var elements = stripe.elements();
        var cardElement = elements.create('card');
        cardElement.mount('#card-element');

        // Set up the payment form submission
        var form = document.getElementById('payment-form');
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            stripe.confirmCardPayment('{{ client_secret }}', {
                payment_method: {
                    card: cardElement,
                    billing_details: {
                        name: '{{ description }}'
                    }
                }
            }).then(function(result) {
                if (result.error) {
                    // Show error to your customer
                    console.log(result

.error.message);
                } else {
                    // The payment was processed successfully
                    console.log(result.paymentIntent);
                }
            });
        });
    </script>
</body>
</html>
```

Step 5: Run the Flask app
-------------------------
Save all the changes, and from the command line, navigate to the directory containing `app.py`. Run the following command to start the Flask app:

```
python app.py
```

You should see output similar to the following:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now, open your web browser and go to `http://127.0.0.1:5000/`. You should see the eCommerce website with a form to enter the payment amount and description. When you submit the form, it will process the payment using Stripe's payment processing API.

Note: Replace `<your_secret_key>` and `<your_publishable_key>` with your actual Stripe API keys in the `app.py` file and `charge.html` file respectively.

That's it! You have built an eCommerce website with payment processing using Python and Flask with Stripe integration. Remember to handle errors and security considerations when deploying a real-world application.