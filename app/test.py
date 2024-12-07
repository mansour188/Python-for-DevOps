import os
import requests

def main():
    api_url = os.getenv("API_URL", "https://default-api.com")
    log_level = os.getenv("LOG_LEVEL", "info")
    
    print(f"Using API URL: {api_url}")
    print(f"Log Level: {log_level}")
    
    response = requests.get(api_url)
    print(f"GitHub API Status: {response.status_code}")

if __name__ == "__main__":
    main()