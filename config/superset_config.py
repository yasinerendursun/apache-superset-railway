import os

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

ENABLE_PROXY_FIX = True

SECRET_KEY = os.environ.get("SECRET_KEY")

# Add Content Security Policy to allow images from all sources
CONTENT_SECURITY_POLICY = {
    "default-src": ["'self'"],
    "img-src": ["*"],  # Allow images from any domain
    "script-src": ["'self'", "'unsafe-inline'"],
    "style-src": ["'self'", "'unsafe-inline'"],
}