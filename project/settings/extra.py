SITE_ID = 1

THUMBNAIL_PRESERVE_FORMAT = True

RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.8

DATA_UPLOAD_MAX_MEMORY_SIZE = 15*1024*1024
FILE_UPLOAD_PERMISSIONS = 0o644

TG_API_URL = 'https://api.telegram.org'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
PROJECTNAME = 'test'
