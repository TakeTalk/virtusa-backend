import openai

openai.api_key = "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"


def emotion(sentence):
    messages = [{"role": "system", "content": "You are kind hearted doctor"}]
    message = sentence
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    additional_msg = " Also I can suggest and book appointment to hospitals on your preferred location."
    return reply + additional_msg

# print(emotion("i am very sick"))
