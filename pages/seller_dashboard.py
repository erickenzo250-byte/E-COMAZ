import streamlit as st
import json

PRODUCTS_FILE = "data/products.json"

def load_products():
    with open(PRODUCTS_FILE, "r") as f:
        return json.load(f)

def save_products(products):
    with open(PRODUCTS_FILE, "w") as f:
        json.dump(products, f, indent=2)

def show_seller_dashboard():
    st.title("Seller Dashboard")
    products = load_products()

    st.subheader("Add New Product")
    name = st.text_input("Name")
    price = st.number_input("Price", min_value=1)
    desc = st.text_area("Description")
    if st.button("Add Product"):
        new_product = {"id": len(products)+1, "name": name, "price": price, "description": desc}
        products.append(new_product)
        save_products(products)
        st.success(f"Added {name}!")

    st.subheader("Existing Products")
    for p in products:
        st.write(f"{p['name']} - ${p['price']}")
