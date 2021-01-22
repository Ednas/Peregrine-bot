import discord

# Import additional modules

from discord.ext import commands


async def wgu_roles_embed():

    # Set initial message here

    rolesMessage = discord.Embed(
        title="You want em? We've got em.",
        description="Get your roles here! Simply react with the appropriate emoji to autmoatically receive your role. If you're looking to get roles related to your industry certifications, please visit [#cert-verification](https://discordapp.com/channels/688822375327989875/757159500091228170) to begin the process!\n\n━━━━━",
        colour=discord.Colour.dark_blue(),
    )

    # Set custom fields here

    rolesMessage.add_field(
        name="Enrollment Status",
        value="┕ :man_student: Student\n┕ :mortar_board: Alumni\n\n━━━━━━━━━━━━",
        inline=False,
    )


    # Standard footer and author

    rolesMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    rolesMessage.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    rolesMessage.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )

    return rolesMessage