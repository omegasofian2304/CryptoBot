# Base image: Python 3.13
FROM python:3.13-slim

# Working directory inside the container
WORKDIR /app

# Copy requirements.txt first, to take advantage of Docker's build cache
COPY requirements.txt .

# Install Python dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Command executed when the container starts
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]