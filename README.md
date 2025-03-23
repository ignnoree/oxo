# How to Run the Telegram Bot

## Prerequisites
Before running the bot, make sure you have the following installed on your system:

- Python 3.8 or later
- `pip` (Python package manager)
- A Telegram bot API token from **BotFather**

## Getting the Bot API Token
1. Open Telegram and search for `BotFather`.
2. Start a chat and use the command `/newbot`.
3. Follow the instructions to create a bot and get the **API Token**.
4. Save this token as you will need to enter it when running the script.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   cd YOUR_REPOSITORY
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Bot

1. Start the bot script:
   ```bash
   python main.py
   ```
2. Enter your Telegram Bot API Token when prompted.
3. Now, you can send **Spotify playlists or single tracks** to the bot, and it will return MP3 files.

## Troubleshooting
- If you get missing module errors, run:
  ```bash
  pip install -r requirements.txt
  ```
- If the bot doesn’t respond, make sure it's not restricted in Telegram settings.
- If you face API errors, ensure you entered the correct Bot API Token.

## License
This project is open-source. Feel free to contribute!

