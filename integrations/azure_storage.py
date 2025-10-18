import os
from dotenv import load_dotenv
from azure.cosmos import CosmosClient

# Load environment variables from .env file
load_dotenv()

COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")
CONTAINER_ID = os.getenv("CONTAINER_ID")

# Connect to Cosmos DB
client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = client.get_database_client(DATABASE_ID)
container = database.get_container_client(CONTAINER_ID)

user_id = "Jafar"
for item in container.query_items(
    query = "select * from c where c.user_id = @user_id",
    parameters = [{"name": "@user_id", "value": user_id}]
    , enable_cross_partition_query = True):print(item)