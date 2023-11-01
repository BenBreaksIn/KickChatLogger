
# Kick Chat Logger

Kick Chat Logger is a Python script utilizing Selenium to automate the process of logging chat messages from a specific webpage into a text file. The messages, along with their sender usernames and timestamps, are constantly monitored, logged, and saved in a `chat_log.txt` file.

## Prerequisites

Ensure you have the following installed:
- [Python](https://www.python.org/downloads/)
- [Selenium](https://selenium-python.readthedocs.io/installation.html)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ChatStreamLogger.git
   ```
2. Change directory into the cloned repository:
   ```bash
   cd ChatStreamLogger
   ```
3. Run the script:
   ```bash
   python chat_logger.py
   ```
   
   The chat messages will start logging into the `chat_log.txt` file in the same directory.

## Code Structure

- The script initializes a set to keep track of processed messages to avoid duplicates.
- It has a function `stream_chat()` that:
  - Opens `chat_log.txt` to store logged messages.
  - Continuously monitors for new messages in the chat.
  - Logs new messages with timestamps into the console and the `chat_log.txt` file.
- The script utilizes a Selenium WebDriver to interact with the chat webpage.
- The main part of the script:
  - Initializes the WebDriver.
  - Navigates to the chat page.
  - Starts the `stream_chat()` function to begin monitoring and logging messages.

## Customization

- You can customize the URL by modifying the `url` variable with the link to your specific chat page.
- Adjust sleep times in the script to better suit the responsiveness of the webpage you are interacting with.

## Contribution

Feel free to fork the project, open a pull request, or submit issues and enhancement requests.

## Disclaimer

Make sure to use this script in accordance with the terms of service of the website and respect user privacy.
