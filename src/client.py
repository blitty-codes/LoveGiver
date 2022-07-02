import discord

from .config import GUILD
from .utils.roles import assign_rol, remove_rol

common_roles = {
	'🍎': 'rojo',
	'🍆': 'morado',
	'🐷': 'rosa',
	'🐟': 'azul',
	'🤪': 'emojier',
}

special_rol = {
	'DIY_enjoyer': 'DIY enjoyer'
}

client = discord.Client()

@client.event
async def on_ready():
	# guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
	guild = discord.utils.get(client.guilds, name=GUILD)

	print(f'{client.user} is connected to the following guild:\n{guild.name}(id: {guild.id})')

@client.event
async def on_raw_reaction_add(payload):
	if (payload.message_id == 992495124896555009):
		await assign_rol(payload, client, roles=special_rol)

	if (payload.message_id == 888719215178174475):
		await assign_rol(payload, client, roles=common_roles)

@client.event
async def on_raw_reaction_remove(payload):
	if (payload.message_id == 992495124896555009):
		await remove_rol(payload, client, roles=special_rol)

	if (payload.message_id == 888719215178174475):
		await remove_rol(payload, client, roles=common_roles)

#client = CustomClient()
