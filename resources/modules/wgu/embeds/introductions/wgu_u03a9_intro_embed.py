import discord

# Import additional modules

from discord.ext import commands


async def wgu_u03a9_intro_embed():

    # Set initial message here

    u03a9Message = discord.Embed(
        title="Justin \"No Raw Talent\" Garcia | U03A9",
        description="Discord Administrator | BS Cyber Security and Information Assurance | Student\n\n"
        colour=discord.Colour.dark_blue(),
    )
    u93a9Message.add_field(
        name="About me",
        value="I transitioned into the IT realm in late 2018 after spending nearly a decade working in retail sales. I worked for RadioShack, Verizon, Sprint, AT&T, and other various cellular authorized retailers from 2008 to 2018. I got my start on a Help Desk with a Google Support Professional certificate I earned from Coursera. I had the unique opportunity to put my hands on a lot of systems and act as a Jr. Systems Administrator early on in my career. In addition, I stumbled across a documentary about Stuxnet and immediately became fascinated with Cyber Security. I spent 2 years self studying additional Computer Science, Cyber Law, Cyber Security, and .\n\n━━━━━",
        inline=False,
    )
    u93a9Message.add_field(
        name="Q: I'm new to Discord, where can I learn more about it?",
        value="A: You can find additional information about Discord [here](https://support.discord.com/hc/en-us/categories/115000217151 'https://support.discord.com/hc/en-us/categories/115000217151').\n\n━━━━━",
        inline=False,
    )
    # Standard footer and author

    successMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    successMessage.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    successMessage.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )

    return successMessage