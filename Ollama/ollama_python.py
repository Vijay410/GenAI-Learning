# Title: Use Ollama with Python
#
# Description:
# This script demonstrates how to interact with local Large Language Models (LLMs)
# using the Ollama Python library. It covers basic chat, streaming responses,
# and simple text generation.
#
# Installation:
# Before running this code, ensure you have Ollama installed on your system
# (from https://ollama.com/) and the Python library installed.
#
# Command to install the library:
# ollama run llama3.2

import ollama  # Import the official Ollama library

# --- Example 1: Basic Chat ---
# This method mimics a conversation format where you provide a list of messages.
# It is useful for maintaining context or chat history.

response = ollama.chat(
    model='llama3.2',  # Specify the model you want to use (ensure you have pulled it via 'ollama pull llama3.1')
    messages=[
        {
            'role': 'user',    # The role can be 'user', 'assistant', or 'system'
            'content': 'Why is the sky blue?',  # The actual prompt or question
        },
    ]
)

# # The response is a dictionary containing metadata and the message
# print(response)
# # # # To get just the answer text, we access ['message']['content']
# # print(response['message']['content'])

response = ollama.chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': 'Write a SQL query to find duplicate  emails'
        }
    ]
)

response = ollama.chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': 'Explain kubernets '
        },

                {
            'role': 'user',
            'content': 'Explain Docker'
        }
    ]
)




# The response is a dictionary containing metadata and the message
# print(response)
# # # To get just the answer text, we access ['message']['content']
# print(response['message']['content'])


# --- Example 2: Streaming Chat ---
# Streaming allows you to receive and display the response piece by piece
# as it is being generated, rather than waiting for the entire answer.
# This creates a "typewriter" effect similar to ChatGPT.

stream = ollama.chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': 'explain kubernets?'}],
    stream=True,  # Enable streaming mode
)
for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)


