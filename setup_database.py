from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin  # Import UserMixin for Flask-Login integration

# Initialize the database object
db = SQLAlchemy()

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

# Define the Admin model (for login purposes)
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)  # For testing purposes only; hash passwords in production

# Define the Employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)  # New email field
    role = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

# Define the Customer model with UserMixin for Flask-Login
class Customer(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)  # Add first name
    last_name = db.Column(db.String(50), nullable=False)   # Add last name
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    shipping_address = db.Column(db.String(300), nullable=False)
    card_name = db.Column(db.String(100), nullable=False)
    card_number_last4 = db.Column(db.String(4), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)  # Foreign key to Customer model
    date_created = db.Column(db.DateTime, default=db.func.now())
