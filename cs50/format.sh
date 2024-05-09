for f in $(find src -name \*.c); do
    clang-format -i $f
done
