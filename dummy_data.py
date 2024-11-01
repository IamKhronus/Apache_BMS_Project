from app import app, db
from setup_database import Book, Customer, Employee, Admin

# Start app context to work with the database
with app.app_context():
    # Add dummy books to inventory
    books = [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 10.99, "stock": 10},
        {"title": "1984", "author": "George Orwell", "price": 8.99, "stock": 15},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 12.99, "stock": 20},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "price": 9.99, "stock": 12},
        {"title": "Moby Dick", "author": "Herman Melville", "price": 11.99, "stock": 8},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "price": 7.99, "stock": 9},
        {"title": "War and Peace", "author": "Leo Tolstoy", "price": 13.99, "stock": 6},
        {"title": "The Odyssey", "author": "Homer", "price": 10.99, "stock": 15},
        {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "price": 14.99, "stock": 4},
        {"title": "Great Expectations", "author": "Charles Dickens", "price": 9.99, "stock": 10},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "price": 8.99, "stock": 20},
        {"title": "Jane Eyre", "author": "Charlotte Bronte", "price": 7.99, "stock": 13},
        {"title": "The Divine Comedy", "author": "Dante Alighieri", "price": 12.99, "stock": 7},
        {"title": "Brave New World", "author": "Aldous Huxley", "price": 10.99, "stock": 18},
        {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "price": 9.99, "stock": 25},
        {"title": "The Iliad", "author": "Homer", "price": 11.99, "stock": 9},
        {"title": "Les Misérables", "author": "Victor Hugo", "price": 13.99, "stock": 5},
        {"title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll", "price": 6.99, "stock": 15},
        {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "price": 15.99, "stock": 8},
        {"title": "Anna Karenina", "author": "Leo Tolstoy", "price": 13.99, "stock": 7}
    ]

    # Only add books that do not already exist
    for book in books:
        if not Book.query.filter_by(title=book["title"], author=book["author"]).first():
            db.session.add(Book(**book))

    # Add dummy customers with login info
    customers = [
        {"first_name": "Alice", "last_name": "Johnson", "email": "alice@example.com", "username": "alice", "password": "password123"},
        {"first_name": "Bob", "last_name": "Smith", "email": "bob@example.com", "username": "bob", "password": "password123"},
        {"first_name": "Carol", "last_name": "White", "email": "carol@example.com", "username": "carol", "password": "password123"},
    ]

    # Only add customers that do not already exist
    for customer_data in customers:
        if not Customer.query.filter_by(username=customer_data["username"]).first():
            # Unpack customer_data directly
            new_customer = Customer(**customer_data)
            db.session.add(new_customer)

    # Add dummy employees with login info
    employees = [
    {"first_name": "John", "last_name": "Doe", "email": "johndoe@example.com", "role": "Manager", "username": "johndoe", "password": "password123"},
    {"first_name": "Jane", "last_name": "Roe", "email": "janeroe@example.com", "role": "Sales Associate", "username": "janeroe", "password": "password123"},
    {"first_name": "Richard", "last_name": "Roe", "email": "richardroe@example.com", "role": "Inventory Specialist", "username": "richardroe", "password": "password123"},
    {"first_name": "Donnie", "last_name": "Harris", "email": "donnieharris@example.com", "role": "Manager", "username": "donnieharris", "password": "password123"},
    {"first_name": "Yavo", "last_name": "Blaffo", "email": "yavoblaffo@example.com", "role": "Manager", "username": "yavoblaffo", "password": "password123"},
    {"first_name": "Tina", "last_name": "Ellington", "email": "tinaellington@example.com", "role": "Assistant Manager", "username": "tinaellington", "password": "password123"},
    {"first_name": "Aaron", "last_name": "Barnes", "email": "aaronbarnes@example.com", "role": "Assistant Manager", "username": "aaronbarnes", "password": "password123"},
    ]   

    # Only add employees that do not already exist
    for employee_data in employees:
        if not Employee.query.filter_by(username=employee_data["username"]).first():
            # Unpack employee_data directly
            new_employee = Employee(**employee_data)
            db.session.add(new_employee)

    # Add a dummy admin with login info if not already present
    if not Admin.query.filter_by(username="admin").first():
        db.session.add(Admin(username="admin", password="adminpass"))

    # Commit all changes to the database
    db.session.commit()

    print("New items added successfully.")
