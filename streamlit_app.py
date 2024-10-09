import streamlit as st
import asyncio
import threading
from telethon import TelegramClient, events

# Replace these with your own API details
api_id = '27142573'  # Your API ID
api_hash = '5186671fc6420391901f6092e9deb6d8'  # Your API Hash
phone_number = '+918459853169'  # Your phone number

client = None  # Global client variable

# Function to edit the message before forwarding
def edit_message(original_message):
    edited_message = f"🔥 Hot Deal! 🔥\n\n{original_message}"
    return edited_message

# Async Telegram bot function
async def run_telegram_bot():
    global client
    async with client:
        source_channel = 'Mobile_phone_offers_tv_ac_deals'  # Replace with your source channel
        target_channel = 'topdeals12345'  # Replace with your target channel

        @client.on(events.NewMessage(chats=source_channel))
        async def forward_message(event):
            original_message = event.message.message
            edited_message = edit_message(original_message)
            await client.send_message(target_channel, edited_message)

        await client.start(phone=phone_number)
        await client.run_until_disconnected()

# Function to initialize the Telegram client and start the bot in a thread
def start_bot():
    global client
    # Create the Telegram client inside the thread
    client = TelegramClient('session_name', api_id, api_hash)

    # Create a new event loop and set it as the current one
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    # Run the bot in the new event loop
    loop.run_until_complete(run_telegram_bot())

# Streamlit UI
st.title("🎈 My New App with Telegram Bot")
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
st.header("🔍 Telegram Bot")

# Start the bot in a separate thread
if st.session_state.get('bot_running') is not True:
    threading.Thread(target=start_bot, daemon=True).start()
    st.session_state['bot_running'] = True  # Flag to indicate the bot is running

st.write("Telegram bot is running and forwarding messages.")
