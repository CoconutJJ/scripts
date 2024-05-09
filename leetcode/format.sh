#!/bin/sh
set -x
for f in **.py
do
    autopep8 --in-place $f
done