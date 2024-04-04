import os
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
API_SK = os.getenv("OPENAI_API_KEY")  ##this is not going to be in repo, its private key see README
client = OpenAI(
    api_key=API_SK,
)

"""
Process prompts
"""


def promptHandler(prompt) -> str:
    response = callOpenAi(prompt)
    # TODO- format and make the response cleaner. 
    # Any additional functionality can be orchestrated here as well
    
    return response


def callOpenAi(input) -> str:
     
    completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a meeting assistant, skilled in preparing for meetings. Write 2 ice breaker questions related to the topic and 4 agenda items that is related. Write 2-3 items to the agenda items to guide discussion and engage attendees."},
    {"role": "user", "content": f"{input}"}
  ]
)
    response = completion.choices[0].message.content
    print(response)
    response = addHtmlFormatting(response)
    return response

def addHtmlFormatting(raw_input) -> str:
    #TODO- add HTML formatting to the response
    cleaned_response = raw_input.replace("\n", "<br>")
    return cleaned_response
