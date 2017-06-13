include(CTest)

add_test(NAME run-test COMMAND python tests/svFitTest.py
         WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
set_property(TEST run-test PROPERTY ENVIRONMENT LD_LIBRARY_PATH=${PROJECT_BINARY_DIR}/src:$ENV{LD_LIBRARY_PATH})
