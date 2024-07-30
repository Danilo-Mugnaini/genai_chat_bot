import os

import google.generativeai as genai

#API KEY IMPORT
my_secret = os.environ['GENAI_API_KEY']
genai.configure(api_key=my_secret)

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'


def chatbot():
    print(
        "Welcome to Gemini Chatbot! Type 'exit' or 'quit' to end the conversation."
    )
    while True:
        user_input = input(f"{BLUE}Ask your question: {RESET}\n")

        if user_input.lower() in ['exit', 'quit']:
            print(f"{RED}Gemini: Goodbye!{RESET}")
            break

        response = chat.send_message(user_input)

        print(f"{RED}Gemini: {response.text}{RESET}\n")


if __name__ == "__main__":
    chatbot()
