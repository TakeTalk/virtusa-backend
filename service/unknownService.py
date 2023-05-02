
import openai

openai.api_key = "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"
def emotion(sentence):
    messages = []
    messages.append({"role": "system", "content": "You are kind hearted doctor"})

    message = sentence
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return  reply + " Also i can suggest you some hospital nearby or your preferred location."

#print(emotion("i am very sick"))