import discord
from discord.ext import commands
import time

# Set up the bot's intents.
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True  # Add message content intent

# Initialize the bot with a command prefix and the specified intents.
bot = commands.Bot(command_prefix='!', intents=intents)

# This variable will store the class code and its expiration time.
class_code_info = {
    'code': "",
    'expiration_time': 0,
    'submitted_by': None  # Store the user ID who submitted the class code
}

# List of allowed text channels where the commands can be used.
allowed_channels = [
    'it-essentials',
    'fundamentals-of-computing-logic',
    'introduction-to-web-development',
    'personal-finance',
    'mathematics-for-computer-technology',
    'communicating-across-context',
    'introduction-to-networks',
    'linux-essentials',
    'introduction-to-programming',
    'enterprise-desktop-operating-systems',
    'mathematics-for-computer-technology-ii',
    'enterprise-networking-and-automation',
    'wireless-technology-fundamentals',
    'windows-server-network-infrastructure',
    'devops-for-system-administration',
    'cyber-security-fundamentals'
]


# Function to check if the command can be used in the current channel.
def is_allowed_channel(ctx):
    return ctx.channel.name.lower() in allowed_channels


# Function to set the class code with an expiration time and user ID.
@bot.command()
@commands.check(is_allowed_channel)
async def set_class_code(ctx, code: str):
    global class_code_info
    if class_code_info['submitted_by'] is None:
        class_code_info['code'] = code
        class_code_info[
            'expiration_time'] = time.time() + 4 * 60 * 60  # Set expiration time to 4 hours (4 * 60 * 60 seconds)
        class_code_info['submitted_by'] = ctx.author.id  # Store the user ID who submitted the class code
        await ctx.send(f"Class code has been set by {ctx.author.name}.")
    else:
        previous_submitter = bot.get_user(class_code_info['submitted_by']).name
        await ctx.send(f"Class code has already been submitted by {previous_submitter}.")


# Function to view the current class code, but only if it's within the expiration time.
@bot.command()
@commands.check(is_allowed_channel)
async def view_class_code(ctx):
    current_time = time.time()
    expiration_time = class_code_info['expiration_time']

    if current_time <= expiration_time:
        submitted_by = bot.get_user(class_code_info['submitted_by']).name if class_code_info[
            'submitted_by'] else "Unknown User"
        await ctx.send(f"The current class code is: {class_code_info['code']} (Submitted by {submitted_by})")
    else:
        await ctx.send("No class code is available or it has expired.")


# Event listener for when the bot has successfully connected to Discord.
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


# Replace 'YOUR_BOT_TOKEN' with your actual bot token.
bot.run('YOUR_NEW_BOT_TOKEN')







