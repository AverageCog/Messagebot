import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.messages = True  # Enable the intent for message content

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def clear(ctx, user: discord.User):
    await ctx.message.delete()
    async for message in ctx.channel.history(limit=None):
        if message.author == user:
            await message.delete()

bot.run('TE4NDk0NjI5NzA2OTkxMjIxOA.GuqbuO.lKBGNKZNT07OPUoKsMVtZqDXe0nOoyOjnqM6qU')
