import os

# Superset specific config
ROW_LIMIT = 100000

# Flask App Builder configuration
# Your App secret key will be used for securely signing the session cookie
SECRET_KEY = os.environ.get('SUPERSET_SECRET_KEY', 'your_secret_key_here')

# The SQLAlchemy connection string to your database backend
# This connection string is for PostgreSQL metadata database
SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ.get('DATABASE_USER', 'superset')}:{os.environ.get('DATABASE_PASSWORD', 'superset')}@{os.environ.get('DATABASE_HOST', 'superset-db')}:5432/{os.environ.get('DATABASE_DB', 'superset')}"

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

SQLLAB_CTAS_NO_LIMIT = True

# SQL_MAX_ROW = None

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ""

# Enable feature flags
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "DYNAMIC_PLUGINS": True,
}

# Custom security manager to auto-register Presto database
class CustomSecurityManager:
    def __init__(self):
        pass

# Database configuration for Presto connection
DATABASE_CONNECTIONS = {
    'presto': {
        'engine': 'presto',
        'host': 'coordinator',
        'port': 8080,
        'username': 'admin',
        'catalog': 'tpch',
        'schema': 'sf10'
    }
}

# Allow embedding of Superset in iframes
HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}

# Cache configuration
CACHE_CONFIG = {
    'CACHE_TYPE': 'simple',
}

# Enable async queries
SUPERSET_ASYNC_QUERY_ENABLED = True

# Custom CSS
SUPERSET_CUSTOM_CSS = """
    .navbar-brand {
        font-weight: bold;
    }
"""

# Time zone
DEFAULT_TIMEZONE = "UTC"

# Log configuration
import logging
from logging.handlers import RotatingFileHandler

# Setup logging
LOG_DIR = '/app/logs'
try:
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR, exist_ok=True)
    
    file_handler = RotatingFileHandler(f'{LOG_DIR}/superset.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
except (OSError, PermissionError):
    # If we can't create log files, just use console logging
    pass

# Set log level
LOG_LEVEL = "INFO" 
