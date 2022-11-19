import discord
from discord.ext import commands

class Math(commands.Cog, name="Math"):
	"""this is math"""
	def __init__(self, bot):
		self.bot = bot
	
	def fibbonaci(self, n):
		if n == 0:
			return 0
		elif n == 1:
			return 1
		elif n == 2:
			return 1
		else:
			return self.fibbonaci(n-1) + self.fibbonaci(n-2)

	def factorial(self, n):
		if n == 0:
			return 1
		else:
			return n * self.factorial(n-1)

	@commands.command(name="add", aliases=["addition"])
	async def add(self, ctx, *, num):
		"""adds multiple numbers"""
		for i in range(length(num)):
			result = 0
			result += int(num[i])

		ctx.send(result)

	@commands.command(name="subtract", aliases=["subtraction"])
	async def sub(self, ctx, *, num):
		"""subtracts multiple numbers"""
		for i in range(length(num)):
			result = 0
			result -= int(num[i])
		
		ctx.send(result)

	@commands.command(name="multiply", aliases=["multiplication"])
	async def mul(self, ctx, *, num):
		"""multiplies multiple numbers"""
		for i in range(length(num)):
			result = 0
			result *= int(num[i])
		
		ctx.send(result)

	@commands.command(name="divide", aliases=["division"])
	async def div(self, ctx, *, num):
		"""divides multiple numbers"""
		for i in range(length(num)):
			result = 0
			result /= int(num[i])
		
		ctx.send(result)

	@commands.command(name="mod", aliases=["modulus"])
	async def mod(self, ctx, num1, num2):
		"""mod two numbers"""
		ctx.send(int(num1) % int(num2))

	@commands.command(name="pow", aliases=["power"])
	async def pow(self, ctx, num1, num2):
		"""pow"""
		ctx.send(int(num1) ** int(num2))
	
	@commands.command(name="sqrt", aliases=["squareroot"])
	async def sqrt(self, ctx, num):
		"""sqrt"""
		ctx.send(int(round(num ** 0.5)))
	
	@commands.command(name="fibb", aliases=["fibbonaci"])
	async def fibb(self, ctx, num=1):
		"""fibbonaci"""
		ctx.send(self.fibbonaci(num))
	
	@commands.command(name="factor", aliases=["factorial"])
	async def fact(self, ctx, num):
		"""factorial"""
		ctx.send(self.factorial(num))