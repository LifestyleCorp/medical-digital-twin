# backend/Dockerfile

FROM python:3.8-slim

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential cmake

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . .

# Build C++ module
RUN mkdir build && cd build && cmake .. && make

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the application
CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]


# backend/Dockerfile

# Install COPASI dependencies
RUN apt-get update && apt-get install -y libxml2-dev libxslt1-dev

# Install COPASI (Assuming using COPASI binaries)
RUN wget https://github.com/copasi/copasi/releases/download/COPASI_4.29/COPASI-4.29-Linux-x86_64.tar.gz && \
    tar -xzvf COPASI-4.29-Linux-x86_64.tar.gz -C /opt && \
    ln -s /opt/copasi/bin/copasi-cli /usr/local/bin/copasi-cli
