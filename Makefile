setup:
	pip install -r requirements.txt

run:
	python src/main.py

clean:
	find . -name '*.log' -delete
	find . -name 'config.dat' -delete