import discord

# Import additional modules

from discord.ext import commands


async def wgu_sos_intro_embed():

    # Set initial message here

    sosMessage = discord.Embed(
        title="Justin \"No Raw Talent\" Garcia | U03A9",
        description="Discord Administrator | BS Cyber Security & Information Assurance\n\n━━━━━━━━━━━━━━━━━━━━━━━━━",
        colour=discord.Colour.dark_blue(),
    )
    sosMessage.add_field(
        name="Tell us a little bit about yourself",
        value="Simeon is a Systems Administrator by day and Cyber Security and Privacy Enthusiast by night. He is a tinkerer, a hobbyist, and all around geek and nerd. Simeon got his first start working with a laptop that couldn't even run Windows XP stably at the age of 12. Troubleshooting and fixing issues as they arised, Simeon couldn't get enough. Years later, Simeon now has an in home data-center and lab that rivals most small businesses compute and storage power.\n\n━━━━━",
        inline=False,
    )
    sosMessage.add_field(
        name="Why did you choose WGU?",
        value="It was cheap and fit my schedule. \n━━━━━",
        inline=False,
    )
    sosMessage.add_field(
        name="What's something interesting about you?",
        value="I have more certs than your entire team. :p\n━━━━━",
        inline=False,
    )
    sosMessage.add_field(
        name="Where can we find additional information?",
        value="Links to various platforms are below!\n\t┕ [Blog](https://simeononsecurity.ch/)\n\t┕ [GitHub](https://github.com/simeononsecurity 'https://github.com/simeononsecurity')\n\t┕ [HackTheBox](https://www.hackthebox.eu/home/users/profile/419832 'https://www.hackthebox.eu/home/users/profile/419832')\n\t┕ [TryHackMe](https://tryhackme.com/p/simeononsecurity 'https://tryhackme.com/p/simeononsecurity')\n━━━━━",
        inline=False,
    )
    # Standard footer and author

    sosMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    sosMessage.set_thumbnail(
        url="https://media-exp1.licdn.com/dms/image/C4E35AQEN1_1SZLjf1g/profile-framedphoto-shrink_200_200/0/1611702743840?e=1612663200&v=beta&t=47cw5yMapS1aue9fSngg_tA-vr7f1ZuclQIFenbYSig"
    )
    sosMessage.set_author(
        name="U03A9 | jsherl1",
        icon_url="https://cdn.discordapp.com/avatars/592047479168565272/a_f4ead966c2e7d7ba26bd525a492b21db.gif",
    )

    return sosMessage