import discord

# Import additional modules

from discord.ext import commands


async def wgu_subscription_embed():

    # Set initial message here

    subMessage = discord.Embed(
        title="Looking to subscribe to various notifications? Just react",
        description="Various categories include announcement channels. Rather than ping the entire guild every time something new is available you can cater your notifications instead. Simply react to the desired category to be notified.\n\n━━━━━━━━━━━━",
        colour=discord.Colour.dark_blue(),
    )

    # Set custom fields here

    subMessage.add_field(
        name="Collegiete Cyber Defense Competition Notifications",
        value="These announcmeents are contributed to us from various resources and are located in [#ccdc-announcements](https://discordapp.com/channels/688822375327989875/756320882225446983).\n┕ :shield: CCDC\n\n━━━━━━━━━━━━",
        inline=False,
    )
    subMessage.add_field(
        name="NICE Cyber Challenge Notifications",
        value="These announcmeents are contributed to us from various resources and are located in [#nice-announcements](https://discordapp.com/channels/688822375327989875/770760554276978688).\n┕ :film_frames: NICE\n\n━━━━━━━━━━━━",
        inline=False,
    )
    subMessage.add_field(
        name="Capture The Flag Notifications",
        value="These announcmeents are related to various CTF events and are located in [#ctf-announcements](https://discordapp.com/channels/688822375327989875/770760554276978688).\n┕ :triangular_flag_on_post: Capture The Flag\n\n━━━━━━━━━━━━",
        inline=False,
    )
    subMessage.add_field(
        name="Hack the Box Notifications",
        value="These announcmeents are related to various CTF events and are located in [#htb-announcements](https://discordapp.com/channels/688822375327989875/770760554276978688).\n┕ :toolbox: HackTheBox\n\n━━━━━━━━━━━━",
        inline=False,
    )
    subMessage.add_field(
        name="Try Hack Me Notifications",
        value="These announcmeents are related to various CTF events and are located in [#thm-announcements](https://discordapp.com/channels/688822375327989875/770760554276978688).\n┕ :postbox: TryHackMe\n\n━━━━━━━━━━━━",
        inline=False,
    )
    subMessage.add_field(
        name="Over The Wire Calendar Notifications",
        value="These announcmeents are related to various CTF events and are located in [#otw-announcements](https://discordapp.com/channels/688822375327989875/770760554276978688).\n┕ :electric_plug: OverTheWire\n\n━━━━━━━━━━━━",
        inline=False,
    )
    subMessage.add_field(
        name="Miscellaneous Foreign Announcements",
        value="These announcmeents are contributed to us from various resources and are located in [#foreign-announcements](https://discordapp.com/channels/688822375327989875/765664389792923688).\n┕ :newspaper: Foreign\n\n━━━━━━━━━━━━",
        inline=False,
    )
    
    # Standard footer and author

    subMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    subMessage.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    subMessage.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )

    return subMessage