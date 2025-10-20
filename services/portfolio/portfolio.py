import os
from dotenv import load_dotenv

try:
    from azure.cosmos import CosmosClient, exceptions  # type: ignore
except Exception:
    CosmosClient = None
    exceptions = None


class PortfolioService:
    """Portfolio service with an optional dev fallback.

    If COSMOS_ENDPOINT/COSMOS_KEY are set (and azure-cosmos is installed)
    the service will use Cosmos DB. Otherwise it falls back to a small
    in-memory store which is convenient for local dev and tests.
    """

    def __init__(self):
        load_dotenv()
        self.endpoint = os.getenv("COSMOS_ENDPOINT")
        self.key = os.getenv("COSMOS_KEY")
        self.database_id = os.getenv("DATABASE_ID")
        self.container_id = os.getenv("CONTAINER_ID")
        self.dev_fallback = os.getenv("PFA_DEV_FALLBACK", "0") == "1"

        if self.endpoint and self.key and CosmosClient and not self.dev_fallback:
            # Initialize Cosmos client
            self.client = CosmosClient(self.endpoint, self.key)
            self.database = self.client.get_database_client(self.database_id)
            self.container = self.database.get_container_client(self.container_id)
            self._mode = "cosmos"
        else:
            # In-memory fallback store: dict[user_id] -> list[portfolio]
            self._store = {}
            self._mode = "mock"

    # --- CRUD operations ---
    def create_portfolio(self, portfolio_data):
        """Create a new portfolio document."""
        if self._mode == "cosmos":
            return self.container.create_item(body=portfolio_data)
        else:
            user_id = portfolio_data.get("user_id") or portfolio_data.get("userId")
            if not user_id:
                raise ValueError("portfolio_data must include user_id")
            self._store.setdefault(user_id, []).append(portfolio_data)
            return portfolio_data

    def get_portfolio(self, user_id):
        """Get all portfolios for a user."""
        if self._mode == "cosmos":
            query = "SELECT * FROM c WHERE c.user_id = @user_id"
            items = list(self.container.query_items(
                query=query,
                parameters=[{"name": "@user_id", "value": user_id}],
                enable_cross_partition_query=True
            ))
            return items
        else:
            return list(self._store.get(user_id, []))

    def update_portfolio(self, portfolio_id, user_id, new_data):
        """Update an existing portfolio document."""
        if self._mode == "cosmos":
            try:
                item = self.container.read_item(item=portfolio_id, partition_key=user_id)
                item.update(new_data)
                return self.container.upsert_item(body=item)
            except Exception:
                return None
        else:
            items = self._store.get(user_id, [])
            for i, it in enumerate(items):
                if it.get("id") == portfolio_id or it.get("portfolio_id") == portfolio_id:
                    items[i].update(new_data)
                    return items[i]
            return None

    def delete_portfolio(self, portfolio_id, user_id):
        """Delete a portfolio document."""
        if self._mode == "cosmos":
            try:
                return self.container.delete_item(item=portfolio_id, partition_key=user_id)
            except Exception:
                return None
        else:
            items = self._store.get(user_id, [])
            for i, it in enumerate(items):
                if it.get("id") == portfolio_id or it.get("portfolio_id") == portfolio_id:
                    return items.pop(i)
            return None
