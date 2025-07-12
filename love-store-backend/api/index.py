import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.main import app

# Export the Flask app for Vercel
handler = app 