import discord


async def wguRemoveVerifiedRole(self, member, payload, channel):

    try:
        if payload.emoji:
            print("Success! Emoji is: {}".format(payload.emoji))
            await member.add_roles(
                discord.utils.get(member.guild.roles, name="Unverified")
            )

            await member.remove_roles(
                discord.utils.get(member.guild.roles, name="Verified")
            )

        else:
            print("Failed! Emoji is: {}".format(payload.emoji))

    except Exception as e:
        print(e)
        errorMessage = "Failed to process verification role for new member: {}\nPlease hand verify this member or contact a bot developer".format(
            member
        )
        await channel.send(content=errorMessage)

    return