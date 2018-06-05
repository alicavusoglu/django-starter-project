from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)

SECRET_KEY = env('DJANGO_SECRET_KEY', default='cjw(78uhyf93+*ca1rrdtu^1hzbai08)5f9*0-b(1by4u*=kk$')