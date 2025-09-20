import streamlit as st

def show_product():
    if not st.session_state.selected_product:
        st.warning("Please select a product from Home first!")
        return

    product = st.session_state.selected_product
    st.title(f"{product['name']} Details")
    st.write(f"Price: ${product['price']}")
    st.write(product['description'])

    qty = st.number_input("Quantity", min_value=1, value=1)
    if st.button("Add to Cart"):
        st.session_state.cart.append({"product": product, "quantity": qty})
        st.success(f"Added {qty} x {product['name']} to cart")
