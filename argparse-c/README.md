# argparse

argparse is a command line argument parsing library inspired by the Python argparse library.

Parsing command line arguments in C should not be hard!

## Installation

Building argparse from source is trivial. Run

```
make
```

in the root project directory. In the `build/` directory, you will find the static library file and header include.

## Getting Started

To use argparse, include `argparse.h` in your source file and initialize a `struct ArgumentParser`. You are free to allocate this struct on either the stack or the heap with `malloc()`. If you allocate on the heap, you are responsible for freeing this memory after you are finished with the struct, the library will not free it for you.

```c
#include <argparse.h>

int main(int argc, char **argv) {
    struct ArgumentParser parser;

}
```

Pass the address of the `ArgumentParser` struct into the `argparse_init (struct ArgumentParser *parser, int argc, char **argv)` method along with the `argc` and `argv` command line parameters.

```c
#include <argparse.h>

int main(int argc, char **argv) {
    struct ArgumentParser parser;
    argparse_init (&parser, argc, argv)
}
```

This initializes the `ArgumentParser` struct for use. To add command line arguments use the 

```c
int argparse_add_argument (struct ArgumentParser *parser,
                           const char *short_name,
                           const char *long_name,
                           int nargs,
                           enum ArgumentParserOptions action,
                           enum ArgumentParserOptions type,
                           char *help_text)
```
function. Let us break down these parameters

- `parser` - the `ArgumentParser` struct
- `short_name` - the flag's short name (short name flags can only have 1 character) eg. `-f`, `-c`. Pass `NULL` if no short name.
- `long_name` - the flag's long name eg. `--file`, `--copy`
- `nargs` - the number of arguments the flag expects, use 0 if no argument
- `action` - what should be done when this flag is specified
  - 


## Submodule Parser

## Examples
