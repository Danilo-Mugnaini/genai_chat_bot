# Gemini Chatbot

Welcome to the Gemini Chatbot project! This Python-based chatbot uses Google's Gemini API to interact with users in a conversational manner.

## Overview
The Gemini Chatbot allows you to have a text-based conversation with a chatbot powered by Google's Gemini-1.5 Flash model. You can ask questions and get responses directly from the chatbot.

## Features
- Conversational interaction with the Gemini-1.5 Flash model.
- User-friendly command-line interface.
- Exit the conversation by typing 'exit' or 'quit'.

## Installation
To run the Gemini Chatbot, follow these steps:
1. **Clone the repository:** ```bash git clone https://github.com/Danilo-Mugnaini/genai_chat_bot.git cd genai_chat_bot ```
2. **Create and activate a virtual environment (optional but recommended):** ```bash python -m venv venv source venv/bin/activate  # On Windows use `venv\Scripts\activate` ```
3. **Install the required packages:** Create a `requirements.txt` file with the following content: ```plaintext google-generativeai ``` Then run: ```bash pip install -r requirements.txt ```

4. **Set up your environment variables:** You need to set the `GENAI_API_KEY` environment variable with your Google Gemini API key. You can set this in your terminal like so: ```bash export GENAI_API_KEY='your_api_key_here'  # On Windows use `set GENAI_API_KEY=your_api_key_here` ```

## Usage
To start the chatbot, run the following command: ```bash python chatbot.py ```
You will see a welcome message and can start chatting with the bot. Type 'exit' or 'quit' to end the conversation.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please contact [Danilo Mugnaini](https://github.com/Danilo-Mugnaini).
