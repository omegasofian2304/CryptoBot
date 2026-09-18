cmake_minimum_required(VERSION 3.10)

project(AnalysisCpp)

set(CMAKE_CXX_STANDARD 17)

find_package(nlohmann_json CONFIG REQUIRED)

find_package(PkgConfig REQUIRED)
pkg_check_modules(HIREDIS REQUIRED hiredis)

add_executable(analysis_cpp src/main.cpp "src/candle.h" "src/dow_theory.h" "src/dow_theory.cpp" "src/redis_client.h" "src/redis_client.cpp")

target_include_directories(analysis_cpp PRIVATE ${HIREDIS_INCLUDE_DIRS})
target_link_libraries(analysis_cpp PRIVATE ${HIREDIS_LIBRARIES} nlohmann_json::nlohmann_json)