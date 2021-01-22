import discord

async def wgu_enrollment_status_self_role(self, payload, STUDENT_EMOJI, ALUMNI_EMOJI, GUILD_ID):

    guild = self.get_guild(int(GUILD_ID))

    # Assign Student role

    if str(payload.emoji.name) == str(STUDENT_EMOJI):
        await payload.member.add_roles(discord.utils.get(guild.roles, name='Student'))

    # Assign Alumni role

    if str(payload.emoji.name) == str(ALUMNI_EMOJI):
        await payload.member.add_roles(discord.utils.get(guild.roles, name='Alumni'))
    
    return