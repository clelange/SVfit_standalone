include(CTest)

add_test(NAME import-test COMMAND python tests/import-test.py
         WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
set_property(TEST import-test PROPERTY ENVIRONMENT LD_LIBRARY_PATH=${CMAKE_INSTALL_PREFIX}/lib:$ENV{LD_LIBRARY_PATH})

