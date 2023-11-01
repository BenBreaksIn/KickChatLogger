from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# Set to keep track of processed message IDs
processed_message_ids = set()


# Function to stream and log chat messages
def stream_chat():
    with open("chat_log.txt", "a") as file:
        while True:
            try:
                # Wait for new chat messages to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#chatroom [data-chat-entry]'))
                )
                # Find all chat message elements
                chat_messages = driver.find_elements(By.CSS_SELECTOR, '#chatroom [data-chat-entry]')
                for message in chat_messages:
                    message_id = message.get_attribute('data-chat-entry')
                    if message_id not in processed_message_ids:  # Check if this message is a new message
                        try:
                            # Check if the .chat-entry-content element exists for this message
                            message_content_elements = message.find_elements(By.CSS_SELECTOR, '.chat-entry-content')
                            if message_content_elements:
                                # Extract username and message text
                                username = message.find_element(By.CSS_SELECTOR, '.chat-entry-username').text
                                message_text = message_content_elements[0].text
                                # Get the current timestamp
                                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                # Format and output to console and file
                                output = f"{timestamp} | {username}: {message_text}"
                                print(output)
                                file.write(f"{output}\n")
                                processed_message_ids.add(message_id)  # Mark this message as processed
                        except Exception as e:
                            print(f"Error processing message {message_id}: {e}")
                time.sleep(1)  # Optional: wait for a short interval before checking for new messages again
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(5)  # Wait for a longer interval if an error occurs


# Setup WebDriver for Chrome
driver = webdriver.Chrome()  # for Chrome

# Navigate to the chat page
url = "https://kick.com/username"
driver.get(url)

# Allow time for the page to load (adjust as needed)
time.sleep(5)

# Start streaming and logging chat
stream_chat()
