.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	cd ~/Documents/GitLabs/lab_2
	sudo -H pip3 install -U pipenv
	pipenv --python 3.6
	pipenv shell
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest

test:
	@echo "Start tests."
	pytest tests/tests.py > results.txt

run:
	@echo "Run Python app."
	python app.py >> results.txt

deploy:
	@echo "Adding and Committing results.txt to git."
	git add results.txt
	git commit -m "Lab2 commit file 'results.txt'"
	git push
