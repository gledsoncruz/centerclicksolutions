DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gsolucoes',
        'USER': 'gledson',
        'PASSWORD': 'gledson',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"