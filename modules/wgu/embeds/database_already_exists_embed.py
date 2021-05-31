import discord

async def database_already_exists_embed(user_email):

    # Set initial message here

    already_verified_message = discord.Embed(
        title="This email has already been verified!",
        description=f"Hello,\n\nThe email address `{user_email}` is already registered to a member of this guild.\n\nIf you believe this is a mistake, please contact a moderator in [#verification-support](https://discordapp.com/channels/688822375327989875/768993144380981248)",
        colour=discord.Colour.dark_blue(),
    )
  
    # Standard footer and author

    already_verified_message.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    already_verified_message.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    already_verified_message.set_author(
        name="Peregrine",
        icon_url="https://cdn.discordapp.com/avatars/716442510423228496/f293e738c3559906120db7e4d43da13e.png?size=256",
    )

    return already_verified_message