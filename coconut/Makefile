CC=gcc
OBJ=buffer/buffer.o io/io.o signal/signal.o term/term.o editor/editor.o graphics/graphics.o coconut.o

default: FLAGS=-Wall -g
optimized: FLAGS=-Ofast -Wall

%.o: %.c
	$(CC) $(FLAGS) -c $^ -o $@

default: $(OBJ) 
	$(CC) $(FLAGS) $(OBJ) -o coconut
	rm *.o **/*.o

optimized: all
	$(CC) $(FLAGS) $(OBJ) -o coconut
	rm *.o **/*.o


