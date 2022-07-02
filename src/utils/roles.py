import discord

async def assign_rol(payload, client, roles: dict):
	guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

	if payload.emoji.name in roles:
		role = discord.utils.get(guild.roles, name=roles[payload.emoji.name])
		# print(role)

		if role is not None:
			member = await guild.fetch_member(payload.user_id)
			if member is not None:
				await member.add_roles(role)
				# print("Done!")
			# else:
				# print("Member not found")
		# else:
			# print("Role not found")

async def remove_rol(payload, client, roles: dict):
	guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

	if payload.emoji.name in roles:
		role = discord.utils.get(guild.roles, name=roles[payload.emoji.name])
		# print(role)

		if role is not None:
			member = await guild.fetch_member(payload.user_id)
			if member is not None:
				await member.remove_roles(role)
				# print("Done!")
			# else:
				# print("Member not found")
		# else:
			# print("Role not found")
