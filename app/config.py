import os


class Config:
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/skinsdb")
