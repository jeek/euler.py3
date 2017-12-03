all:	real

real:
	python3 euler.py

test:
	python3 -munittest -v euler.py

clean:
	rm -rf *~ __pycache__
  