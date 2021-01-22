import discord

# Import additional modules

from discord.ext import commands


async def wgu_htb_embed():

    # Set initial message here

    htbMessage = discord.Embed(
        title="Hack The Box? Try Harder",
        description="\n\n━━━━━━━━━━━━",
        color=discord.Colour.dark_green(),
    )

    # Set custom fields here

    htbMessage.add_field(
        name="Join the WGU Hack The Box team!",
        value="",
        inline=False,
    )

    # Standard footer and author

    htbMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    htbMessage.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    htbMessage.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )

    return htbMessage