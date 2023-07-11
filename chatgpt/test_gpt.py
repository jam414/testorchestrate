import openai
import os


openai.api_key = os.environ["OPENAI_API_KEY"]
prompt = "Write a selenium code in java to test web page"
model = "text-davinci-002"
response = openai.Completion.create(
  engine=model,
  prompt=prompt,
  max_tokens=400
)

print(response.choices[0].text)