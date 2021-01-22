

import discord

async def wgu_set_user_nick_on_verify(self, username, channel, conx):

    # Get email from database

    cursor = conx.cursor()
    sql = "SELECT * FROM verified WHERE username = %s"
    val = (username)
    cursor.execute(sql, val)
    result = cursor.fetchall()

    ###### Code here

    # Set up new username

    new_nickname = "{} | {}".format(username, result.email)

    # Apple username

    try:

        await member.edit(nick=new_nickname)

    except Exception as e:
        print(e)
        errorMessage = "Failed to set nickname on new user: {}\n".format(member)
        await channel.send(content=errorMessage)
    return