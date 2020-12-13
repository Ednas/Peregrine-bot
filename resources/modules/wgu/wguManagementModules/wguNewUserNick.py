import discord


async def wguSetNewUserNick(member, channel):

    defaultNick = "{Pseudonym} | {WGU Handle}"

    # Set new members to default unverified role

    try:

        await member.edit(nick=defaultNick)

    except Exception as e:
        print(e)
        errorMessage = "Failed to set nickname on new user: {}\n".format(member)
        await channel.send(content=errorMessage)
    return