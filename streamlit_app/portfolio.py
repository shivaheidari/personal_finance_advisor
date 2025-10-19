import streamlit as st
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
