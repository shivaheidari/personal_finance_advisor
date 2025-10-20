import os
import sys
import json
import streamlit as st

# Ensure repository root is on sys.path so package imports work when Streamlit runs this file
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from services.portfolio import PortfolioService

service = PortfolioService()

st.title("Portfolio Manager")

# Read / Show Portfolio
user_id = st.text_input("Enter User ID to View Portfolio")
if st.button("Show Portfolio"):
    result = service.get_portfolio(user_id)
    if result:
        st.json(result)
    else:
        st.warning("No portfolio found for this user.")

st.markdown("---")

# Create Portfolio
st.subheader("Create Portfolio")
new_portfolio_json = st.text_area("Enter new portfolio JSON")
if st.button("Create Portfolio"):
    if new_portfolio_json:
        try:
            portfolio_data = json.loads(new_portfolio_json)
            created = service.create_portfolio(portfolio_data)
            st.success("Portfolio created successfully!")
        except Exception as e:
            st.error(f"Error creating portfolio: {str(e)}")
    else:
        st.error("Please enter portfolio JSON.")

st.markdown("---")

# Update Portfolio
st.subheader("Update Portfolio")
update_portfolio_id = st.text_input("Portfolio ID to Update")
update_user_id = st.text_input("User ID")
update_json = st.text_area("Enter updated fields JSON (partial)")
if st.button("Update Portfolio"):
    if update_portfolio_id and update_user_id and update_json:
        try:
            new_data = json.loads(update_json)
            updated = service.update_portfolio(update_portfolio_id, update_user_id, new_data)
            if updated:
                st.success("Portfolio updated successfully!")
            else:
                st.warning("Portfolio not found.")
        except Exception as e:
            st.error(f"Error updating portfolio: {str(e)}")
    else:
        st.error("Please fill all update fields.")

st.markdown("---")

# Delete Portfolio
st.subheader("Delete Portfolio")
delete_portfolio_id = st.text_input("Portfolio ID to Delete")
delete_user_id = st.text_input("User ID for Deletion")
if st.button("Delete Portfolio"):
    if delete_portfolio_id and delete_user_id:
        deleted = service.delete_portfolio(delete_portfolio_id, delete_user_id)
        if deleted:
            st.success("Portfolio deleted successfully!")
        else:
            st.warning("Portfolio not found.")
    else:
        st.error("Please enter portfolio ID and user ID.")

import os
import sys
import json
import streamlit as st

# Ensure repository root is on sys.path so package imports work when Streamlit runs this file
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from services.portfolio import PortfolioService
service = PortfolioService()

st.title("Portfolio Manager")

# Read / Show Portfolio
user_id = st.text_input("Enter User ID to View Portfolio")
if st.button("Show Portfolio"):
    result = service.get_portfolio(user_id)
    if result:
        st.json(result)
    else:
        st.warning("No portfolio found for this user.")

st.markdown("---")

# Create Portfolio
st.subheader("Create Portfolio")
new_portfolio_json = st.text_area("Enter new portfolio JSON")
if st.button("Create Portfolio"):
    if new_portfolio_json:
        try:
            portfolio_data = json.loads(new_portfolio_json)
            created = service.create_portfolio(portfolio_data)
            st.success("Portfolio created successfully!")
        except Exception as e:
            st.error(f"Error creating portfolio: {str(e)}")
    else:
        st.error("Please enter portfolio JSON.")
st.markdown("---")

# Update Portfolio
st.subheader("Update Portfolio")
update_portfolio_id = st.text_input("Portfolio ID to Update")
update_user_id = st.text_input("User ID")
update_json = st.text_area("Enter updated fields JSON (partial)")
if st.button("Update Portfolio"):
    if update_portfolio_id and update_user_id and update_json:
        try:
            new_data = json.loads(update_json)
            updated = service.update_portfolio(update_portfolio_id, update_user_id, new_data)
            if updated:
                st.success("Portfolio updated successfully!")
            else:
                st.warning("Portfolio not found.")
        except Exception as e:
            st.error(f"Error updating portfolio: {str(e)}")
    else:
        st.error("Please fill all update fields.")

st.markdown("---")

# Delete Portfolio
st.subheader("Delete Portfolio")
delete_portfolio_id = st.text_input("Portfolio ID to Delete")
delete_user_id = st.text_input("User ID for Deletion")
if st.button("Delete Portfolio"):
    if delete_portfolio_id and delete_user_id:
        deleted = service.delete_portfolio(delete_portfolio_id, delete_user_id)
        if deleted:
            st.success("Portfolio deleted successfully!")
        else:
            st.warning("Portfolio not found.")
    else:
        st.error("Please enter portfolio ID and user ID.")

