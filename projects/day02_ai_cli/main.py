from menu import display_menu
from ai_service import ask_AI

def explain_ai_concept():
    topic = input("Enter the AI concept you want to understand: ")
    prompt = f"""
    Explain the following AI concept in simple terms.

    Topic: {topic}

    Give:
    1. Definition
    2. Real-world example
    3. Why it is important
    """

    response = ask_AI(prompt)
    print(f"\nResponse:\n{response}")

def summarize_text():
    text = input("Enter the text you want to summarize: ")
    prompt = f"""
    Summarize the following text.

    Text: {text}

    Provide:
    1. Key points
    2. Summary in bullet points
    """

    response = ask_AI(prompt)
    print(f"\nResponse:\n{response}")

def generate_interview_question():
    topic = input("Interview topic: ")
    prompt = f"""
    Generate one interview question on {topic}.

    Then provide:

    - Ideal answer
    - Common mistakes
    """

    print("\nThinking...\n")
    print(ask_AI(prompt))

def generate_python_code():
    user_input = input("Enter your task to generate code in Python:")
    prompt = f"""
    You are an expert Python developer.

    Generate clean Python code for:

    {user_input}

    Include comments.
    """

    print("Generating...")
    print(ask_AI(prompt))

def chatbot():
    while(True):
        user_input = input("You: ")
        if(user_input.lower() == "exit"):
            print("Exiting the chatbot. Goodbye!")
            break
        prompt = f"""
        You are a intelligent chatbot and answer the quesions in a friendly manner. You have to answer the questions in a simple way. If you don't know the answer, say "I don't know".

        {user_input}
        """

        print("Thinking...\n")
        print(f"AI: {ask_AI(prompt)}")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            explain_ai_concept()
        elif choice == '2':
            summarize_text()
        elif choice == '3':
            generate_interview_question()
        elif choice == '4':
            print("Generate Python code")
            generate_python_code()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            chatbot()
            # print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
