from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class Recommendation:
    """Data class for a single recommendation"""
    action: str  # "Buy", "Sell", "Hold", "Rebalance"
    asset: str
    reason: str
    priority: str  # "High", "Medium", "Low"
    confidence_score: float


class RuleEngine:
    """
    Rule-based recommendation engine for portfolio analysis.
    Applies financial best practices and heuristics.
    """
    
    def __init__(self):
        self.recommendations = []
        
    def evaluate_portfolio(self, portfolio_data: Dict, user_profile: Dict) -> List[Recommendation]:
        """
        Main method to evaluate portfolio and generate recommendations.
        
        Args:
            portfolio_data: Dictionary with holdings, values, asset types
            user_profile: Dictionary with age, risk_tolerance, goals
            
        Returns:
            List of Recommendation objects
        """
        self.recommendations = []
        
        # Apply all rules
        self._check_diversification(portfolio_data)
        self._check_age_based_allocation(portfolio_data, user_profile)
        self._check_risk_alignment(portfolio_data, user_profile)
        self._check_sector_concentration(portfolio_data)
        self._check_cash_buffer(portfolio_data)
        
        return self.recommendations
    
    def _check_diversification(self, portfolio_data: Dict):
        """Rule: Don't put more than 60% in one asset class"""
        total_value = portfolio_data.get("total_value", 1)
        
        for asset_class, value in portfolio_data.get("asset_classes", {}).items():
            ratio = value / total_value
            
            if ratio > 0.60:
                self.recommendations.append(Recommendation(
                    action="Rebalance",
                    asset=asset_class,
                    reason=f"{asset_class} represents {ratio*100:.1f}% of portfolio. Reduce to improve diversification.",
                    priority="High",
                    confidence_score=0.85
                ))
    
    def _check_age_based_allocation(self, portfolio_data: Dict, user_profile: Dict):
        """Rule of 110: Stock allocation = 110 - age"""
        age = user_profile.get("age", 40)
        target_stock_ratio = (110 - age) / 100
        
        total_value = portfolio_data.get("total_value", 1)
        stock_value = portfolio_data.get("asset_classes", {}).get("stocks", 0)
        current_stock_ratio = stock_value / total_value
        
        difference = abs(current_stock_ratio - target_stock_ratio)
        
        if difference > 0.10:  # More than 10% off target
            if current_stock_ratio > target_stock_ratio:
                action = "Sell"
                asset = "stocks"
                reason = f"Stock allocation ({current_stock_ratio*100:.1f}%) is above age-appropriate target ({target_stock_ratio*100:.1f}%). Consider reducing exposure."
            else:
                action = "Buy"
                asset = "stocks"
                reason = f"Stock allocation ({current_stock_ratio*100:.1f}%) is below age-appropriate target ({target_stock_ratio*100:.1f}%). Consider increasing exposure."
            
            self.recommendations.append(Recommendation(
                action=action,
                asset=asset,
                reason=reason,
                priority="Medium",
                confidence_score=0.75
            ))
    
    def _check_risk_alignment(self, portfolio_data: Dict, user_profile: Dict):
        """Ensure portfolio risk matches user's risk tolerance"""
        risk_tolerance = user_profile.get("risk_tolerance", "moderate").lower()
        portfolio_volatility = portfolio_data.get("volatility", 0.15)
        
        risk_thresholds = {
            "conservative": 0.10,
            "moderate": 0.15,
            "aggressive": 0.25
        }
        
        max_volatility = risk_thresholds.get(risk_tolerance, 0.15)
        
        if portfolio_volatility > max_volatility:
            self.recommendations.append(Recommendation(
                action="Rebalance",
                asset="high-volatility assets",
                reason=f"Portfolio volatility ({portfolio_volatility*100:.1f}%) exceeds {risk_tolerance} risk tolerance. Consider safer assets like bonds.",
                priority="High",
                confidence_score=0.80
            ))
    
    def _check_sector_concentration(self, portfolio_data: Dict):
        """Rule: No single sector should exceed 30% of portfolio"""
        total_value = portfolio_data.get("total_value", 1)
        
        for sector, value in portfolio_data.get("sectors", {}).items():
            ratio = value / total_value
            
            if ratio > 0.30:
                self.recommendations.append(Recommendation(
                    action="Sell",
                    asset=f"{sector} sector",
                    reason=f"{sector} sector represents {ratio*100:.1f}% of portfolio. Reduce to minimize sector risk.",
                    priority="Medium",
                    confidence_score=0.70
                ))
    
    def _check_cash_buffer(self, portfolio_data: Dict):
        """Rule: Maintain 5-10% cash buffer"""
        total_value = portfolio_data.get("total_value", 1)
        cash_value = portfolio_data.get("asset_classes", {}).get("cash", 0)
        cash_ratio = cash_value / total_value
        
        if cash_ratio < 0.05:
            self.recommendations.append(Recommendation(
                action="Sell",
                asset="assets to create cash buffer",
                reason=f"Cash buffer ({cash_ratio*100:.1f}%) is below recommended 5-10%. Consider liquidating some assets.",
                priority="Low",
                confidence_score=0.65
            ))
        elif cash_ratio > 0.15:
            self.recommendations.append(Recommendation(
                action="Buy",
                asset="income-generating assets",
                reason=f"Cash holdings ({cash_ratio*100:.1f}%) are high. Consider investing excess cash.",
                priority="Low",
                confidence_score=0.60
            ))
