import discord

# Import additional modules

from discord.ext import commands


async def wgu_email_bad_domain(user_email, discord_user):

    # Set initial message here

    bad_domainMessage = discord.Embed(
        title="This email's domain isn't from WGU!",
        description="Hello, {}!\n\nThe email address {} doesn't contain a WGU domain.\n\n\nIf you believe this is a mistake, please contact a moderator in [#verification-support](https://discordapp.com/channels/688822375327989875/768993144380981248)".format(discord_user[0][0:24], user_email),
        colour=discord.Colour.dark_blue(),
    )

    # Standard footer and author

    already_verifiedMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    already_verifiedMessage.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    already_verifiedMessage.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )

    return already_verifiedMessage
