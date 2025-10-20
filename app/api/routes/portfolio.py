from fastapi import FastAPI, HTTPException
from services.portfolio.portfolio import PortfolioService

app = FastAPI()
portfolio_service = PortfolioService()

@app.post("/portfolio/")
def create_portfolio(portfolio: dict):
    result = portfolio_service.create_portfolio(portfolio)
    return result

@app.get("/portfolio/{user_id}")
def get_portfolio(user_id: str):
    result = portfolio_service.get_portfolio(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return result

@app.put("/portfolio/{portfolio_id}")
def update_portfolio(portfolio_id: str, user_id: str, new_data: dict):
    result = portfolio_service.update_portfolio(portfolio_id, user_id, new_data)
    if not result:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return result

@app.delete("/portfolio/{portfolio_id}")
def delete_portfolio(portfolio_id: str, user_id: str):
    result = portfolio_service.delete_portfolio(portfolio_id, user_id)
    if not result:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return {"status": "deleted"}
