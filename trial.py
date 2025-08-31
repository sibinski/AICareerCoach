from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("API_KEY")

print("API Key:", api_key)
project_id = os.environ.get("PROJECT_ID")

print("PROJECT ID:", project_id)