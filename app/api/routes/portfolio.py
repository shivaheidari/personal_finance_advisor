from fastapi import APIRouter, HTTPException
from services.portfolio.portfolio import PortfolioService

router = APIRouter()
portfolio_service = PortfolioService()

@router.post("/")
def create_portfolio(portfolio: dict):
    result = portfolio_service.create_portfolio(portfolio)
    return result

@router.get("/{user_id}")
def get_portfolio(user_id: str):
    result = portfolio_service.get_portfolio(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return result

@router.put("/{portfolio_id}")
def update_portfolio(portfolio_id: str, user_id: str, new_data: dict):
    result = portfolio_service.update_portfolio(portfolio_id, user_id, new_data)
    if not result:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return result

@router.delete("/{portfolio_id}")
def delete_portfolio(portfolio_id: str, user_id: str):
    result = portfolio_service.delete_portfolio(portfolio_id, user_id)
    if not result:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return {"status": "deleted"}
