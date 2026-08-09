cmake_minimum_required(VERSION 3.10)

set(CMAKE_TOOLCHAIN_FILE "C:/vcpkg/scripts/buildsystems/vcpkg.cmake" CACHE STRING "Vcpkg toolchain file")

project(AnalysisCpp)

set(CMAKE_CXX_STANDARD 17)

find_package(hiredis CONFIG REQUIRED)

add_executable(analysis_cpp src/main.cpp "src/candle.h" "src/dow_theory.h" "src/dow_theory.cpp" "src/redis_client.h" "src/redis_client.cpp")
target_link_libraries(analysis_cpp PRIVATE hiredis::hiredis)