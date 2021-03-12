import discord

async def command_sql_check_auth_embed(issuer_name, email, ver_date, discord_nick, user_id, guild_name):

    # Set initial message here

    verify_log_message = discord.Embed(
        title="Database results",
        description=f"Hello, {issuer_name}\n\nThe Database contains the following in the `auth` table for: {email}\n\n\
            Verified on: {ver_date}\nDiscord Nickname: {discord_nick}\nDiscord ID: {user_id}\
                \n\nThis user has not completed the verification process. Please instruct them to check their email\
                and issue the `!verify <pin>` command to the bot to finish verifying\
                \n\nIssued In: {guild_name}",
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