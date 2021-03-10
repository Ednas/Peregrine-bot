import discord

async def wgu_instructions_embed(member):

    instructionsEmbed = discord.Embed(
        title="Verification Instructions",
        description="\n\nHello, {}!\nTo access the Discord, please reply with the following command\n'!email <your student email>'\
            (ex. !email jsmith0@wgu.edu)\n An email will be sent to you with a verification code. Please refer to the instructions included\
            in the email. Please allow up to five minutes for the email to arrive, and verify that it did not go to your spam folder.\
            \nIf you have submitted the wrong email address or have a type, you can reset the bot and resend the email by issueing the\
            `!delete`\ command followed by the email address you submitted. Afterwards, you can resubmit by reissuing the !email command\
            \n\n If you require support, please visit the verification-support channel located in the welcome area. Refer to the embed\
            in welcome for further details".format(member),
        colour=discord.Colour.dark_blue(),
        )

    # Standard footer and author

    instructionsEmbed.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    instructionsEmbed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    instructionsEmbed.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )

    return instructionsEmbed