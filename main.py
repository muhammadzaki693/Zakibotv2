import os
from keep_alive import keep_alive
from discord.ext import commands
os.load_dotenv(".env")

bot = commands.Bot(
	command_prefix="z",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 758298255389097984  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


extensions = [
	'cogs.cog_developer',
	'cogs.cog_utils',
	'cogs.cog_math'# Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot