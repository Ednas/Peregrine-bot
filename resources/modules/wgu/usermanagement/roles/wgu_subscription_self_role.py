import discord

async def wgu_subscription_self_role(self, payload, CCDC_SUB_EMOJI, NICE_SUB_EMOJI, CTF_SUB_EMOJI, HTB_SUB_EMOJI, THM_SUB_EMOJI, OTW_SUB_EMOJI, FOREIGN_SUB_EMOJI):

    # Assign CCDC sub role

    if str(payload.emoji.name) == str(CCDC_SUB_EMOJI):
        await payload.member.add_roles(discord.utils.get(payload.guild.roles, name='CCDC Alerts'))

    # Assign NICE sub role

    if str(payload.emoji.name) == str(CCDC_SUB_EMOJI):
        await payload.member.add_roles(discord.utils.get(payload.guild.roles, name='NICE Alerts'))

    # Assign CTF sub role

    if str(payload.emoji.name) == str(CCDC_SUB_EMOJI):
        await payload.member.add_roles(discord.utils.get(payload.guild.roles, name='CTF Alerts'))
    
    
    # Assign Foreign sub role

    if str(payload.emoji.name) == str(CCDC_SUB_EMOJI):
        await payload.member.add_roles(discord.utils.get(payload.guild.roles, name='Foreign Alerts'))
    
    
    # Assign HTB sub role

    if str(payload.emoji.name) == str(CCDC_SUB_EMOJI):
        await payload.member.add_roles(discord.utils.get(payload.guild.roles, name='HTB Alerts'))
    
    
    # Assign THM sub role

    if str(payload.emoji.name) == str(CCDC_SUB_EMOJI):
        await payload.member.add_roles(discord.utils.get(payload.guild.roles, name='THM Alerts'))
    
    
    # Assign OTW sub role

    if str(payload.emoji.name) == str(CCDC_SUB_EMOJI):
        await payload.member.add_roles(discord.utils.get(payload.guild.roles, name='OTW Alerts'))
    
    return