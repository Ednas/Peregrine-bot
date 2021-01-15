

import discord

async def wgu_set_user_nick_on_join(member, channel, NICKNAME_SCHEMA):

    # Set new members to default unverified role

    try:

        await member.edit(nick=NICKNAME_SCHEMA)

    except Exception as e:
        print(e)
        errorMessage = "Failed to set nickname on new user: {}\n".format(member)
        await channel.send(content=errorMessage)
    return