# Environment Setup Guide

This guide explains how to set up environment variables for both the backend and frontend of your Tanishka Love Store project.

## Backend Environment Setup

### 1. Create `.env` file
Copy the example file and create your own `.env` file in the `love-store-backend/` directory:

```bash
cp love-store-backend/env.example love-store-backend/.env
```

### 2. Configure Backend Environment Variables

Edit `love-store-backend/.env` with your actual values:

```env
# Flask Configuration
SECRET_KEY=your-actual-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USE_SSL=False
MAIL_USERNAME=your-actual-email@gmail.com
MAIL_PASSWORD=your-actual-app-password
MAIL_DEFAULT_SENDER=your-actual-email@gmail.com

# Database Configuration
SQLALCHEMY_DATABASE_URI=sqlite:///app.db
SQLALCHEMY_TRACK_MODIFICATIONS=False

# Server Configuration
HOST=0.0.0.0
PORT=5000
```

### 3. Email Setup Instructions

For Gmail, you'll need to:
1. Enable 2-factor authentication on your Google account
2. Generate an App Password (not your regular password)
3. Use the App Password in the `MAIL_PASSWORD` field

## Frontend Environment Setup

### 1. Create `.env` file
Copy the example file and create your own `.env` file in the `tanishka-love-store/` directory:

```bash
cp tanishka-love-store/env.example tanishka-love-store/.env
```

### 2. Configure Frontend Environment Variables

Edit `tanishka-love-store/.env` with your actual values:

```env
# React App Configuration
VITE_APP_TITLE=Tanishka Love Store
VITE_APP_VERSION=1.0.0

# API Configuration
VITE_API_BASE_URL=http://localhost:5000/api
VITE_API_TIMEOUT=10000

# Feature Flags
VITE_ENABLE_ANALYTICS=false
VITE_ENABLE_DEBUG_MODE=true

# External Services (if needed)
VITE_GOOGLE_ANALYTICS_ID=
VITE_SENTRY_DSN=
```

## Important Notes

### Security
- **Never commit `.env` files to version control**
- Add `.env` to your `.gitignore` file
- Keep your secret keys and passwords secure

### Vite Environment Variables
- All frontend environment variables must be prefixed with `VITE_` to be accessible in the React app
- These variables will be embedded in the build, so don't include sensitive information

### Backend Environment Variables
- The Flask app uses `python-dotenv` to load environment variables
- Make sure to restart the Flask server after changing environment variables

## Usage in Code

### Backend (Python/Flask)
```python
import os
from dotenv import load_dotenv

load_dotenv()

# Access environment variables
mail_server = os.getenv('MAIL_SERVER')
secret_key = os.getenv('SECRET_KEY')
```

### Frontend (React/Vite)
```javascript
// Access environment variables
const apiUrl = import.meta.env.VITE_API_BASE_URL;
const appTitle = import.meta.env.VITE_APP_TITLE;
```

## Troubleshooting

1. **Environment variables not loading**: Make sure the `.env` file is in the correct directory
2. **Email not working**: Verify your Gmail app password is correct
3. **Frontend can't connect to backend**: Check that `VITE_API_BASE_URL` points to the correct backend URL
4. **Build errors**: Ensure all required environment variables are set

## Development vs Production

For production deployment:
- Use different environment variables for production
- Set `FLASK_ENV=production` and `FLASK_DEBUG=False`
- Use a proper secret key (not the default one)
- Configure production email settings
- Set appropriate API URLs for production 