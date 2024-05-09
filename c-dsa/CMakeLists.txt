project(cdsa C)
cmake_minimum_required(VERSION 3.24)

add_library(map "${CMAKE_SOURCE_DIR}/map/map.c")
target_include_directories(map PUBLIC "${CMAKE_SOURCE_DIR}/map")

add_library(heap "${CMAKE_SOURCE_DIR}/heap/heap.c")
target_include_directories(heap PUBLIC "${CMAKE_SOURCE_DIR}/heap")

add_library(array "${CMAKE_SOURCE_DIR}/array/array.c")
target_include_directories(array PUBLIC "${CMAKE_SOURCE_DIR}/array")
