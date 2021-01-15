import discord


async def wgu_set_unverified_on_new_join(member, channel):

    # Set new members to default unverified role

    try:

        await member.add_roles(discord.utils.get(member.guild.roles, name="Unverified"))

    except Exception as e:
        print(e)
        errorMessage = "Failed to add default roles to new user: {}\n".format(member)
        await channel.send(content=errorMessage)
    return