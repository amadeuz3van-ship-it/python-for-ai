import os
from dotenv import load_dotenv

os.getcwd()  # Get the current working directory

load_dotenv()# Load environment variables from .env file

# Read from environment
api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_NAME')

print(f"Using API key: {api_key}")
print(f"Using database: {database}")
