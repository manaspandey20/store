import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')

# Enable CORS for frontend-backend communication
CORS(app, origins=[os.getenv('CORS_ORIGINS', '*')])

# Email configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() == 'true'
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL', 'False').lower() == 'true'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/')
def home():
    return jsonify({
        "message": "Tanishka Love Store API", 
        "status": "running",
        "version": "1.0.0"
    })

@app.route('/api/health')
def health():
    return jsonify({
        "status": "healthy", 
        "message": "API is running",
        "timestamp": "2025-07-12T20:35:00Z"
    })

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        logger.info(f"Contact request received: {data}")
        
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        
        if not all([name, email, message]):
            logger.error("Missing required fields in contact form")
            return jsonify({"error": "Missing required fields"}), 400
        
        # Send email (if configured)
        if app.config['MAIL_USERNAME'] and app.config['MAIL_PASSWORD']:
            try:
                msg = Message(
                    subject=f"New Contact from {name}",
                    recipients=[app.config['MAIL_DEFAULT_SENDER']],
                    body=f"""
                    Name: {name}
                    Email: {email}
                    Message: {message}
                    """
                )
                mail.send(msg)
                logger.info("Contact email sent successfully")
            except Exception as e:
                logger.error(f"Email error: {e}")
                # Don't fail the request if email fails
                pass
        else:
            logger.warning("Email not configured - skipping email send")
        
        return jsonify({
            "success": True,
            "message": "Contact form submitted successfully"
        })
        
    except Exception as e:
        logger.error(f"Contact error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/order', methods=['POST'])
def order():
    try:
        data = request.get_json()
        logger.info(f"Order request received: {data}")
        
        # Extract order details
        customer_name = data.get('customerName', '')
        customer_email = data.get('customerEmail', '')
        customer_phone = data.get('customerPhone', '')
        items = data.get('items', [])
        total_amount = data.get('totalAmount', 0)
        shipping_address = data.get('shippingAddress', '')
        
        logger.info(f"Processing order for {customer_name} ({customer_email})")
        
        if not all([customer_name, customer_email, items]):
            logger.error("Missing required order fields")
            return jsonify({"error": "Missing required order fields"}), 400
        
        # Send order email (if configured)
        if app.config['MAIL_USERNAME'] and app.config['MAIL_PASSWORD']:
            try:
                # Create order details
                items_text = "\n".join([f"- {item.get('name', 'Unknown')}: ${item.get('price', 0)}" for item in items])
                
                msg = Message(
                    subject=f"New Order from {customer_name}",
                    recipients=[app.config['MAIL_DEFAULT_SENDER']],
                    body=f"""
                    New Order Received!
                    
                    Customer Details:
                    Name: {customer_name}
                    Email: {customer_email}
                    Phone: {customer_phone}
                    
                    Shipping Address:
                    {shipping_address}
                    
                    Order Items:
                    {items_text}
                    
                    Total Amount: ${total_amount}
                    
                    Order ID: {hash(f"{customer_name}{customer_email}") % 1000000}
                    """
                )
                mail.send(msg)
                logger.info("Order notification email sent to admin")
                
                # Send confirmation to customer
                customer_msg = Message(
                    subject="Order Confirmation - Tanishka Love Store",
                    recipients=[customer_email],
                    body=f"""
                    Dear {customer_name},
                    
                    Thank you for your order! We have received your order and will process it soon.
                    
                    Order Details:
                    {items_text}
                    
                    Total Amount: ${total_amount}
                    
                    We will contact you soon with shipping updates.
                    
                    Best regards,
                    Tanishka Love Store Team
                    """
                )
                mail.send(customer_msg)
                logger.info("Order confirmation email sent to customer")
                
            except Exception as e:
                logger.error(f"Email error: {e}")
                # Don't fail the order if email fails
                pass
        else:
            logger.warning("Email not configured - skipping email send")
        
        order_id = hash(f"{customer_name}{customer_email}") % 1000000
        logger.info(f"Order {order_id} processed successfully")
        
        return jsonify({
            "success": True,
            "message": "Order placed successfully",
            "orderId": order_id
        })
        
    except Exception as e:
        logger.error(f"Order error: {e}")
        return jsonify({"error": "Failed to send order. Please try again later."}), 500

@app.route('/api/orders', methods=['GET'])
def get_orders():
    # This would typically connect to a database
    # For now, return a mock response
    return jsonify({
        "orders": [],
        "message": "No orders found"
    })

@app.route('/api/test')
def test():
    return jsonify({
        "message": "API is working!",
        "endpoints": [
            "/api/health",
            "/api/contact",
            "/api/order",
            "/api/orders",
            "/api/test"
        ]
    })

# Export for Vercel
handler = app 