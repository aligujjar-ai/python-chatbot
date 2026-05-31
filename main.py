def show_help():
    print("""
Available Commands:
- /help  -> Show all commands
- /name  -> Show stored name
- /reset -> Erase stored name
- /exit  -> Exit chatbot
""")


def chatbot():
    name = None

    print("Welcome to Python Chatbot!")

    while True:
        msg = input("You: ").strip()

        if msg.startswith('/'):

            if msg == '/help':
                show_help()

            elif msg == '/name':
                if name:
                    print(f"Bot: Your name is {name}")
                else:
                    print("Bot: I don't know your name yet.")

            elif msg == '/reset':
                name = None
                print("Bot: Memory cleared.")

            elif msg == '/exit':
                print("Bot: Goodbye!")
                break

            else:
                print("Bot: Unknown command.")

        else:
            if msg.lower().startswith("my name is "):
                name = msg[11:].strip()
                print(f"Bot: Nice to meet you, {name}!")

            elif "hello" in msg.lower() or "hi" in msg.lower():
                print("Bot: Hello!")

            elif "how are you" in msg.lower():
                print("Bot: I'm doing great!")

            else:
                print("Bot: I don't understand that.")


chatbot()
