from fastapi import FastAPI
from pymongo import AsyncMongoClient
from dotenv import dotenv_values
from contextlib import asynccontextmanager

config = dotenv_values(".env")

mongodb_client: AsyncMongoClient = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global mongodb_client
    # Connect to the database
    mongodb_client = AsyncMongoClient(
        host=config["DB_HOST"],
        port=int(config["DB_PORT"]),
        username=config["DB_USER"],
        password=config["DB_PASSWORD"],
        authSource=config["AUTH_DB"],
    )
    print(f"✅ Connection to MongoDB on {config['DB_HOST']} successful!")
    yield
    # Clean up the resources
    if mongodb_client:
        await mongodb_client.close()
        print(f"✅ Connection to MongoDB on {config['DB_HOST']} successfully closed!")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    # This is just an example, you would perform async operations here
    # e.g., user_count = await mongodb_client[config["DB_NAME"]]["user"].count_documents({})
    return {"message": "Welcome to the PyMongo tutorial!"}
