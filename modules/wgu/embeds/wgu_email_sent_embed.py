import discord

async def wgu_email_sent_embed(user_email):

    # Set initial message here

    email_sent_message = discord.Embed(
        title="Success!",
        description=f"An email has been sent to {user_email}. Please allow up to 5 minutes for it to arrive. If you do not receive an email, please send a message in [#verification-support](https://discordapp.com/channels/688822375327989875/768993144380981248)",
        colour=discord.Colour.dark_blue(),
    )
  
    email_sent_message.set_image(
        url='https://cdn.discordapp.com/attachments/819072570266877992/823683888877666354/submit_your_pin.gif'
    )
    # Standard footer and author

    email_sent_message.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    email_sent_message.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    email_sent_message.set_author(
        name="Peregrine",
        icon_url="https://cdn.discordapp.com/avatars/716442510423228496/f293e738c3559906120db7e4d43da13e.png?size=256",
    )

    return email_sent_message