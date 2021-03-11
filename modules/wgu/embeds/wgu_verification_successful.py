import discord

async def wgu_verification_successful(discord_nick):

    # Set initial message here

    success_message = discord.Embed(
        title="Success!",
        description=f"\n\nHello, {discord_nick}!\nYou have been verified! You should now see new channels available. If you do not, please alert a moderator in [#verification-support](https://discordapp.com/channels/688822375327989875/768993144380981248)",
        colour=discord.Colour.dark_blue(),
    )
  
    # Standard footer and author

    success_message.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    success_message.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    success_message.set_author(
        name="Merlin | Test Branch",
        icon_url="https://cdn.discordapp.com/avatars/805916873480470588/2bbcc095669380edec1641774d217a0d.png?size=256",
    )

    return success_message