# Vercel Environment Variables Setup

To configure your backend API, add these environment variables in your Vercel dashboard:

## Required Environment Variables

### 1. Go to Vercel Dashboard
- Visit: https://vercel.com/dashboard
- Select your project: `store`

### 2. Add Environment Variables
Navigate to Settings > Environment Variables and add:

```
SECRET_KEY=your-super-secret-key-here
MAIL_USERNAME=manasxlevi@gmail.com
MAIL_PASSWORD=your-gmail-app-password
MAIL_DEFAULT_SENDER=manasxlevi@gmail.com
CORS_ORIGINS=https://store-q4m4jlgxh-manaspandey20s-projects.vercel.app
```

### 3. Email Setup Instructions
For Gmail:
1. Enable 2-factor authentication
2. Generate App Password (not regular password)
3. Use the App Password in MAIL_PASSWORD

### 4. Test API Endpoints
After deployment, test these endpoints:
- `GET /api/health` - Health check
- `GET /api/test` - Test endpoint
- `POST /api/contact` - Contact form

### 5. Frontend Integration
Update your frontend to use the deployed API:
```javascript
const API_BASE_URL = 'https://your-vercel-domain.vercel.app/api';
``` 