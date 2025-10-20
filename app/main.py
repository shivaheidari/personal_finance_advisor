from fastapi import FastAPI
from app.api.routes import portfolio
app = FastAPI(
    title="My API",
    description="API for portfolio, advisor, alerts, and news services",
    version="1.0.0"
)
app.include_router(portfolio.router, prefix="/portfolio", tags=["portfolio"])
# app.include_router(advisor.router, prefix="/advisor", tags=["advisor"])
# app.include_router(alerts.router, prefix="/alerts", tags=["alerts"])
# app.include_router(news.router, prefix="/news", tags=["news"])

# Optional: a root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the API"}
