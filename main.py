import discord
import random
import os
import asyncio
from flask import Flask
from keep_alive import keep_alive
import traceback

keep_alive()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

port = os.environ.get('PORT', 8080)  # Default to 5000 if PORT environment variable is not set

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

client = MyClient()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return

        if message.embeds:
            print(f"Embeds found in message from {message.author}:")
            for embed in message.embeds:
                print(f"- Description: {embed.description}")
                if embed.fields:
                    print("  Fields:")
                    for field in embed.fields:
                        print(f"    - {field.name}: {field.value}")
                if embed.footer:
                    print(f"  Footer: {embed.footer.text}")
                print("---")
    except Exception as e:
        print(f"An error occurred in on_message: {e}")
        traceback.print_exc()

# Example of adding debug output
@client.event
async def on_ready():
    try:
        print(f'Logged in as {client.user.name} ({client.user.id})')
        print('------')
    except Exception as e:
        print(f"An error occurred in on_ready: {e}")
        traceback.print_exc()

# Run the bot with your token
if __name__ == "__main__":
    client.run(os.environ['TOKEN'])
