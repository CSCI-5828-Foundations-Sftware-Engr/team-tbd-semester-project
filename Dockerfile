FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code into the container
COPY . .

# Expose the necessary ports
EXPOSE 5000 5001

# Set the entrypoint command for the container
CMD ["docker-compose", "up"]