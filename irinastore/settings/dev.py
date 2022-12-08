from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-_a8e^k0!-t3rw51pa^r(mib!avfxiyv%chh6$1l4k9x+$r8a(5'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'irinastore2',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'lopaslopas'
    }
}