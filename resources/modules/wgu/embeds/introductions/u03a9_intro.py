import discord

# Import additional modules

from discord.ext import commands


async def wgu_u03a9_intro_embed(wgu_user):

    # Set initial message here

    successMessage = discord.Embed(
        title="Justin \"No Raw Talent\" Garcia | U03A9",
        description="Discord Administrator | BS Cyber Security and Information Assurance | Student\n\n".format(wgu_user[0]),
        colour=discord.Colour.dark_blue(),
    )
  
    # Standard footer and author

    successMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    successMessage.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    successMessage.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )

    return successMessage