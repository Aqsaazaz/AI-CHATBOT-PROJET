
print("================================")
print("       AI SMART CHATBOT")
print("================================")
print("Hello! Welcome to AI Smart Chatbot.")
print("Type 'bye' to exit the chatbot.")

while True:
    user = input("\nYou: ").lower()

    if user == "hello" or user == "hi":
        print("Chatbot: Hello! How can I help you?")

    elif user == "how are you":
        print("Chatbot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Chatbot: My name is AI Smart Chatbot.")

    elif user == "who created you":
        print("Chatbot: I was created using Python.")

    elif user == "what is python":
        print("Chatbot: Python is a programming language.")

    elif user == "what is ai":
        print("Chatbot: AI stands for Artificial Intelligence.")

    elif user == "what can you do":
        print("Chatbot: I can answer basic questions.")

    elif user == "thank you":
        print("Chatbot: You're welcome!")

    elif user == "bye":
        print("Chatbot: Goodbye! Have a nice day!")
        break

    else:
        print("Chatbot: Sorry, I don't understand your question.")
