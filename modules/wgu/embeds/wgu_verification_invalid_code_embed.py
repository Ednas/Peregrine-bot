import discord

async def wgu_verification_invalid_code_embed(submitted_auth_code):

    # Set initial message here

    invalid_pin_message = discord.Embed(
        title="Invalid pin!",
        description=f"The pincode: {submitted_auth_code} does not match our records. Please double-check the code you submitted. If you are confident that you have submitted the correct code, please send a message in [#verification-support](https://discordapp.com/channels/688822375327989875/768993144380981248)",
        colour=discord.Colour.dark_blue(),
    )
  
    # Standard footer and author

    invalid_pin_message.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    invalid_pin_message.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    invalid_pin_message.set_author(
        name="Merlin | Test Branch",
        icon_url="https://cdn.discordapp.com/avatars/805916873480470588/2bbcc095669380edec1641774d217a0d.png?size=256",
    )

    return invalid_pin_message