clean:
	rm -f example.sqlite

create_database:
	./manage.py makemigrations --noinput
	./manage.py migrate --noinput
	./manage.py createsuperuser --username=root --email=root@example.com --noinput

make_fixtures:
	./manage.py create_users
	./manage.py create_photos
	./manage.py create_departments
	./manage.py create_employees


all: clean create_database make_fixtures
