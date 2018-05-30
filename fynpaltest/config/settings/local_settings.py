from .base import *


DEBUG = True

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.postgresql_psycopg2",
		"NAME": "fynpaltest",
		"USER": "francisco",
		"PASSWORD": "12345",
		"HOST": "localhost",
		"PORT": "5432",
	}
}