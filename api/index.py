import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        
        if not all([name, email, message]):
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
            except Exception as e:
                # Log error but don't fail the request
                print(f"Email error: {e}")
        
        return jsonify({
            "success": True,
            "message": "Contact form submitted successfully"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/test')
def test():
    return jsonify({
        "message": "API is working!",
        "endpoints": [
            "/api/health",
            "/api/contact",
            "/api/test"
        ]
    })

# Export for Vercel
handler = app 