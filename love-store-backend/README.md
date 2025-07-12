# 💕 Tanishka's Love Store - From Manas with Love 💕

A beautiful, cute baby pink themed love store website created specially for Tanishka by Manas. This full-stack application features a React frontend with a Flask backend for email functionality.

## ✨ Features

- **Beautiful Baby Pink Theme**: Cute and romantic design with baby pink gradients and heart animations
- **8 Romantic Products**: Including unlimited hugs, premium cuddles, late-night talks, sweet kisses, morning texts, surprise dates, listening ears, and silly jokes
- **Shopping Cart Functionality**: Add items to cart and view them in a beautiful sidebar
- **Backend Email System**: Orders are sent via Flask backend API to manasxlevi@gmail.com
- **Environment Variables**: Email configuration using .env file
- **Mock Email Support**: Works without real SMTP credentials for testing
- **Responsive Design**: Works perfectly on both desktop and mobile devices
- **Cute Animations**: Heart animations, hover effects, and smooth transitions

## 🛍️ Products Available

1. **Unlimited Hugs** - ₹0 (Unlimited stock, Instant delivery)
2. **Premium Cuddles** - Free (Always Available, 1 click delivery)
3. **Late-Night Talks** - Priceless (Endless stock, Add to cart)
4. **Sweet Kisses** - Free (Infinite stock, On demand)
5. **Morning Texts** - ₹0 (365 days stock, Daily delivery)
6. **Surprise Dates** - Love (Monthly stock, Surprise timing)
7. **Listening Ears** - Free (Always available, 24/7 available)
8. **Silly Jokes** - Laughter (Unlimited stock, Random delivery)

## 🚀 How to Run

### Prerequisites
- Python 3.11+
- Node.js 20+
- npm or pnpm

### Backend Setup
1. Navigate to the project directory:
   ```bash
   cd love-store-backend
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables (optional for real email):
   ```bash
   # Edit .env file with your email credentials
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=your_app_password
   ```

5. Start the Flask server:
   ```bash
   python src/main.py
   ```

The application will be available at `http://localhost:5000`

### Frontend Development (Optional)
If you want to modify the frontend:

1. Navigate to the React project:
   ```bash
   cd ../tanishka-love-store
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   pnpm install
   ```

3. Start development server:
   ```bash
   npm run dev
   # or
   pnpm run dev
   ```

4. Build for production:
   ```bash
   npm run build
   # or
   pnpm run build
   ```

5. Copy built files to Flask static directory:
   ```bash
   cp -r dist/* ../love-store-backend/src/static/
   ```

## 📧 Email Configuration

### Mock Email Mode (Default)
By default, the application runs in mock email mode. Orders are logged to the console but not actually sent via email. This is perfect for testing and demonstration.

### Real Email Mode
To enable real email sending:

1. Edit the `.env` file:
   ```env
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USE_SSL=False
   MAIL_USERNAME=your_actual_email@gmail.com
   MAIL_PASSWORD=your_actual_app_password
   MAIL_DEFAULT_SENDER=your_actual_email@gmail.com
   RECIPIENT_EMAIL=manasxlevi@gmail.com
   SENDER_NAME=Tanishka's Love Store
   ```

2. For Gmail, you'll need to:
   - Enable 2-factor authentication
   - Generate an app password
   - Use the app password instead of your regular password

## 🎯 How Orders Work

1. **Add Items**: Browse the love products and click "Add to Cart"
2. **View Cart**: Click the cart button in the header to view selected items
3. **Send Order**: Click "Send Order to Manas 💕" to send the order
4. **Email Delivery**: Order details are sent to manasxlevi@gmail.com with:
   - Romantic subject line with date
   - All selected items with prices and delivery info
   - Total item count
   - Sweet message from Tanishka
   - Timestamp

## 🎨 Technology Stack

### Frontend
- **React 18** - Modern React with hooks
- **Vite** - Fast build tool and development server
- **Tailwind CSS** - Utility-first CSS framework
- **Shadcn/UI** - Beautiful UI components
- **Lucide Icons** - Beautiful icons
- **Framer Motion** - Smooth animations

### Backend
- **Flask** - Python web framework
- **Flask-Mail** - Email sending functionality
- **Flask-CORS** - Cross-origin resource sharing
- **Python-dotenv** - Environment variable management

## 📁 Project Structure

```
love-store-backend/
├── src/
│   ├── routes/
│   │   ├── user.py          # User management routes
│   │   └── email.py         # Email sending routes
│   ├── models/
│   │   └── user.py          # Database models
│   ├── static/              # Built React frontend files
│   │   ├── index.html
│   │   └── assets/
│   └── main.py              # Flask application entry point
├── venv/                    # Python virtual environment
├── .env                     # Environment variables
├── requirements.txt         # Python dependencies
└── README.md               # This file

tanishka-love-store/         # React frontend source
├── src/
│   ├── components/ui/       # UI components
│   ├── App.jsx             # Main React component
│   └── ...
├── dist/                   # Built frontend files
└── package.json           # Node.js dependencies
```

## 🔧 API Endpoints

### POST /api/send-order
Send a love order via email.

**Request Body:**
```json
{
  "cart_items": [
    {
      "name": "Unlimited Hugs",
      "price": "₹0",
      "delivery": "Instant delivery",
      "icon": "🤗",
      "category": "Physical Affection"
    }
  ]
}
```

**Response:**
```json
{
  "success": true,
  "message": "Order sent successfully! 💕",
  "email_status": "Email simulated (no SMTP credentials configured)",
  "order_details": {
    "items": [...],
    "total_items": 1,
    "sent_to": "manasxlevi@gmail.com",
    "timestamp": "2025-07-12 13:28:02",
    "subject": "💕 Love Order from Tanishka - 2025-07-12",
    "body": "Hi Manas! 💕\n\n..."
  }
}
```

### GET /api/test-email
Test email configuration.

## 💝 Special Features

- **Cute Emojis**: Each product has its own adorable emoji
- **Love Categories**: Products are categorized (Physical Affection, Emotional Connection, etc.)
- **Romantic Copy**: All text is written with love and care
- **Personal Touch**: Footer shows "Made with Love by Manas for Tanishka"
- **Heart Animations**: Pulsing hearts and sparkle effects
- **Responsive Cart**: Beautiful sidebar cart with smooth animations
- **Error Handling**: Graceful error handling for email failures

## 📱 Responsive Design

The website is fully responsive and works beautifully on:
- Desktop computers (1920px+)
- Laptops (1024px+)
- Tablets (768px+)
- Mobile phones (320px+)

## 🎯 Email Format

When an order is placed, the email includes:

**Subject:** `💕 Love Order from Tanishka - [Date]`

**Body:**
```
Hi Manas! 💕

I've placed an order at your Love Store:

Unlimited Hugs - ₹0 (Instant delivery)
Sweet Kisses - Free (On demand)

Total items: 2

Can't wait to receive all this love! 

With all my love,
Tanishka 💖

---
Order placed on: 2025-07-12 13:28:02
From: Tanishka's Love Store
```

## 🚀 Deployment

The application is ready for deployment. The Flask backend serves the built React frontend from the static directory, making it a complete full-stack application.

For production deployment:
1. Set up real email credentials in environment variables
2. Use a production WSGI server like Gunicorn
3. Configure a reverse proxy like Nginx
4. Set up SSL certificates for HTTPS

## 💕 Made with Love

This website was created with lots of love and care by Manas for his girlfriend Tanishka. Every detail was thoughtfully designed to bring smiles and joy.

**All orders will be delivered with extra love and care! 💕**

---

*For any issues or questions, the love store is always open! 💖*

