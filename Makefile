cov:
	coverage run --omit='manage.py' --source='.' manage.py test
	coverage html
	coverage report
