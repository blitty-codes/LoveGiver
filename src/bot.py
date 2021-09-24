import os
import random
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='lover?')

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='yeah', help=' - Gives you a welcome')
async def on_message(ctx):
	await ctx.send('Hello bombom ;)')

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice = 0, number_of_sides = 0):
	if (number_of_dice == 0) or (number_of_sides == 0):
		await ctx.send('I need 2 numbers :(')
		return

	dice = [
		str(random.choice(range(1, number_of_sides + 1)))
		for _ in range(number_of_dice)
	]
	await ctx.send(', '.join(dice))

bot.run(TOKEN)