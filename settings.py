try:
    from development_settings import DEBUG
except ImportError:
    DEBUG = False


try:
    from development_settings import URLS
except ImportError:
    URLS = {}