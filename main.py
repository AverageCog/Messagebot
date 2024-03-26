import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.messages = True  # Enable the intent for message content

bot = commands.Bot(command_prefix='!!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def clear(ctx, *, user_names: str):
    await ctx.message.delete()
    users = [mention for mention in ctx.message.mentions if isinstance(mention, discord.User)]  # Get all mentioned users
    ids = list(map(lambda x: x.id, users)) + ctx.author.id  # Convert mentions to IDs and add the bot's own ID
    
    async for message in ctx.channel.history(limit=None):
        if any(user_id == message.author.id for user_id in ids):
            await message.delete()
bot.run('TE4NDk0NjI5NzA2OTkxMjIxOA.GuqbuO.lKBGNKZNT07OPUoKsMVtZqDXe0nOoyOjnqM6qU')
