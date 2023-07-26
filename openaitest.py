import os
import openai


openai.api_key = os.getenv("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")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my boss for resignation?",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)