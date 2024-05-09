#!/bin/bash

gcc -L/Users/david/Documents/Programming/png-reader/lib/ -I$(pwd)/include/ -g png.c -o png -lz

