import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# OpenAI Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4-turbo')
OPENAI_TEMPERATURE = float(os.getenv('OPENAI_TEMPERATURE', 0.7))
OPENAI_MAX_TOKENS = int(os.getenv('OPENAI_MAX_TOKENS', 2000))

# Application Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# Logging Configuration
LOGS_DIR = BASE_DIR / 'logs'
LOGS_DIR.mkdir(exist_ok=True)

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': LOG_LEVEL,
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': LOG_LEVEL,
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': LOGS_DIR / 'app.log',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'file'],
            'level': LOG_LEVEL,
            'propagate': True
        }
    }
}

# Validate OpenAI API Key
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in .env file")
