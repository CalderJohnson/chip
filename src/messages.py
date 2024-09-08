"""Message templates for Discord bot"""
import os
import discord

async def error(ctx, title: str, content: str):
    """Display an error message"""
    message = discord.Embed(title=title, color=0xFF0000, description=content)
    await ctx.respond(embed=message)

async def success(ctx, title: str, content: str):
    """Display a success message"""
    message = discord.Embed(title=title, color=0x00FF00, description=content)
    await ctx.respond(embed=message)

async def info(ctx, title: str, content: str):
    """Misc message"""
    message = discord.Embed(title=title, color=0x00FFA2, description=content)
    await ctx.respond(embed=message)

async def log(message, score, log_channel_id):
    """Log a message to the server's log channel"""
    channel = message.guild.get_channel(log_channel_id)
    user = message.author
    message = discord.Embed(title="Log", color=0x00FFA2, description=f"Message logged with score {score} from user <@{user.id}>: {message.content}")
    await channel.send(embed=message)
