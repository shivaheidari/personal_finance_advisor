import os
import sys
import streamlit as st

# When Streamlit runs a script it doesn't always set the project root on sys.path.
# Add the repository root (two levels up from this file) to sys.path so imports
# like `from services.portfolio import PortfolioService` work.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from services.portfolio import PortfolioService

service = PortfolioService()

st.title("Portfolio Viewer")

user_id = st.text_input("Enter User ID")

if st.button("Show Portfolio"):
    result = service.get_portfolio(user_id)
    if result:
        st.json(result)
    else:
        st.warning("No portfolio found for this user.")
