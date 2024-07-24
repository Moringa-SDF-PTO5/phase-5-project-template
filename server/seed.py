from app import app, db
from models import User, Category, Product, Order, OrderItem, Address, Payment

def seed_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create sample users
        users = [
            User(username='admin', password='adminpassword', email='admin@example.com', role='admin'),
            User(username='customer1', password='customerpassword', email='customer1@example.com', role='customer'),
            User(username='customer2', password='customerpassword', email='customer2@example.com', role='customer')
        ]
        db.session.bulk_save_objects(users)
        db.session.commit()

        # Create sample categories
        categories = [
            
            Category(name='tablets', description='Versatile tablets for work and play.'),
            Category(name='headphones', description='Top quality headphones for the best sound experience.'),
            Category(name='cameras', description='High-resolution cameras for photography enthusiasts.'),
            Category(name='Laptops', description='High-performance laptops for all needs.'),
            Category(name='Smartphones', description='Latest smartphones with cutting-edge technology.'),
            Category(name='home appliances', description='different kinds of home appliances.')
           
        ]
        db.session.bulk_save_objects(categories)
        db.session.commit()

        # Create sample products
        products = [
            
            Product(name='Tablet Z3', image='https://m.media-amazon.com/images/I/51gj5oQXbnL._AC_UY327_FMwebp_QL65_.jpg', description='A versatile tablet for productivity and entertainment.', price=499.99, category_id=1, stock_quantity=75),
            Product(name='Headphones A4', image='https://m.media-amazon.com/images/I/61O7S27O+jL._AC_UY327_FMwebp_QL65_.jpg', description='Noise-cancelling headphones for a superior listening experience.', price=199.99, category_id=2, stock_quantity=150),
            Product(name='Camera B5', image='https://m.media-amazon.com/images/I/713rZRWpnPL._AC_UY327_FMwebp_QL65_.jpg', description='A high-resolution camera for capturing stunning photos.', price=1199.99, category_id=3, stock_quantity=30),
            Product(name='Hp Laptop', image='https://m.media-amazon.com/images/I/71CDSpds6jL._AC_UY327_FMwebp_QL65_.jpg', description='A powerful laptop with high-speed performance.', price=999.99, category_id=4, stock_quantity=50),
            Product(name='Moto G Smartphone', image='https://m.media-amazon.com/images/I/61K1Fz5LxvL._AC_UY327_FMwebp_QL65_.jpg', description='A sleek smartphone with the latest features.', price=799.99, category_id=5, stock_quantity=100),
             Product(name='Amazon Fire TV', image='https://m.media-amazon.com/images/I/71Nma1KADeL._AC_UY327_FMwebp_QL65_.jpg', description='high resolution smart TV', price=1009.99, category_id=6, stock_quantity=50)
            
        ]
        db.session.bulk_save_objects(products)
        db.session.commit()

        # Create sample orders
        orders = [
            Order(user_id=2, total_amount=1299.98, status='completed'),
            Order(user_id=3, total_amount=499.99, status='pending')
        ]
        db.session.bulk_save_objects(orders)
        db.session.commit()

        # Create sample order items
        order_items = [
            OrderItem(order_id=1, product_id=1, quantity=1, price=999.99),
            OrderItem(order_id=1, product_id=2, quantity=1, price=199.99),
            OrderItem(order_id=2, product_id=3, quantity=1, price=499.99)
        ]
        db.session.bulk_save_objects(order_items)
        db.session.commit()

        # Create sample addresses
        addresses = [
            Address(user_id=2, street='123 Main St', city='Anytown', state='CA', postal_code='12345', country='USA'),
            Address(user_id=3, street='456 Elm St', city='Othertown', state='TX', postal_code='67890', country='USA')
        ]
        db.session.bulk_save_objects(addresses)
        db.session.commit()

        # Create sample payments
        payments = [
            Payment(order_id=1, amount=1199.98, payment_method='Credit Card', transaction_id='tx1234567890'),
            Payment(order_id=2, amount=499.99, payment_method='PayPal', transaction_id='tx0987654321')
        ]
        db.session.bulk_save_objects(payments)
        db.session.commit()

        print("Database seeded with users, categories, products, orders, order items, addresses, and payments.")

if __name__ == "__main__":
    seed_database()
