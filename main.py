import discord
import requests


client = discord.Client()

CHANNEL_WEBHOOKS = {
    523687931483783168: "webhook url here",  # 2b2tpe
    711600776451194910: "webhook url here"   # 2b2e
}

@client.event
async def on_ready():
    print(f"Logged in as {client.user}.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

     if message.channel.id in CHANNEL_WEBHOOKS:
        webhook_url = CHANNEL_WEBHOOKS[message.channel.id] 

        webhook_payload = {
            "username": str(message.author),
            "avatar_url": str(message.author.avatar.url) if message.author.avatar else None,
            "content": message.content,
        }

        response = requests.post(webhook_url, json=webhook_payload)

        if response.status_code == 204:
            print(f"Message from channel {message.channel.id} forwarded successfully: {message.content}")
        else:
            print(f"Failed to forward message from channel {message.channel.id}: {response.status_code} {response.text}")


TOKEN = "your token here" 
client.run(TOKEN)