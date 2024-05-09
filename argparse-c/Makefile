
all: src/argparse.c src/argparse.h
	gcc -Wall -c src/argparse.c
	ar rcs libargparse.a argparse.o
	mkdir build
	mkdir build/lib
	mv libargparse.a build/lib
	mkdir build/include
	cp src/argparse.h build/include
	mkdir build/src
	cp src/argparse.c build/src


tests: src/argparse.c src/argparse.h

	gcc -I src/ -L build/lib tests/main.c -o main -largparse 

clean:
	rm -rf build
	rm -rf *.a *.o