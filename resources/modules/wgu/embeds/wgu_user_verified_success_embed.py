import discord

# Import additional modules

from discord.ext import commands


async def user_verified_success_embed(user_email, wgu_user):

    # Set initial message here

    emailMessage = discord.Embed(
        title="Email sent!",
        description="Hello, {}!\nAn email has been sent to {}. Please allow up to 5 minutes for it to arrive. If you do not receive an email, please send a message in [#verification-support](https://discordapp.com/channels/688822375327989875/768993144380981248)".format(wgu_user[0], user_email),
        colour=discord.Colour.dark_blue(),
    )
  
    # Standard footer and author

    emailMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    emailMessage.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    emailMessage.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )

    return emailMessage