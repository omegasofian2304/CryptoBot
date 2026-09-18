FROM debian:bookworm-slim

# Install C++ compiler, CMake, and the project's dependencies (hiredis, nlohmann-json) via apt
RUN apt-get update && apt-get install -y \
    g++ \
    cmake \
    pkg-config \
    libhiredis-dev \
    nlohmann-json3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the C++ project source into the container
COPY . .

# Configure and build the project with CMake
RUN cmake -B build -S . && cmake --build build

CMD ["./build/analysis_cpp"]