from dotenv import load_dotenv
import os

# Load variables from .env into environment
load_dotenv(dotenv_path="solution.env")

# Access them
print("DB User:", os.getenv("DB_USER"))
print("DB Password:", os.getenv("DB_PASS"))
print("Debug Mode:", os.getenv("DEBUG"))
