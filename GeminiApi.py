import os
import google.generativeai as genai

genai.configure(api_key='AIzaSyBKJOB_PvzMYKsLNIlT9w2_yK1mDuTZYag')

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

# response = chat_session.send_message("what is java")

# print(response.text)

while True:
    user_input = input("Enter your message (type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Exiting chat. Goodbye!")
        break

    # Send the user's input to the AI model
    response = chat_session.send_message(user_input)
    print("AI Response:", response.text)