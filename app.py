import streamlit as st
import random
import string
import pyperclip

st.set_page_config(page_title="Password Generator", page_icon="🔐")

st.title("🔐 Password Generator")
st.markdown("Generate strong, random passwords instantly!")

# ---- Initialize session state ----
if "passwords" not in st.session_state:
    st.session_state.passwords = []

# ---- Character Set ----
chars = string.ascii_letters + string.digits + "!@#$%^&*().,?"

def generate_password(length):
    return ''.join(random.choice(chars) for _ in range(length))

def copy_to_clipboard(password):
    pyperclip.copy(password)
    st.success("✅ Password copied!")

# ---- UI ----
num_passwords = st.number_input("How many passwords?", min_value=1, max_value=20, value=5, step=1)
password_length = st.slider("Select password length", min_value=6, max_value=30, value=12)

if st.button("🚀 Generate Passwords"):
    st.session_state.passwords = [generate_password(password_length) for _ in range(num_passwords)]

# ---- Show Passwords ----
if st.session_state.passwords:
    st.subheader("🔑 Your Passwords:")
    for i, pwd in enumerate(st.session_state.passwords):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.code(pwd)
        with col2:
            if st.button(f"📋 Copy {i+1}", key=f"copy_{i}"):
                copy_to_clipboard(pwd)

# ---- Footer ----
st.markdown("---")
st.markdown("⚠️ Please store your passwords securely. Generated passwords are not saved.")
