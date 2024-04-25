#Make sure you're on latest version of openai
#you can run "pip install --upgrade openai" if required.
#A Chatbot Without Memory.
#Can be Assigned Specific Role, look #Ref1.0


from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Load your API key from an environment variable or secret management service
client = OpenAI(api_key=os.getenv('API_KEY'))

def create_chatbot_response(prompt: str) -> str:
    try:
        # Using the gpt-3.5-turbo-instruct model
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=4000,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
        )
        response_message = response.choices[0].message.content
        return response_message
    except Exception as e:
        return str(e)



def main() -> None:
    topic = input("Enter a podcast topic you'd like to create a script about: ") 
    prompt = f"Write a detailed script for podcast about '{topic}'."
    
    #Ref1.0
    #The SuperPower : Update the topic and prompt as you want! like: Turn it into a professionl cook, just by starting the prompt with "Write a detailed recipe:....."
    #You get the idea!

    response = create_chatbot_response(prompt)
    print(response)
    
    with open("summary_podcast.txt", "w", encoding="utf-8") as file:
        file.write(response)


if __name__ == "__main__":
    main()
