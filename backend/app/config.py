import os

class Config:
    API_URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/posts")
    DB_URL = os.getenv("DB_URL", "postgresql://user:password@localhost:5432/devopsdb")
    POLL_INTERVAL = int(os.getenv("POLL_INTERVAL", 5))