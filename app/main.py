from fastapi import FastAPI
from .api.routes import portfolio

app = FastAPI(
    title="My API",
    description="API for portfolio, advisor, alerts, and news services",
    version="1.0.0"
)
app.include_router(portfolio.router, prefix="/portfolio", tags=["portfolio"])
# app.include_router(advisor.router, prefix="/advisor", tags=["advisor"])
# app.include_router(alerts.router, prefix="/alerts", tags=["alerts"])
# app.include_router(news.router, prefix="/news", tags=["news"])


@app.get("/")
def root():
    return {"message": "Welcome to the API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)


"""

uvicorn app.main:app --reload
# or
python -m app.main

"""