import random
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"how are you",
        ["I'm good, thanks for asking! How about you?", "Doing well, thank you!"]
    ],
    [
        r"what is your name",
        ["I'm a simple AI chatbot! I don't have a name yet."]
    ],
    [
        r"quit",
        ["Goodbye! Take care.", "See you later!", "It was nice talking with you."]
    ]
]

chatbot = Chat(pairs, reflections)


def start_chat():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break

        response = chatbot.respond(user_input)
        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I didn't quite understand that. Could you try again?")


# Run the chatbot
if __name__ == "__main__":
    start_chat()
