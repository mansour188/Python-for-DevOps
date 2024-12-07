# My Python Envirement 

This project sets up a Python development environment using Docker and Docker Compose. It includes a sample script to demonstrate working with APIs and environment variables.

## Project Structure


```plaintext
my-python-project/
├── app/
│   ├── main.py               # Python script entry point
│   ├── requirements.txt      # Python dependencies
│   ├── Dockerfile            # Dockerfile for building the app image
├── docker-compose.yml        # Docker Compose configuration file
├── .env                      # Environment variables
└── README.md      


## Setup Instructions

### Prerequisites

- **Docker**: Install Docker from [Docker's official website](https://www.docker.com/get-started).
- **Docker Compose**: Install Docker Compose from [Docker Compose installation guide](https://docs.docker.com/compose/install/).

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone git@github.com:mansour188/Python-for-DevOps.git
cd Python-for-DevOps

### Step 2: Add Environment Variables
Create a .env file in the project root and define your variables:

To run a script, you should create it inside the app, update the SCRIPT_NAME variable with the name of the script file, and restart the environment.<.start.sh>

```bash
#.env file
API_URL=https://api.github.com
LOG_LEVEL=debug
SCRIPT_NAME=automate_files.py
```



### Step 3: Build and Run the envirement 
```bash
./start.sh
```

