# justfile

dev:
	python main.py

freeze:
	rm requirements.txt || true
	pip freeze > requirements.txt