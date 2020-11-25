INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps'
]

PROJECT_APPS = [
    'apps.core.apps.CoreConfig',
    'apps.main.apps.MainConfig'
]

EXTRA_APPS = [
    'django_cleanup.apps.CleanupConfig',
    'sorl.thumbnail',
    'ckeditor',
    'ckeditor_uploader',
    'robots',
    'snowpenguin.django.recaptcha3'
]

INSTALLED_APPS += PROJECT_APPS
INSTALLED_APPS += EXTRA_APPS

LOCAL_MIGRATIONS = [app_path.split('.')[1] for app_path in PROJECT_APPS]
MIGRATION_PATH = 'migrations.'
MIGRATION_MODULES = {app_name: MIGRATION_PATH + app_name for app_name in LOCAL_MIGRATIONS}
