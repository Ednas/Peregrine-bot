import discord

# Import additional modules

from discord.ext import commands
import discord

async def wgu_verify_success_log_embed( message):

    # Set initial message here

    logMessage = discord.Embed(
        title="Verification complete",
        description="The following account has been verified succesfully!\n\n   ┕ Username: {}\n".format(message.author),
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
        name="Peregrine",
        icon_url="https://cdn.discordapp.com/avatars/716442510423228496/f293e738c3559906120db7e4d43da13e.png?size=128",
    )

    return logMessage