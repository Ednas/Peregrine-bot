import discord


async def wgu_add_verified_role(self, channel, guild, VERIFIED_ROLE, UNVERIFIED_ROLE, message):
     
    member = discord.utils.find(lambda m : m.id == message.channel.recipient.id, guild.members) 
    
    print("Verification triggered by: {} for guild {}".format(member.id, member.guild))
    
    try:

        await member.add_roles(
            discord.utils.get(guild.roles, name=VERIFIED_ROLE)
        )

        await member.remove_roles(
            discord.utils.get(guild.roles, name=UNVERIFIED_ROLE)
        )

    except Exception as e:
        print(e)
        errorMessage = "Failed to process verification role for new member: {}\nPlease hand verify this member or contact a bot developer".format(member)
        await channel.send(content=errorMessage)

    return