import openai
import prompt_toolkit

# Set up OpenAI API key
openai.api_key = "INSERT_YOUR_API_KEY_HERE"

# Define function to generate response from GPT-3
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

# Define function to handle user input and generate response
def chat():
    while True:
        user_input = prompt_toolkit.prompt("> ")
        if user_input.lower() in ["exit", "quit"]:
            break
        prompt = f"User: {user_input}\nChatGPT:"
        response = generate_response(prompt)
        print(response)

# Call chat function to start the conversation
chat()

    