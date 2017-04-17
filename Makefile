setup:
	pip install -r requirements.txt

run:
	python src/build.py

clean:
	find . -name '*.log' -delete
	find . -name 'config.dat' -delete