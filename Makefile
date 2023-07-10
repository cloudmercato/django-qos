install:
	pip install -r requirements.txt

test_install:
	pip install -r requirements-tests.txt

test:
	./runtests.py

coverage:
	coverage runtests.py
	coverage report
