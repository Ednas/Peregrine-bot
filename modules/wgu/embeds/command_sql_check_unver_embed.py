import discord

async def command_sql_check_unver_embed(issuer_name, email, guild_name):

    # Set initial message here

    verify_log_message = discord.Embed(
        title="Database results",
        description=f"Hello, {issuer_name}\n\nThe database does not contain an entry User email: {email}\n\n\
            This user has not initiated the verification process. Please instruct them to do so.\n\
                \n\nIssued in: {guild_name}",
        colour=discord.Colour.dark_blue(),
    )
  
    # Standard footer and author

    verify_log_message.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    verify_log_message.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    verify_log_message.set_author(
        name="Merlin | Test Branch",
        icon_url="https://cdn.discordapp.com/avatars/805916873480470588/2bbcc095669380edec1641774d217a0d.png?size=256",
    )

    return verify_log_message