import discord
from discord.ext import commands

# Set up the bot's intents.
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True  # Add message content intent

# Initialize the bot with a command prefix and the specified intents.
bot = commands.Bot(command_prefix='!', intents=intents)

# This variable will store the class code.
class_code = ""

# Event listener for when the bot has successfully connected to Discord.
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to set the class code.
@bot.command()
async def set_class_code(ctx, code: str):
    global class_code
    class_code = code
    await ctx.send(f"Class code set to {code}")

# Command to view the current class code.
@bot.command()
async def view_class_code(ctx):
    if class_code:
        await ctx.send(f"The current class code is: {class_code}")
    else:
        await ctx.send("No class code has been set yet.")

bot.run('YOUR_NEW_BOT_TOKEN')







