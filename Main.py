import discord
from discord.ext import commands
from Commands import register_commands
from Scheduler import task_worker

TOKEN = "TOKEN"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Register all bot commands
register_commands(bot)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    bot.loop.create_task(task_worker())

bot.run(TOKEN)

