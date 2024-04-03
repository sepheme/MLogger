import discord

intents = discord.Intents.default()
intents.presences = True
intents.members = True
# Set to True to make message content visible in the console.
intents.message_content = True

# Insert your discord bot token here.
TOKEN = ""

client = discord.Client(intents=intents)

# Initialization
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='You'))
    print(f'{client.user} is now online!')

# Upon receiving message/s
@client.event
async def on_message(message):
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'===========================')
    print(f'guild: {message.guild}')
    print(f'guild id: {message.guild.id}')
    print(f'user: {message.author}')
    print(f'user id: {message.author.id}')
    print(f'channel: {channel}')
    print(f'content: {user_message}')
    print(f'===========================')

client.run(TOKEN)