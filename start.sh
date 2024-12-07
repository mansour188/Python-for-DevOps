#!/bin/bash

# Function to print messages in a formatted way
function print_message {
    echo -e "\n\033[1;32m$1\033[0m"  # Green color for messages
}

# Bring down any running containers
print_message "Stopping and removing containers..."
docker compose down

# Build the images
print_message "Building images..."
docker compose build

# Start the containers
print_message "Starting containers..."
docker compose up

# Inform the user that the process is complete
print_message "Process completed successfully!"