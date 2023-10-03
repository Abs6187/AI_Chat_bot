import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a Indian Lawyer and Gave Advice according to Indian constitution"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "AI Chat Bot for Legal Assistance")

demo.launch(share=True)
