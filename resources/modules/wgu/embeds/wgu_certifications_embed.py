import discord


async def wgu_certifications_embed():

    # Set initial message here

    certMessage = discord.Embed(
        title="Trust me, I'm certified.",
        description="Do you carry industry certifications? Want to show them off? We offer that here! The WGU Cyber Club has custom roles to recognize a number of industry certifications. To begin the process, please fill out the requested information [here](https://www.google.com 'optional hovertext'). Roles are assigned within 72 hours of request.\n\nThere are multiple ways to get the information we will request to validate your certification status. If you need assistance, please follow the guides below. In addition, you can reach out to a moderator at any time.\n\n━━━━━━━━━━━━",
        color=discord.Colour.dark_green(),
    )

    # Set custom fields here

    certMessage.add_field(
        name="Submit via Acclaim",
        value="This is the preferred method to validate your certifications. Click [here](https://www.google.com 'optional hovertext') for instructions.\n\n━━━━━",
        inline=False,
    )
    certMessage.add_field(
        name="GIAC",
        value="For instructions on validating GIAC certifications, click [here](https://www.google.com 'optional hovertext').",
        inline=True,
    )
    certMessage.add_field(
        name="CompTIA",
        value="For instructions on validating CompTIA certifications, click [here](https://www.google.com 'optional hovertext').",
        inline=True,
    )
    certMessage.add_field(
        name="EC-Council",
        value="For instructions on validating EC-Council certifications, click [here](https://www.google.com 'optional hovertext').",
        inline=True,
    )
    certMessage.add_field(
        name="(ISC)²",
        value="For instructions on validating (ISC)² certifications, click [here](https://www.google.com 'optional hovertext').",
        inline=True,
    )
    certMessage.add_field(
        name="Offensive Security",
        value="For instructions on validating Offensive Security certifications, click [here](https://www.google.com 'optional hovertext').",
        inline=True,
    )
    certMessage.add_field(
        name="Cisco",
        value="For instructions on validating Cisco certifications, click [here](https://www.google.com 'optional hovertext').",
        inline=True,
    )
    certMessage.add_field(
        name="Other",
        value="Don't see what you're certified in? Send it to us in a suggestion [here](https://www.google.com 'optional hovertext')!",
        inline=True,
    )

    # Standard footer and author

    certMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    certMessage.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    certMessage.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )

    return certMessage