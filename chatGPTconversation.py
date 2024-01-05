import openai

# Set your OpenAI GPT-3 API key
openai.api_key = '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'

def chatgpt_conversation():
    conversation = []

    # Get user input for the initial prompt
    user_input = input("You: ")
    prompt = f"Tell me about {user_input}."

    while True:
        # ChatGPT 1 responds to ChatGPT 2's prompt
        response1 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are ChatGPT 1."},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": "I am ChatGPT 1."},
            ]
        )

        conversation.append(response1['choices'][0]['message']['content'])
        print("ChatGPT 1:", response1['choices'][0]['message']['content'])

        # Check if the user wants to stop
        stop_condition = input("Type 'stop' to end the conversation or press Enter to continue: ")
        if stop_condition.lower() == 'stop':
            break

        # ChatGPT 2 responds to ChatGPT 1's prompt
        response2 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are ChatGPT 2."},
                {"role": "user", "content": response1['choices'][0]['message']['content']},
                {"role": "assistant", "content": "I am ChatGPT 2."},
            ]
        )

        conversation.append(response2['choices'][0]['message']['content'])
        print("ChatGPT 2:", response2['choices'][0]['message']['content'])

        # Check if the user wants to stop
        stop_condition = input("Type 'stop' to end the conversation or press Enter to continue: ")
        if stop_condition.lower() == 'stop':
            break

    return conversation

# Start conversation
conversation = chatgpt_conversation()

# Print the final conversation
for message in conversation:
    print(message)
