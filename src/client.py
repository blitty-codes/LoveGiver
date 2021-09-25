import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

roles = {
	'🍎': 'rojo',
	'🍆': 'morado',
	'🐷': 'rosa',
	'🐟': 'azul',
	'🤪': 'emojier'
}

client = discord.Client()

@client.event
async def on_ready():
	# guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
	guild = discord.utils.get(client.guilds, name=GUILD)

	print(f'{client.user} is connected to the following guild:\n{guild.name}(id: {guild.id})')

@client.event
async def on_raw_reaction_add(payload):
	if (payload.message_id == 888719215178174475):
		guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

		if payload.emoji.name in roles:
			role = discord.utils.get(guild.roles, name=roles[payload.emoji.name])
			print(role)

			if role is not None:
				member = await guild.fetch_member(payload.user_id)
				if member is not None:
					await member.add_roles(role)
					print("Done!")
				else:
					print("Member not found")
			else:
				print("Role not found")

@client.event
async def on_raw_reaction_remove(payload):
	if (payload.message_id == 888719215178174475):
		guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

		if payload.emoji.name in roles:
			role = discord.utils.get(guild.roles, name=roles[payload.emoji.name])
			print(role)

			if role is not None:
				member = await guild.fetch_member(payload.user_id)
				if member is not None:
					await member.remove_roles(role)
					print("Done!")
				else:
					print("Member not found")
			else:
				print("Role not found")

#client = CustomClient()
client.run(TOKEN)
