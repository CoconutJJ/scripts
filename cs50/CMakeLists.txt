# CS50 Solutions 

# In case you are wondering, this script configures all the code for building in
# the build/ directory

cmake_minimum_required(VERSION 3.24)
project (cs50 C)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# build all the problem set solutions
list (APPEND PSET_FILES caesar credit mario readability recover substitution tideman wordle bulbs)
foreach(f IN LISTS PSET_FILES)
    add_executable(${f} "${CMAKE_SOURCE_DIR}/src/psets/${f}/${f}.c")
    target_link_libraries(${f} "${CMAKE_SOURCE_DIR}/lib/libcs50.a") 
    target_include_directories(${f} PUBLIC "${CMAKE_SOURCE_DIR}/include")
    target_include_directories(${f} PUBLIC SYSTEM "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX14.0.sdk/usr/include")
endforeach()

# add the filter solution, this requires more than one C source file to link correctly
add_executable(filter "${CMAKE_SOURCE_DIR}/src/psets/filter-more/filter.c" "${CMAKE_SOURCE_DIR}/src/psets/filter-more/helpers.c")
target_link_libraries(filter "${CMAKE_SOURCE_DIR}/lib/libcs50.a")
target_link_libraries(filter m) # link math library (math.h)
target_include_directories(filter PUBLIC "${CMAKE_SOURCE_DIR}/filter-more")


add_executable(speller "${CMAKE_SOURCE_DIR}/src/psets/speller/speller.c" "${CMAKE_SOURCE_DIR}/src/psets/speller/dictionary.c")
target_link_libraries(speller "${CMAKE_SOURCE_DIR}/lib/libcs50.a")
target_include_directories(filter PUBLIC "${CMAKE_SOURCE_DIR}/include")


# build all lab solutions
list(APPEND LAB_FILES scrabble volume inheritance)
foreach(f IN LISTS LAB_FILES)
    add_executable(${f} "${CMAKE_SOURCE_DIR}/src/labs/${f}/${f}.c")
    target_link_libraries(${f} "${CMAKE_SOURCE_DIR}/lib/libcs50.a")
    target_include_directories(${f} PUBLIC "${CMAKE_SOURCE_DIR}/include")
endforeach()
