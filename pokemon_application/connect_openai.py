# to make the application more intelligent by adding AI into it
from openai import OpenAI
client = OpenAI()
prompt = input("ask pokebot: ")
response = client.responses.create(
    input=prompt,
    model="gpt-5"
)
print(response.output_text)