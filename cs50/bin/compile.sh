# run our cmake script
# -B build      tells cmake what our build directory will be named, in this case "build"
# -S .          tells cmake where our source directory is, in this case, our current directory
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -B build -S . CMakeLists.txt
cd build
make