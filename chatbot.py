def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        return "Hello! Welcome to our store 😊 How can I help you?"

    # Order tracking
    elif "track order" in user_input:
        return "Sure! Please provide your order ID."

    # Shipping info
    elif "shipping" in user_input:
        return "We offer free shipping on orders above $50. Delivery takes 3–5 days."

    # Return policy
    elif "return" in user_input:
        return "You can return products within 30 days of purchase."

    # Payment methods
    elif "payment" in user_input:
        return "We accept credit cards, PayPal, and Apple Pay."

    # Fallback response
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

# Chat loop
print("Chatbot: Hello! Type 'exit' to end chat.")
while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("Chatbot: Thank you! Have a great day!")
        break
    print("Chatbot:", chatbot_response(user))