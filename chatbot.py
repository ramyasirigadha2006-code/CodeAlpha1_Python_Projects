
print("Welcome to My Chatbot!")

print("You can chat with me.")
print("Type 'bye' to exit.")

while True:
    message = input("\nYou: ").lower()

    if message == "hello":
        print("Bot: Hey! Nice to meet you.")

    elif message == "how are you":
        print("Bot: I'm doing good. How about you?")

    elif message == "what is your name":
        print("Bot: I'm your Python chatbot.")

    elif message == "what can you do":
        print("Bot: I can answer a few simple questions.")

    elif message == "bye":
        print("Bot: Bye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't know that. Try something else.")

