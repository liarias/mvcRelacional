.PHONY:migration
migration:
	python manage.py makemigrations
	python manage.py migrate

.PHONY:runserver
runserver:
	python manage.py runserver

.PHONY:virtual
virtual:
	source myvenv/bin/activate
	
.PHONY:superuser
superuser:
	python manage.py createsuperuser