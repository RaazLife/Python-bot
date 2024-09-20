import streamlit as st
import requests

# Your bot token (keep this secure)
TOKEN = '7356115926:AAHfeMgRew1m5I1gN42SClfoSKPB2Ds_jGE'  # Your actual bot token
CHAT_ID = '6357923154'  # Your chat ID

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
