import discord


async def wgu_ncl_embed():

    # Set initial message here

    resourcesMessage = discord.Embed(
        title="Looking for additional resources? You've come to the right place.",
        description="Below you will find a variety of resources in different categories. We try and update this with the most recent and relevant information to assist you in your learning journey. If you have suggestions, we'd love to hear from you!\n\n━━━━━━━━━━━━",
        colour=discord.Colour.dark_blue(),
    )

    # Set custom fields here

    resourcesMessage.add_field(
        name="WGU Student Resources",
        value="A variety of resources are available from the WGU. There are a significant number of free learning tools and software licenses.\n┕ [WGU Student Resources](https://www.wgu.edu/admissions/student-experience/learning-resources.html 'https://www.wgu.edu/admissions/student-experience/learning-resources.html')\n┕ [WGU Alumni](https://www.wgu.edu/alumni.html 'https://www.wgu.edu/alumni.html')\n┕ [WGU DreamSpark Portal](https://wgudreamspark.onthehub.com/WebStore/Welcome.aspx 'https://wgudreamspark.onthehub.com/WebStore/Welcome.aspx')\n\n━━━━━",
        inline=False,
    )
    resourcesMessage.add_field(
        name="Professional Organizations",
        value="Paying your dues can return dividends. The organizations listed here offer a variety of resources as part of your membership.\n┕ [CompTIA Student Membership](https://www.comptia.org/membership/it-pro/student-membership-and-benefits 'https://www.comptia.org/membership/it-pro/student-membership-and-benefits')\n┕ [(ISC)² Membership](https://www.isc2.org/Membership# 'https://www.isc2.org/Membership#')\n┕ [Association of Computing Machinery Student Membership](https://services.acm.org/public/qj/quickjoin/qj_control.cfm?promo=PWEBTOP&form_type=Student 'https://services.acm.org/public/qj/quickjoin/qj_control.cfm?promo=PWEBTOP&form_type=Student')\n\n━━━━━",
        inline=False,
    )
    resourcesMessage.add_field(
        name="Additional Free Resources",
        value="The resources below will give you access to a variety of free software, licenses, and learning tools.\n┕ [Azure Student Starter Pack](https://azure.microsoft.com/en-us/offers/ms-azr-0144p/ 'https://azure.microsoft.com/en-us/offers/ms-azr-0144p/')\n┕ [GitHub Student Developer Pack](https://github.blog/2019-08-20-the-github-student-developer-pack-is-back/ 'https://github.blog/2019-08-20-the-github-student-developer-pack-is-back/')\n┕ [Jet Brains Student Licenses](https://www.jetbrains.com/community/education/#students 'https://www.jetbrains.com/community/education/#students')\n┕ [Tableau Student License](https://www.tableau.com/academic/students 'https://www.tableau.com/academic/students')\n\n━━━━━",
        inline=False,
    )

    # Standard footer and author

    resourcesMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    resourcesMessage.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    resourcesMessage.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )

    return resourcesMessage