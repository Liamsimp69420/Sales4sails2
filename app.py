from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    # Implement product retrieval logic here
    products = [
        {'name': 'Octopus', 'price': 19.99},
        {'name': 'Race Cart', 'price': 299.99}
    ]
    return render_template('products.html', products=products)

@app.route('/checkout', methods=['POST'])
def checkout():
    # Implement checkout logic here
    # Process payment, update inventory, etc.
    return redirect('/')
