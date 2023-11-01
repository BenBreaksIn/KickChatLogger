# Kick Chat Logger

Kick Chat Logger is a Python script using Selenium to automate logging chat messages from a specified webpage into a text file. This tool continually monitors chat messages, capturing their senders’ usernames and timestamps, and saving this data in a `chat_log.txt` file.

## Prerequisites

Ensure the following components are installed:
- [Python](https://www.python.org/downloads/)
- [Selenium](https://selenium-python.readthedocs.io/installation.html)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/BenBreaksIn/KickChatLogger.git
   ```
2. Change directory into the cloned repository:
   ```bash
   cd KickChatLogger
   ```
3. Run the script:
   ```bash
   python chat_logger.py
   ```
   
   The chat messages will be logged into the `chat_log.txt` file in the same directory.

## Code Structure

- The script starts by initializing a set to keep track of processed messages and avoid duplications.
- A function `stream_chat()`:
  - Opens or creates `chat_log.txt` for storing logged messages.
  - Constantly checks for new messages in the chat.
  - Logs new messages with timestamps to both the console and the `chat_log.txt` file.
- Selenium WebDriver is employed to interact with the chat webpage.
- Main part of the script:
  - Initializes WebDriver.
  - Navigates to the specific chat page.
  - Begins the `stream_chat()` function to start monitoring and logging the messages.

## Customization

- Customize the URL by updating the `url` variable with the link to your preferred chat page.
- Sleep intervals within the script may be adjusted based on the webpage's responsiveness.

## Contribution

Contributions are welcomed! Feel free to fork the project, open a pull request, or submit issues and enhancement requests.

## Disclaimer

Ensure the use of this script complies with the terms of service of the website. Respect and uphold user privacy and ethical guidelines when using this tool.

