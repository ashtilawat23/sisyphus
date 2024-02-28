# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents and the run_action.sh script into the container at /usr/src/app
COPY . .
COPY run_action.sh /usr/src/app

# Make run_action.sh executable
RUN chmod +x /usr/src/app/run_action.sh

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run run_action.sh when the container launches
ENTRYPOINT ["/usr/src/app/run_action.sh"]