#This needs to access openai.Completion, but this is no longer supported in openai>=1.0.0 
#In Order To Run This you can pin your installation to the old version, e.g. `pip install openai==0.28`

import openai
from dotenv import load_dotenv
import os

load_dotenv()


openai.api_key = os.getenv('API_KEY')

def ask_gpt(prompt: str) -> str:
    response = openai.Completion.create(
        engine = "gpt-3.5-turbo-instruct-0914",
        prompt = prompt,
        max_tokens = 4000,
        temperature = 0.5,
        frequency_penalty = 0,
        presence_penalty = 0,
    )
    return response.choices[0].text.strip()


def main() -> None:
    topic = input("Enter a podcast topic you'd like to create a script about: ")
    prompt = f"Write a detailed script for podcast about '{topic}'."

    response = ask_gpt(prompt)
    print(response)
    
    with open("summary_podcast_legacy.txt", "w", encoding="utf-8") as file:
        file.write(response)


if __name__ == "__main__":
    main()