# CMakeLists.txt for event package. It creates a library with dictionary and a main program
cmake_minimum_required(VERSION 2.8 FATAL_ERROR)
project(svfit)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_FLAGS "-fPIC -DDROP_CGAL -Wall -Wextra -Wpedantic -Wno-unused-variable -Wno-unused-parameter")

enable_testing()

add_subdirectory(src)
add_subdirectory(tests)
