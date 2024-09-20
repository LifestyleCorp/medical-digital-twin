# backend/src/cpp_module/CMakeLists.txt

cmake_minimum_required(VERSION 3.10)
project(SimulationModule)

set(CMAKE_CXX_STANDARD 14)

add_library(simulation SHARED simulation.cpp)

target_include_directories(simulation PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
