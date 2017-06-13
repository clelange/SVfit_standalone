# CMakeLists.txt for event package. It creates a library with dictionary and a main program
cmake_minimum_required(VERSION 2.8 FATAL_ERROR)
project(svfit)

# You need to tell CMake where to find the ROOT installation. This can be done in a number of ways:
#   - ROOT built with classic configure/make use the provided $ROOTSYS/etc/cmake/FindROOT.cmake
#   - ROOT built with CMake. Add in CMAKE_PREFIX_PATH the installation prefix for ROOT
list(APPEND CMAKE_PREFIX_PATH $ENV{ROOTSYS})

#---Locate the ROOT package and defines a number of variables (e.g. ROOT_INCLUDE_DIRS)
find_package(ROOT REQUIRED COMPONENTS MathCore RIO Hist Tree Net)

#---Define useful ROOT functions and macros (e.g. ROOT_GENERATE_DICTIONARY)
include(${ROOT_USE_FILE})

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/interface ${ROOT_INCLUDE_DIRS})
add_definitions(${ROOT_CXX_FLAGS})

#---Find files
file(GLOB sources *.cc)
file(GLOB headers ${CMAKE_CURRENT_SOURCE_DIR}/interface/*.h)

#---Generate dictionary
#---ROOT_GENERATE_DICTIONARY(SVfitStandaloneAlgorithm ${headers})
REFLEX_GENERATE_DICTIONARY(SVfitStandaloneAlgorithm ${headers} SELECTION selection.xml)
add_library(SVfitStandaloneAlgorithmDict SHARED SVfitStandaloneAlgorithm.cxx)
add_dependencies(SVfitStandaloneAlgorithmDict SVfitStandaloneAlgorithm-dictgen)
target_link_libraries(SVfitStandaloneAlgorithmDict SVfitStandaloneAlgorithm ${ROOT_LIBRARIES})
#install(TARGETS SVfitStandaloneAlgorithmDict DESTINATION lib)

#---Create a shared library with generated dictionary
add_library(SVfitStandaloneAlgorithm SHARED ${sources})
target_link_libraries(SVfitStandaloneAlgorithm ${ROOT_LIBRARIES})

#---Create  a main program using the library
#---add_executable(Main SVfitStandaloneAlgorithm.cc)
#---target_link_libraries(Main SVfitStandaloneAlgorithm)
