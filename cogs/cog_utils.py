import discord
from discord.ext import commands

class Utils(commands.Cog, name="Utils"):
	"""Utilities for the bot."""
	def __init__(self, bot):
		self.bot = bot
	
	def ping(self, ctx):
		ctx.send("Pong! {}".format(ctx.bot.latency * 1000))
	
	def say(self, ctx, *, msg):
		ctx.send(msg)

def setup(bot):
	bot.add_cog(Utils(bot))