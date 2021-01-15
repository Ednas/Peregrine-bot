import discord


async def wgu_faq_embed():

    # Set initial message here

    faqMessage = discord.Embed(
        title="Got Questions? We've got answers",
        description="Do you feel lost? Fear not! You're in the right place. We have tutorial videos for reference here, as well as answers to some of our most common questions. As always, you can reach out to one of our moderators directly.\n\n━━━━━━━━━━━━",
        color=discord.Colour.dark_green(),
    )

    # Set custom fields here

    faqMessage.add_field(
        name="Q: I'm new to Discord, where can I learn more about it?",
        value="A: You can find additional information about Discord [here](https://support.discord.com/hc/en-us/categories/115000217151 'https://support.discord.com/hc/en-us/categories/115000217151').\n\n━━━━━",
        inline=False,
    )
    faqMessage.add_field(
        name="Q: Why did I need to verify my identity? I like being anonymous on Discord.",
        value="A: This is an excellent question. This Discord Guild is officially sponsored by the WGU Cyber Club and Western Governors University. As such, we cannot allow anonymity on this server for several reasons. We verify identity of all members to control access to this private server and ensure a high level of accountability to each other. If you are concerned about anonymity on Discord, it may be best to create a separate Discord account with your WGU email. This will allow you to keep your identities separate.\n\n━━━━━",
        inline=False,
    )
    faqMessage.add_field(
        name="Q: Why did I need to change my nickname for this Discord?",
        value='A: To further support our goals of accountability we require all users to utilize a standard nickname format. Do not worry, your nickname is specific to this server and does not affect others. This allows your peers to find you on other school platforms. In addition, you can begin to build your personal brand surrounding your pseudonym (sometimes called a "Hacker Handle") among potential future coworkers or employers. We have a diverse group of students in this University, and you never know what sorts of doors may open while you are here. Make the most of it and have fun!\n\n━━━━━',
        inline=False,
    )
    faqMessage.add_field(
        name="Q: Is there any additional resources I should know about?",
        value="A: In addition to our growing list located in [#student-resources](https://discord.com/channels/655170668660523070/787767748981161985/787767778869903372), you can find additional information from the [WGU Student Resources](https://www.wgu.edu/admissions/student-experience/learning-resources.html 'https://www.wgu.edu/admissions/student-experience/learning-resources.html') page, the [WGU Alumni](https://www.wgu.edu/alumni.html 'https://www.wgu.edu/alumni.html') page and on the [WGU DreamSpark Portal](https://wgudreamspark.onthehub.com/WebStore/Welcome.aspx 'https://wgudreamspark.onthehub.com/WebStore/Welcome.aspx').\n\n━━━━━",
        inline=False,
    )
    faqMessage.add_field(
        name="Q: Where can I find information on upcoming events such as Capture-The-Flag?",
        value="A: We maintain several channel categories, which you can find on the left side of the client, dedicated to Cyber Challenges, Cyber Competitions, and Capture the Flag events. In addition, we make announcements that will alert the Guild when new events are coming up! Keep an eye out for those announcements!\n\n━━━━━━━━━━━━",
        inline=False,
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