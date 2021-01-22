import discord

# Import additional modules

from discord.ext import commands


async def verify_embed_log_message(message, author, email, wgu_user, discord_user):

    # Set initial message here

    logMessage = discord.Embed(
        title="New verification interaction",
        description="{}\n{}\n{}\n{}\n{}\n{}\n{}".format(message, author, email, wgu_user, discord_user),
        colour=discord.Colour.dark_blue(),
    )
    
    # Standard footer and author

    logMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    logMessage.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    logMessage.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )

    return logMessage