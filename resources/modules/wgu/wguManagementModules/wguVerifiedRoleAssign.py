import discord


async def wguAddVerifiedRole(self, payload, channel):

    try:

        if payload.emoji:
            print("Success! Emoji is: {}".format(payload.emoji))
            await payload.member.add_roles(
                discord.utils.get(payload.member.guild.roles, name="Verified")
            )

            # await payload.member.remove_roles(
            #    discord.utils.get(payload.member.guild.roles, name="Unverified")
            # )

        else:
            print("Failed! Emoji is: {}".format(payload.emoji))

    except Exception as e:
        print(e)
        errorMessage = "Failed to process verification role for new member: {}\nPlease hand verify this member or contact a bot developer".format(
            payload.member
        )
        await channel.send(content=errorMessage)

    return