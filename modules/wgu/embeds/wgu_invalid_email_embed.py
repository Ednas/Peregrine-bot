import discord

async def wgu_invalid_email_embed(user_email):

    # Set initial message here

    invalid_email_message = discord.Embed(
        title="Invalid email domain!",
        description=f"The email `{user_email}` is not a valid student email. Please submit your student email (e.x johndoe@wgu.edu). If you believe this is an error, please send a message in [#verification-support](https://discordapp.com/channels/688822375327989875/768993144380981248)",
        colour=discord.Colour.dark_blue(),
    )
  
    # Standard footer and author

    invalid_email_message.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    invalid_email_message.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    invalid_email_message.set_author(
        name="Peregrine",
        icon_url="https://cdn.discordapp.com/avatars/716442510423228496/f293e738c3559906120db7e4d43da13e.png?size=256",
    )

    return invalid_email_message