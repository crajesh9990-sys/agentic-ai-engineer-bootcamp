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

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")

        if choice == '1':
            explain_ai_concept()
        elif choice == '2':
            summarize_text()
        elif choice == '3':
            generate_interview_question()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
