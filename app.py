import streamlit as st
import pandas as pd
from project_code import clientsdb, purchases, goodsrev, raports


st.set_page_config(page_title="MAIG Warehouse", layout="wide")

st.title("🏭 MAIG Warehouse Management System")

menu = st.sidebar.radio("Navigation", ["Home", "Clients", "Purchases", "Reports", "Settings"])

if menu == "Home":
    st.write("Welcome to MAIG Warehouse — Streamlit Version")
    st.info("Use the sidebar to navigate between sections.")

elif menu == "Clients":
    st.subheader("Client Database")
    clients = clientsdb.get_all_clients() if hasattr(clientsdb, "get_all_clients") else []
    df = pd.DataFrame(clients)
    st.dataframe(df)

elif menu == "Purchases":
    st.subheader("Purchases & Transactions")
    if hasattr(purchases, "get_purchases"):
        data = purchases.get_purchases()
        st.dataframe(pd.DataFrame(data))
    else:
        st.warning("Function get_purchases() not found.")

elif menu == "Reports":
    st.subheader("Reports & Analysis")
    if hasattr(raports, "generate_report"):
        report = raports.generate_report()
        st.text(report)
    else:
        st.warning("No report generation function found.")

elif menu == "Settings":
    st.subheader("Application Settings")
    st.write("Modify configuration and user preferences.")