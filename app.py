import streamlit as st
from database import get_database, add_customer, get_customer_by_mobile, add_product_to_customer
from pdf import generate_pdf

db = get_database()

st.title("Online Merch Grocery Store")

# Customer addition
with st.form("add_customer"):
    name = st.text_input("Customer Name")
    mobile = st.text_input("Mobile Number")
    submitted = st.form_submit_button("Add Customer")
    if submitted:
        add_customer(db, name, mobile)
        st.success("Customer Added")

# Product selection
products = {"salt": 1, "peanuts": 2, "Nirama": 3, "Mango": 4}
customer_mobile = st.text_input("Enter Customer Mobile to Add Products")

with st.form("add_products"):
    selected_product = st.selectbox("Select Product", list(products.keys()))
    add_product = st.form_submit_button("Add Product")
    if add_product:
        add_product_to_customer(db, customer_mobile, selected_product, products[selected_product])
        st.success("Product Added")

# PDF Generation
if st.button("Generate Bill"):
    customer = get_customer_by_mobile(db, customer_mobile)
    generate_pdf(customer)
    st.success("PDF Generated")
