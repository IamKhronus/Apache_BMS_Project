from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user, login_required
from setup_database import Book, Customer, Order

# Flask setup 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apache_bookstore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Replace with a strong, random secret key

# Initialize database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@app.route('/')
def home():
    return render_template('home.html')  # Or whatever you want to display on the homepage

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Authentication logic
        customer = Customer.query.filter_by(username=username).first()
        if customer and customer.password == password:  # Basic password check (insecure!)
            login_user(customer)
            return redirect(url_for('home'))  # Or the page you want after login
        else:
            flash("Invalid username or password", "error")
            return redirect(url_for('login'))

    return render_template('login.html')

# Checkout route with validation
@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    if request.method == 'POST':
        # Extract data from the form
        book_title = request.form.get('book')
        quantity = request.form.get('quantity')
        shipping_address = request.form.get('address')
        card_name = request.form.get('name')
        card_number = request.form.get('card-number')
        expiry_date = request.form.get('expiry-date')
        cvv = request.form.get('cvv')

        card_number_last4 = card_number[-4:] if card_number else None

        # Enhanced Input Validation
        if not book_title or not book_title.strip():
            flash("Book title is required", "error")
            return redirect(url_for('checkout'))

        if not quantity or not quantity.isdigit() or int(quantity) <= 0:
            flash("Please provide a valid quantity", "error")
            return redirect(url_for('checkout'))

        if not shipping_address or not shipping_address.strip():
            flash("Shipping address is required", "error")
            return redirect(url_for('checkout'))

        if not card_name or not card_name.strip():
            flash("Name on card is required", "error")
            return redirect(url_for('checkout'))

        if not card_number or not card_number.isdigit() or len(card_number) != 16:
            flash("Please provide a valid 16-digit card number", "error")
            return redirect(url_for('checkout'))

        if not expiry_date or len(expiry_date) != 5 or not expiry_date[:2].isdigit() \
           or expiry_date[2] != '/' or not expiry_date[3:].isdigit():
            flash("Please provide a valid expiry date in MM/YY format", "error")
            return redirect(url_for('checkout'))

        if not cvv or not cvv.isdigit() or len(cvv) != 3:
            flash("Please provide a valid 3-digit CVV", "error")
            return redirect(url_for('checkout'))

        try:
            customer_id = current_user.id

            new_order = Order(
                book_title=book_title,
                quantity=int(quantity),
                shipping_address=shipping_address,
                card_name=card_name,
                card_number_last4=card_number_last4,
                customer_id=customer_id
            )
            db.session.add(new_order)
            db.session.commit()

            flash("Order submitted successfully!", "success")
            return render_template('confirmation.html',
                                   book=book_title,
                                   quantity=quantity,
                                   address=shipping_address)

        except Exception as e:
            flash("An error occurred while processing your order.", "error")
            print(f"Error: {e}")  # Print detailed error for debugging
            return redirect(url_for('checkout'))

    books = Book.query.all()
    return render_template('checkout.html', books=books)

# Flask login loader
@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(int(user_id))

if __name__ == "__main__":
    app.run(debug=True)