import streamlit as st
import random
import string

# ---- App Title ----
st.title("🔐 Password Generator")
st.markdown("Generate strong, random passwords instantly!")

# ---- UI Inputs ----
num_passwords = st.number_input("How many passwords?", min_value=1, max_value=20, value=5, step=1)
password_length = st.slider("Select password length", min_value=6, max_value=30, value=12)

# ---- Character Set ----
chars = string.ascii_letters + string.digits + "!@#$%^&*().,?"

# ---- Password Generation Logic ----
def generate_password(length):
    return ''.join(random.choice(chars) for _ in range(length))

# ---- Generate Button ----
if st.button("🚀 Generate Passwords"):
    st.subheader("🔑 Your Passwords:")
    for i in range(num_passwords):
        pwd = generate_password(password_length)
        with st.container():
            st.code(pwd, language='')  # just shows as formatted code
            st.text_input("Click to copy", value=pwd, key=f"text_{i}", label_visibility="collapsed")

# ---- Footer Note ----
st.markdown("---")
st.markdown("⚠️ Please store your passwords securely. Generated passwords are not saved.")
