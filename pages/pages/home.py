import streamlit as st
import json

PRODUCTS_FILE = "data/products.json"

def load_products():
    with open(PRODUCTS_FILE, "r") as f:
        return json.load(f)

def show_home():
    st.title("Welcome to E-Commerce App")
    products = load_products()

    for p in products:
        st.subheader(p["name"])
        st.write(f"Price: ${p['price']}")
        st.write(p["description"])
        if st.button(f"View {p['name']}"):
            st.session_state.selected_product = p
            st.success(f"Selected {p['name']}")
