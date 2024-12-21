SECRET_KEY = 'django-insecure-secret-key'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ['cart', 'products', 'django.contrib.admin', 'django.contrib.auth', 
    'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 
    'django.contrib.staticfiles']
ROOT_URLCONF = 'django_ecommerce_project.urls'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'db.sqlite3'}}
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['templates'], 'APP_DIRS': True, 'OPTIONS': {'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'django_ecommerce_project.wsgi.application'
STATIC_URL = 'static/'