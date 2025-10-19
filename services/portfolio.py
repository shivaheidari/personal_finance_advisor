import os
from dotenv import load_dotenv
from azure.cosmos import CosmosClient, exceptions

# Load environment variables
import os
from dotenv import load_dotenv
from azure.cosmos import CosmosClient, exceptions

class PortfolioService:
    def __init__(self):
        load_dotenv()
        self.endpoint = os.getenv("COSMOS_ENDPOINT")
        self.key = os.getenv("COSMOS_KEY")
        self.database_id = os.getenv("DATABASE_ID")
        self.container_id = os.getenv("CONTAINER_ID")
        self.client = CosmosClient(self.endpoint, self.key)
        self.database = self.client.get_database_client(self.database_id)
        self.container = self.database.get_container_client(self.container_id)

    def create_portfolio(self, portfolio_data):
        """Create a new portfolio document."""
        return self.container.create_item(body=portfolio_data)

    def get_portfolio(self, user_id):
        """Get all portfolios for a user."""
        query = "SELECT * FROM c WHERE c.user_id = @user_id"
        items = list(self.container.query_items(
            query=query,
            parameters=[{"name": "@user_id", "value": user_id}],
            enable_cross_partition_query=True
        ))
        return items

    def update_portfolio(self, portfolio_id, user_id, new_data):
        """Update an existing portfolio document."""
        try:
            item = self.container.read_item(item=portfolio_id, partition_key=user_id)
            item.update(new_data)
            return self.container.upsert_item(body=item)
        except exceptions.CosmosResourceNotFoundError:
            return None

    def delete_portfolio(self, portfolio_id, user_id):
        """Delete a portfolio document."""
        try:
            return self.container.delete_item(item=portfolio_id, partition_key=user_id)
        except exceptions.CosmosResourceNotFoundError:
            return None
