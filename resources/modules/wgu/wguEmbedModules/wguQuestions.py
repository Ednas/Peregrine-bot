import discord


async def wguQuestionsEmbed():

    # Set initial message here

    faqMessage = discord.Embed(
        title="Got Questions? We've got answers",
        description="Do you feel lost? Fear not! You're in the right place. We have tutorial videos for reference here, as well as answers to some of our most common questions. As always, you can reach out to one of our moderators directly.\n\n━━━━━━━━━━━━",
        color=discord.Colour.dark_green(),
    )

    # Set custom fields here

    faqMessage.add_field(
        name="Submit via Acclaim",
        value="This is the preferred method to validate your certifications. Click [here](https://www.google.com 'optional hovertext') for instructions.\n\n━━━━━",
        inline=False,
    )
    faqMessage.add_field(
        name="GIAC",
        value="For instructions on validating GIAC certifications, click [here](https://www.google.com 'optional hovertext').",
        inline=True,
    )
    faqMessage.add_field(
        name="CompTIA",
        value="For instructions on validating CompTIA certifications, click [here](https://www.google.com 'optional hovertext').",
        inline=True,
    )
    faqMessage.add_field(
        name="EC-Council",
        value="For instructions on validating EC-Council certifications, click [here](https://www.google.com 'optional hovertext').",
        inline=True,
    )
    faqMessage.add_field(
        name="(ISC)²",
        value="For instructions on validating (ISC)² certifications, click [here](https://www.google.com 'optional hovertext').",
        inline=True,
    )
    faqMessage.add_field(
        name="Offensive Security",
        value="For instructions on validating Offensive Security certifications, click [here](https://www.google.com 'optional hovertext').",
        inline=True,
    )
    faqMessage.add_field(
        name="Cisco",
        value="For instructions on validating Cisco certifications, click [here](https://www.google.com 'optional hovertext').",
        inline=True,
    )
    faqMessage.add_field(
        name="Other",
        value="Don't see what you're certified in? Send it to us in a suggestion [here](https://www.google.com 'optional hovertext')!",
        inline=True,
    )

    # Standard footer and author

    faqMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    faqMessage.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    faqMessage.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )

    return faqMessage