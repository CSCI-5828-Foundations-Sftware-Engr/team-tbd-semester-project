FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the ports that the app is running on
EXPOSE 5000
EXPOSE 5001

# Start the app using Honcho
CMD ["honcho", "start"]
