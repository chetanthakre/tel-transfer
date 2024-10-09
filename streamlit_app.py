import streamlit as st
import threading
import asyncio
from telethon import TelegramClient, events

# Streamlit UI
st.title("🎈 My New App with Telegram Bot")
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

st.header("🔍 Telegram Bot")

# Function to edit the message before forwarding
def edit_message(original_message):
    # Example modification: prepend a custom string
    edited_message = f"🔥 Hot Deal! 🔥\n\n{original_message}"
    return edited_message

# Async Telegram bot function
async def run_telegram_bot():
    # Replace with your API details from https://my.telegram.org
    api_id = '27142573'
    api_hash = '5186671fc6420391901f6092e9deb6d8'
    phone_number = '+918459853169'
    
    # Initialize the client
    client = TelegramClient('session_name', api_id, api_hash)

    # Monitor only the first source channel
    source_channel = 'Mobile_phone_offers_tv_ac_deals'  # Only the first channel

    @client.on(events.NewMessage(chats=source_channel))  # Listen for new messages in this source channel
    async def forward_message(event):
        target_channel = 'topdeals12345'  # Replace with your target channel username
        
        # Get the message text and edit it using the edit_message function
        original_message = event.message.message
        edited_message = edit_message(original_message)  # Call the separate function

        # Forward the edited message as a new message
        await client.send_message(target_channel, edited_message)

    # Start the client and keep it running
    await client.start(phone=phone_number)
    await client.run_until_disconnected()

# Function to start the Telegram bot asynchronously
def start_bot():
    asyncio.run(run_telegram_bot())

# Start the Telegram bot in a separate thread
threading.Thread(target=start_bot, daemon=True).start()

st.write("Telegram bot is running and forwarding messages.")
