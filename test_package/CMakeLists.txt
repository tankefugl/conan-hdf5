cmake_minimum_required(VERSION 3.13)

project(test_package LANGUAGES CXX)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

find_package(HDF5 MODULE REQUIRED)

add_executable(${CMAKE_PROJECT_NAME} test_package.cpp)
target_link_libraries(${CMAKE_PROJECT_NAME} HDF5::HDF5)
