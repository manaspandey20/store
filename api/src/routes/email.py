from flask import Blueprint, jsonify, request
from flask_mail import Mail, Message
from datetime import datetime
import os

email_bp = Blueprint('email', __name__)

def init_mail(app):
    """Initialize Flask-Mail with the app"""
    mail = Mail(app)
    return mail

@email_bp.route('/send-order', methods=['POST'])
def send_order():
    try:
        data = request.json
        cart_items = data.get('cart_items', [])
        
        if not cart_items:
            return jsonify({'error': 'Cart is empty'}), 400
        
        # Get configuration
        recipient_email = os.getenv('RECIPIENT_EMAIL', 'manasxlevi@gmail.com')
        sender_name = os.getenv('SENDER_NAME', "Tanishka's Love Store")
        
        # Create order details
        order_details = []
        for item in cart_items:
            order_details.append(f"{item.get('name', 'Unknown')} - {item.get('price', 'Free')} ({item.get('delivery', 'Standard delivery')})")
        
        order_text = '\n'.join(order_details)
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        # Email subject and body
        subject = f"💕 Love Order from Tanishka - {current_date}"
        
        body = f"""Hi Manas! 💕

I've placed an order at your Love Store:

{order_text}

Total items: {len(cart_items)}

Can't wait to receive all this love! 

With all my love,
Tanishka 💖

---
Order placed on: {current_time}
From: {sender_name}"""
        
        # Mock email sending (for demonstration purposes)
        # In production, you would configure real email credentials
        email_configured = (os.getenv('MAIL_USERNAME') and 
                           os.getenv('MAIL_PASSWORD') and 
                           os.getenv('MAIL_USERNAME') != 'your_email@gmail.com' and
                           os.getenv('MAIL_PASSWORD') != 'your_app_password')
        
        if email_configured:
            # Try to send real email
            from flask import current_app
            mail = current_app.extensions.get('mail')
            
            if mail:
                msg = Message(
                    subject=subject,
                    recipients=[recipient_email],
                    body=body
                )
                mail.send(msg)
                email_status = "Email sent successfully via SMTP"
            else:
                email_status = "Email service not configured"
        else:
            # Mock email sending for demonstration
            email_status = "Email simulated (no SMTP credentials configured)"
            
            # Log the email content for demonstration
            print(f"\n{'='*50}")
            print("MOCK EMAIL SENT:")
            print(f"To: {recipient_email}")
            print(f"Subject: {subject}")
            print(f"Body:\n{body}")
            print(f"{'='*50}\n")
        
        return jsonify({
            'success': True,
            'message': 'Order sent successfully! 💕',
            'email_status': email_status,
            'order_details': {
                'items': cart_items,
                'total_items': len(cart_items),
                'sent_to': recipient_email,
                'timestamp': current_time,
                'subject': subject,
                'body': body
            }
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': f'Failed to send order: {str(e)}'
        }), 500

@email_bp.route('/test-email', methods=['GET'])
def test_email():
    """Test endpoint to check if email configuration is working"""
    try:
        recipient_email = os.getenv('RECIPIENT_EMAIL', 'manasxlevi@gmail.com')
        email_configured = os.getenv('MAIL_USERNAME') and os.getenv('MAIL_PASSWORD')
        
        if email_configured:
            from flask import current_app
            mail = current_app.extensions.get('mail')
            
            if not mail:
                return jsonify({'error': 'Email service not configured'}), 500
            
            msg = Message(
                subject="💕 Love Store Email Test",
                recipients=[recipient_email],
                body="This is a test email from Tanishka's Love Store! If you receive this, the email configuration is working correctly. 💖"
            )
            
            mail.send(msg)
            
            return jsonify({
                'success': True,
                'message': 'Test email sent successfully!',
                'sent_to': recipient_email
            }), 200
        else:
            return jsonify({
                'success': True,
                'message': 'Email service is in mock mode (no SMTP credentials configured)',
                'note': 'To enable real email sending, configure MAIL_USERNAME and MAIL_PASSWORD in .env file',
                'recipient': recipient_email
            }), 200
        
    except Exception as e:
        return jsonify({
            'error': f'Email test failed: {str(e)}'
        }), 500

