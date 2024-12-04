import os

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

ENABLE_PROXY_FIX = True

SECRET_KEY = os.environ.get("SECRET_KEY")

# Override default Superset CSP settings
WTF_CSRF_ENABLED = True
CONTENT_SECURITY_POLICY = {}  # Empty dict to disable default CSP
TALISMAN_ENABLED = False  # Disable Talisman (Flask-Security wrapper)
CONTENT_SECURITY_POLICY_ENABLED = False  # Explicitly disable CSP

# If the above doesn't work, we provide a permissive CSP as fallback
if CONTENT_SECURITY_POLICY_ENABLED:
    CONTENT_SECURITY_POLICY = {
        "default-src": ["'*'", "'unsafe-inline'", "'unsafe-eval'"],
        "img-src": ["'*'", "data:", "blob:", "'self'"],
        "connect-src": ["'*'"],
        "script-src": ["'*'", "'unsafe-inline'", "'unsafe-eval'"],
        "style-src": ["'*'", "'unsafe-inline'"],
    }