import streamlit as st
import os
import json
from faker import Faker
import random

PRODUCTS_FILE = "data/products.json"

# Generate random products if file doesn't exist or is empty
def generate_random_products(n=10):
    fake = Faker()
    products = []
    for i in range(1, n+1):
        products.append({
            "id": i,
            "name": fake.word().capitalize() + f" {i}",
            "price": random.randint(10, 500),
            "description": fake.sentence(),
            "image": f"https://picsum.photos/200?random={i}"
        })
    with open(PRODUCTS_FILE, "w") as f:
        json.dump(products, f, indent=2)
    return products

def load_products():
    if not os.path.exists(PRODUCTS_FILE):
        return generate_random_products()

    try:
        with open(PRODUCTS_FILE, "r") as f:
            data = f.read().strip()
            if not data:  # empty file
                return generate_random_products()
            return json.loads(data)
    except json.JSONDecodeError:
        return generate_random_products()

def show_home():
    st.title("Welcome to E-Commerce App")
    products = load_products()

    for p in products:
        st.subheader(p["name"])
        st.write(f"Price: ${p['price']}")
        st.write(p["description"])
        st.image(p["image"], width=150)
        if st.button(f"View {p['name']}", key=p["id"]):
            st.session_state.selected_product = p
            st.success(f"Selected {p['name']}")
