from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Load your API key from an environment variable or secret management service
client = OpenAI(api_key=os.environ['API_KEY'])


def engine(prompt : str):
    
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="hd",
    n=1,
    style="vivid",
    )

    image_url = response.data[0].url
    return image_url
    
def main() -> None:
    topic = input("What do you want to draw?: ")
    prompt = f"Create an Image where {topic}"
    response = engine(prompt)
    print(response)
    
if __name__ == "__main__":
    main()
    