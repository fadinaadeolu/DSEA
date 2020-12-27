help:
	echo "build: to build penguin_classification image"
	echo "run: deploy penguin_classification"
	
build:
	docker build -f Dockerfile -t penguin_classification:v1 .

run:
	docker run -p 8501:8501 penguin_classification:v1