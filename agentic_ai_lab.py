import ollama

def main():
    print("---- Agentic AI Lab: Offline LLM Test ----")
    user_input = input("Enter your question for the LLM: ")
    try:
        response = ollama.chat(
            model='mistral:7b-q4',
            messages=[{'role': 'user', 'content': user_input}]
        )
        print("\n--- LLM Response ---")
        print(response['message']['content'])
    except Exception as e:
        print(f"Error: {e}\nCheck if Ollama is running and the model is pulled.")

if __name__ == "__main__":
    main()

