

import discord

async def wgu_set_user_nick_on_join(member, channel):

    new_nickname = "{} | UNVERIFIED".format(member.name[0..20])

    # Set new members to default unverified role

    try:

        await member.edit(nick=new_nickname)

    except Exception as e:
        print(e)
        errorMessage = "Failed to set nickname on new user: {}\n".format(member)
        await channel.send(content=errorMessage)
    return