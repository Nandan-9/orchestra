from llm.deepseek import chat_completion

while True:
    chatInput = input("You: ")
    if chatInput.lower() in {"exit", "quit"}:
        break
    chatOutput = chat_completion(chatInput)
    print("Bot:", chatOutput)
