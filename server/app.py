from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Product, Category, Order, OrderItem, Address, Payment
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://group2_electronics_project_3nds_user:W7lH5WhzPpazqIBxlTXxVs1rd9rPLwi2@dpg-cqh45tiju9rs73efvvig-a.frankfurt-postgres.render.com/group2_electronics_project_3nds'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

     # Configure CORS
    CORS(app, resources={r"/*": {"origins": "*"}})
    db.init_app(app)
    migrate = Migrate(app, db)
    return app

app=create_app()    

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Our Electronic Shop!"})

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"message": "Invalid JSON data"}), 400
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if not username or not email or not password:
            return jsonify({'message': 'Missing required fields'}), 400
        
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return jsonify({'message': 'User already exists'}), 409
        
        new_user = User(username=username, email=email, password=password)
    
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    user = User.query.filter_by(username=username).first()
    
    if user and user.check_password(password):
        return jsonify(user.to_dict()), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/categories', methods=['POST'])
def create_category():
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        
        if not name:
            return jsonify({'message': 'Category name is required'}), 400
        
        new_category = Category(name=name, description=description)
        db.session.add(new_category)
        db.session.commit()
        
        return jsonify(new_category.to_dict()), 201
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/categories', methods=['GET'])
def get_categories():
    try:
        categories = Category.query.all()
        return jsonify([category.to_dict() for category in categories]), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    try:
        category = Category.query.get_or_404(category_id)
        return jsonify(category.to_dict()), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    try:
        data = request.get_json()
        category = Category.query.get_or_404(category_id)
        
        name = data.get('name')
        description = data.get('description')
        
        if name:
            category.name = name
        if description is not None:
            category.description = description
        
        db.session.commit()
        
        return jsonify(category.to_dict()), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        category = Category.query.get_or_404(category_id)
        db.session.delete(category)
        db.session.commit()
        
        return jsonify({'message': 'Category deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = [product.to_dict() for product in products]
    return jsonify(result), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify(product.to_dict()), 200

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    image = data['image']
    description = data['description']
    price = data['price']
    category_id = data['category_id']
    stock_quantity = data['stock_quantity']
    
    new_product = Product(name=name, image=image, description=description, price=price, category_id=category_id, stock_quantity=stock_quantity)
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    if 'name' in data:
        product.name = data['name']
    if 'image' in data:
        product.image = data['image']
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        product.price = data['price']
    if 'category_id' in data:
        product.category_id = data['category_id']
    if 'stock_quantity' in data:
        product.stock_quantity = data['stock_quantity']
    
    db.session.commit()
    return jsonify(product.to_dict()), 200

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    result = [order.to_dict() for order in orders]
    return jsonify(result), 200

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    return jsonify(order.to_dict()), 200

@app.route('/orders', methods=['POST'])
def add_order():
    data = request.get_json()
    user_id = data['user_id']
    total_amount = data['total_amount']
    status = data.get('status', 'pending')
    
    new_order = Order(user_id=user_id, total_amount=total_amount, status=status)
    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order.to_dict()), 201

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    if 'user_id' in data:
        order.user_id = data['user_id']
    if 'total_amount' in data:
        order.total_amount = data['total_amount']
    if 'status' in data:
        order.status = data['status']
    
    db.session.commit()
    return jsonify(order.to_dict()), 200

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 200

@app.route('/order-items', methods=['GET'])
def get_order_items():
    order_items = OrderItem.query.all()
    result = [item.to_dict() for item in order_items]
    return jsonify(result), 200

@app.route('/order-items/<int:order_item_id>', methods=['GET'])
def get_order_item(order_item_id):
    order_item = OrderItem.query.get(order_item_id)
    if not order_item:
        return jsonify({'message': 'Order item not found'}), 404
    return jsonify(order_item.to_dict()), 200

@app.route('/order-items', methods=['POST'])
def add_order_item():
    data = request.get_json()
    order_id = data['order_id']
    product_id = data['product_id']
    quantity = data['quantity']
    price = data['price']
    
    new_order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=quantity, price=price)
    db.session.add(new_order_item)
    db.session.commit()
    return jsonify(new_order_item.to_dict()), 201

