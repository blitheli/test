import os
import openai

"""
  gpt-3.5-turbo
  chat

  20230401  初次编写
  如果git出现proxy问题，则在控制台输入: git config --global --add remote.origin.proxy "127.0.0.1:10809"
"""

print('----start openai------')
openai.organization = "org-DaDfB9xHQ5ySB3qRdJC8G0zD"
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.Model.list()

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": "北京有多大？"}]
)

print("-------from openai-------")
print(completion.choices[0].message.content)