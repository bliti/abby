try:
    from development_settings import DEBUG
except ImportError:
    DEBUG = False


try:
    from development_settings import URLS
except ImportError:
    URLS = {
            'blog': 'http://blog.wutbot.com',
            'twitter': 'https://twitter.com/wutbot5000',
            'youtube': 'https://www.youtube.com/channel/UCOlSfiGQCT5_rmcxQDNygkg',
            'store': 'http://tindie.com' 
            }