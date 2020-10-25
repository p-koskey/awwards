serve:
	python manage.py runserver

superuser:
	python manage.py createsuperuser --username $(name) 

migrate:
	python manage.py migrate

app:
	django-admin startapp $(name)

migrations:
	python manage.py makemigrations $(app)

check:
	python manage.py check

collectstatic:
	python manage.py collectstatic

test:
	python manage.py test $(app) 