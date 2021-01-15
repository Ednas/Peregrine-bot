import discord


async def wgu_add_verified_role(self, channel, VERIFIED_ROLE, UNVERIFIED_ROLE, member):
       
    try:

        await member.id.add_roles(
            discord.utils.get(member.guild.roles, name=VERIFIED_ROLE)
        )

        await member.id.remove_roles(
            discord.utils.get(member.guild.roles, name=UNVERIFIED_ROLE)
        )

    except Exception as e:
        print(e)
        errorMessage = "Failed to process verification role for new member: {}\nPlease hand verify this member or contact a bot developer".format(member)
        await channel.send(content=errorMessage)

    return