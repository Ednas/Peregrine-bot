import discord

async def peregrine_check_status(author_name, guild_name, guild_id, database_status):

    # Set initial message here

    status_embed = discord.Embed(
        title="Current status information",
        description=f"Hello, {author_name}!\n\n\tI am currently connected to: {guild_name}\n\tThe Guild ID is: {guild_id}\n\tDatabase connection status is: {database_status}",
        colour=discord.Colour.dark_blue(),
    )

    # Standard footer and author

    status_embed.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    status_embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    status_embed.set_author(
        name="Merlin | Test Branch",
        icon_url="https://cdn.discordapp.com/avatars/805916873480470588/2bbcc095669380edec1641774d217a0d.png?size=256",
    )

    return status_embed
