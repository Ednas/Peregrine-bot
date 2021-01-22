import discord

async def wgu_enrollment_status_self_role(self, payload, STUDENT_EMOJI, ALUMNI_EMOJI):

    # Assign Student role

    if str(payload.emoji.name) == str(STUDENT_EMOJI):
        await payload.member.add_roles(discord.utils.get(payload.guild.roles, name='Student'))

    # Assign Alumni role

    if str(payload.emoji.name) == str(ALUMNI_EMOJI):
        await payload.member.add_roles(discord.utils.get(payload.guild.roles, name='Alumni'))
    
    return