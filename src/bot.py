"""Discord bot definition for Chip"""
import os
import asyncio
import discord
from dotenv import load_dotenv
load_dotenv()

from uwin_ai_assistant import inference

import config
from automod import AutomodInterface
from messages import info, error, success, log

# Setup

intents = discord.Intents.all()
bot = discord.Bot(command_prefix="c!", intents=intents, help_command=None)

automod = AutomodInterface()

# Events

@bot.event
async def on_ready():
    """Triggers when the bot is running"""
    activity = discord.Game(name="Coming soon!", type=2)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Discord bot online")

@bot.event
async def on_message(message):
    """Event handler for messages, flags problematic content"""
    if not config.FEAT_AUTOMOD or message.author == bot.user:
        return
    else:
        score = automod.analyze_message(message.content)
        if float(score[1]) > 0.5:
            await log(message, float(score[1]))

# Commands

@bot.slash_command(name="help", description="Help command")
async def help(ctx):
    """Displays a help message"""
    message = """
        **Chip is an AI powered discord moderation bot and chatbot. It uses machine learning to detect toxic messages and automatically flag for the moderators, and is also available to assist with any queries you may have about Computer Science at The University of Windsor! (Double check important information, AI can make mistakes)**
                            
        **/help** - Displays this message
        **/ask** - Ask Chip anything about Computer Science at the University of Windsor!
    """
    await info(ctx, "Info", message)

@bot.slash_command(name="ask", description="Ask Chip anything about Computer Science at the University of Windsor!")
async def ask(ctx, query: str):
    """Respond to a user query using the RAG model"""
    if not config.FEAT_ADVISOR:
        return
    if ctx.channel.id == int(os.getenv("ADVISOR_CHANNEL")):
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, inference.generate_response, query)
        await success(ctx, query, response)

bot.run(os.getenv("DISCORD_TOKEN"))
