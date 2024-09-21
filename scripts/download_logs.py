"""
This script downloads the logs from the server (after a specified date) and stores them in a CSV file.
The purpose is for iterative improvement in the dataset and to track the performance of the model.
Usage: python download_logs.py <year> <month> <day> <guild_id> <channel_id>
"""
import os
import sys
import csv
import asyncio
from datetime import datetime
from dotenv import load_dotenv
import discord
load_dotenv()

# Setup

intents = discord.Intents.all()
bot = discord.Bot(command_prefix="c!", intents=intents, help_command=None)

# Config
try:
    AFTER_DATE = datetime(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    GUILD_ID = int(sys.argv[4])
    CHANNEL_ID = int(sys.argv[5])
except IndexError:
    print("Usage: python download_logs.py <year> <month> <day> <guild_id> <channel_id>")
    sys.exit(1)

# Events

@bot.event
async def on_ready():
    """Triggers when the bot is running"""
    activity = discord.Game(name="Coming soon!", type=2)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Discord bot online")

    # Grab given guild
    guild = bot.get_guild(GUILD_ID)
    if guild is None:
        print(f'Guild with ID {GUILD_ID} not found')
        await bot.close()
        return

    # Grab given channel
    channel = guild.get_channel(CHANNEL_ID)
    if channel is None:
        print(f'Channel with ID {CHANNEL_ID} not found')
        await bot.close()
        return
    
    # Extract all messages after the given date
    messages = []
    async for message in channel.history(after=AFTER_DATE, oldest_first=True, limit=None):
        if message.author == bot.user:
            for embed in message.embeds:
                messages.append([embed.description.split(":", 1)[1].strip(), 0]) # Defaults to a non-toxic rating

    if not messages:
        print("No messages found.")
    else:
        with open('bot_messages.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['content', 'rating'])
            writer.writerows(messages)
        
        print(f'Successfully saved {len(messages)} messages to bot_messages.csv')

    await bot.close()

bot.run(os.getenv("DISCORD_TOKEN"))