@app.route('/order-items/<int:order_item_id>', methods=['PUT'])
def update_order_item(order_item_id):
    data = request.get_json()
    order_item = OrderItem.query.get(order_item_id)
    if not order_item:
        return jsonify({'message': 'Order item not found'}), 404

    if 'order_id' in data:
        order_item.order_id = data['order_id']
    if 'product_id' in data:
        order_item.product_id = data['product_id']
    if 'quantity' in data:
        order_item.quantity = data['quantity']
    if 'price' in data:
        order_item.price = data['price']
    
    db.session.commit()
    return jsonify(order_item.to_dict()), 200

@app.route('/order-items/<int:order_item_id>', methods=['DELETE'])
def delete_order_item(order_item_id):
    order_item = OrderItem.query.get(order_item_id)
    if not order_item:
        return jsonify({'message': 'Order item not found'}), 404
    
    db.session.delete(order_item)
    db.session.commit()
    return jsonify({'message': 'Order item deleted successfully'}), 200

@app.route('/addresses', methods=['GET'])
def get_addresses():
    addresses = Address.query.all()
    result = [address.to_dict() for address in addresses]
    return jsonify(result), 200

@app.route('/addresses/<int:address_id>', methods=['GET'])
def get_address(address_id):
    address = Address.query.get(address_id)
    if not address:
        return jsonify({'message': 'Address not found'}), 404
    return jsonify(address.to_dict()), 200

@app.route('/addresses', methods=['POST'])
def add_address():
    data = request.get_json()
    user_id = data['user_id']
    street = data['street']
    city = data['city']
    state = data['state']
    postal_code = data['postal_code']
    country = data['country']
    
    new_address = Address(user_id=user_id, street=street, city=city, state=state, postal_code=postal_code, country=country)
    db.session.add(new_address)
    db.session.commit()
    return jsonify(new_address.to_dict()), 201

@app.route('/addresses/<int:address_id>', methods=['PUT'])
def update_address(address_id):
    data = request.get_json()
    address = Address.query.get(address_id)
    if not address:
        return jsonify({'message': 'Address not found'}), 404

    if 'user_id' in data:
        address.user_id = data['user_id']
    if 'street' in data:
        address.street = data['street']
    if 'city' in data:
        address.city = data['city']
    if 'state' in data:
        address.state = data['state']
    if 'postal_code' in data:
        address.postal_code = data['postal_code']
    if 'country' in data:
        address.country = data['country']
    
    db.session.commit()
    return jsonify(address.to_dict()), 200

@app.route('/addresses/<int:address_id>', methods=['DELETE'])
def delete_address(address_id):
    address = Address.query.get(address_id)
    if not address:
        return jsonify({'message': 'Address not found'}), 404
    
    db.session.delete(address)
    db.session.commit()
    return jsonify({'message': 'Address deleted successfully'}), 200

@app.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    result = [payment.to_dict() for payment in payments]
    return jsonify(result), 200

@app.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({'message': 'Payment not found'}), 404
    return jsonify(payment.to_dict()), 200

@app.route('/payments', methods=['POST'])
def add_payment():
    data = request.get_json()
    user_id = data['user_id']
    order_id = data['order_id']
    amount = data['amount']
    payment_method = data['payment_method']
    payment_date = data['payment_date']
    
    new_payment = Payment(user_id=user_id, order_id=order_id, amount=amount, payment_method=payment_method, payment_date=payment_date)
    db.session.add(new_payment)
    db.session.commit()
    return jsonify(new_payment.to_dict()), 201

@app.route('/payments/<int:payment_id>', methods=['PUT'])
def update_payment(payment_id):
    data = request.get_json()
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({'message': 'Payment not found'}), 404

    if 'user_id' in data:
        payment.user_id = data['user_id']
    if 'order_id' in data:
        payment.order_id = data['order_id']
    if 'amount' in data:
        payment.amount = data['amount']
    if 'payment_method' in data:
        payment.payment_method = data['payment_method']
    if 'payment_date' in data:
        payment.payment_date = data['payment_date']
    
    db.session.commit()
    return jsonify(payment.to_dict()), 200

@app.route('/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({'message': 'Payment not found'}), 404
    
    db.session.delete(payment)
    db.session.commit()
    return jsonify({'message': 'Payment deleted successfully'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)       