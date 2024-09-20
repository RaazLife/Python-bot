import streamlit as st
import requests
import os

# Set your bot token and chat ID here
TOKEN = os.getenv("BOT_TOKEN")  # Use environment variable for security
CHAT_ID = os.getenv("CHAT_ID")

st.title("Telegram Bot Interface")

user_message = st.text_input("Enter your message:")

if st.button("Send"):
    response = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": user_message}
    )
    if response.status_code == 200:
        st.success("Message sent!")
    else:
        st.error("Error sending message.")
