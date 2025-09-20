import streamlit as st
import json

ORDERS_FILE = "data/orders.json"

def save_order(order):
    try:
        with open(ORDERS_FILE, "r") as f:
            orders = json.load(f)
    except:
        orders = []
    orders.append(order)
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f, indent=2)

def show_cart():
    st.title("Shopping Cart")

    if not st.session_state.cart:
        st.info("Your cart is empty.")
        return

    total = 0
    for item in st.session_state.cart:
        p = item["product"]
        q = item["quantity"]
        st.write(f"{p['name']} x {q} = ${p['price']*q}")
        total += p['price']*q

    st.write(f"**Total:** ${total}")

    if st.button("Checkout"):
        order = {"items": st.session_state.cart, "total": total}
        save_order(order)
        st.session_state.cart = []
        st.success("Order placed successfully!")
