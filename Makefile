ifeq ($(OS), Windows_NT)
try:
	python hi.py
try2:
	python main.py

else
install:
	pip install -r setup.txt

run_model:
	python main.py
	python interference.py
	
test:
	python app.py
		
all: install run_model test
endif