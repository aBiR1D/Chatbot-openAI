#A Chatbot With Memory, Thus can answer contextual questions.
#Can be Assigned Specific Role, look #Ref1.0

from openai import OpenAI
from dotenv import load_dotenv
import os
import datetime

load_dotenv()


client = OpenAI(api_key=os.getenv('API_KEY'))

#Clearing the history file in case it had any memory!
with open('chat_history.txt', 'w') as file:
    # Move the file pointer to the start of the file
    file.seek(0)
    # Clear the file
    file.truncate(0)


# Function to append the latest interaction to the chat history
def append_interaction_to_history(history, user_input, bot_response):
    history.append(('user', user_input))
    history.append(('AI', bot_response))
    return history

# Function to truncate the history if it gets too long
def truncate_history(history, max_length=1024):
    # Convert history to a single string
    history_str = ""
    for role, line in history:
        history_str += f"{role.capitalize()}: {line}\n"
        
    # Truncate history if it exceeds the max_length
    if len(history_str) > max_length:
        # Find the last occurrence of "User:" or "Bot:" to keep the context intact
        last_user_idx = history_str.rfind("User:")
        last_bot_idx = history_str.rfind("AI:")
        last_idx = min(last_user_idx, last_bot_idx)
        history_str = history_str[last_idx:]
    return history_str

# Function to get the chatbot's response
#Ref1.0
def get_bot_response(history, user_input):
    
    # Append the latest user input to the history
    history_str = truncate_history(history + [('user', user_input)])
    # Generate the response using OpenAI API
    
    try:
    
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                        {"role": "system", "content": "You are chatting with an Ai Assitant."}, #Update the content to specify any role to the chatbot
                        {"role": "user", "content": history_str}
                    ],
        max_tokens=250,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n"]
        )
        
      
        response_message = response.choices[0].message.content
        return response_message
    except Exception as e:
        return str(e)


def main() -> None:
    chat_history = []  # Initialize an empty chat history
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        bot_response = get_bot_response(chat_history, user_input)
        print(bot_response)
        chat_history = append_interaction_to_history(chat_history, user_input, bot_response)
        
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open("chat_history.txt", "a", encoding="utf-8") as file:
            file.write(f"{timestamp}\nUser: {user_input}\n{bot_response}\n\n")
            
            
if __name__ == "__main__":
    main()