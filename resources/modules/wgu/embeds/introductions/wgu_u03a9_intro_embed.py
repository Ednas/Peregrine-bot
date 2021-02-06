import discord

# Import additional modules

from discord.ext import commands


async def wgu_u03a9_intro_embed():

    # Set initial message here

    u03a9Message = discord.Embed(
        title="Justin \"No Raw Talent\" Garcia | U03A9",
        description="Discord Administrator | BS Cyber Security and Information Assurance | Student\n\n",
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

    u03a9Message.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    u03a9Message.set_thumbnail(
        url="https://media-exp1.licdn.com/dms/image/C4E35AQEN1_1SZLjf1g/profile-framedphoto-shrink_200_200/0/1611702743840?e=1612663200&v=beta&t=47cw5yMapS1aue9fSngg_tA-vr7f1ZuclQIFenbYSig"
    )
    u03a9Message.set_author(
        name="U03A9 | jsherl1",
        icon_url="https://cdn.discordapp.com/avatars/592047479168565272/a_f4ead966c2e7d7ba26bd525a492b21db.gif",
    )

    return u03a9Message