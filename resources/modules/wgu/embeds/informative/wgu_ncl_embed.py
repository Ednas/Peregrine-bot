import discord


async def wgu_ncl_embed():

    # Set initial message here

    nclMessage = discord.Embed(
        title="The National Cyber League",
        description="Welcome to the big leagues!\n\nThe NCL and Cyber Skyline host a collegiete level compeition where you can showcase your cyber skills. The WGU Cyber Club participated in the Fall 2020 competition and many members of our club placed among the top 500 players. We will be announcing various rankings, statistics, and interviewing our student peers live with additional information in [#ncl-live-coverage](https://www.discordapp.com/688822375327989875/806030856606318652). Be sure to join us for the streams in the voice channel!\n\n━━━━━━━━━━━━",
        colour=discord.Colour.dark_blue(),
    )

    # Set custom fields here

    nclMessage.add_field(
        name="How to register",
        value="In order to participate in the NCL competition you will need to register an account [here](https://cyberskyline.com/events/ncl/welcome 'https://cyberskyline.com/events/ncl/welcome'). You need to meet the following requirements to participate\n\n   ┕ You must be a student with an active .edu email\n   ┕ You must agree to the rules of conduct [here](https://nationalcyberleague.org/ncl-rules 'https://nationalcyberleague.org/ncl-rules') \n\n━━━━━",
        inline=False,
    )
    nclMessage.add_field(
        name="Gymnasium - February 15th - May 28th",
        value="The Gymnasium will be where you test your skills. We encourage everyone to spend time in the Gymnasium and will have dedicated streams among participants on Fridays hosted by <@592047479168565272>\n\n   ┕ Fridays from 5:00PM - 7:00PM PST\n   ┕ Sundays from 1:00PM - 3:00PM PST\n\n━━━━━",
        inline=False,
    )
    nclMessage.add_field(
        name="NCL Preseason - March 15th - March 22nd",
        value="PLACEMENTS! Important: YOU MUST COMPETE IN PRESEASON TO QUALIFY FOR THE INDIVIDUAL AND TEAM GAMES.\n\n Welcome to the CYBERDOME! This is where your practice pays off and sets you apart from your student peers. The objective in preseason is to assess which rank you belong in in order to measure the individual skill among participants in the league games.\n\n   ┕ Gold - Top 15\% \of qualified players or teams\n   ┕ Silver - Next 35\% \of qualified players or teams\n   ┕ Bronze - Remaining 50\% \of qualified players or teams\n   ┕ Pewter - All coaches and unqualified players \n\n━━━━━",
        inline=False,
    )
    nclMessage.add_field(
        name="Individual Game - March 26th - March 28th",
        value="Earn your bragging rights. This is a cutthroat freeforall Capture-The-Flag in a jeopardy style. A variety of categories will be available with challenges similar to those in the NCL Gymnasium and Preseason. Top 10 WGU students will earn themselves a special role and a mention in our [#ncl-hall-of-fame](https://www.discordapp.com/688822375327989875/806031790430093312)\n\n━━━━━",
        inline=False,
    )
    nclMessage.add_field(
        name="Team Game - April 9th - April 11th",
        value="You can start your own team and register it on the board or contact the leader of a team listed below to be considered for theirs. There is no limit on the number of teams WGU may put forth, so lets take over the leaderboard!\n\n   ┕ The Fowl Owls | <@440718209205927937>\n   ┕ Parliament of Owls | <@246784517778571264>\n\nIf you would like to add your team to this recruitment board please contact any of our moderators or administrators.\n\n━━━━━",
        inline=False,
    )

    # Standard footer and author

    nclMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    nclMessage.set_thumbnail(
        url="https://images.squarespace-cdn.com/content/5e13a4b584a68c775e362068/1607517723861-XBVA0ONKL21ZROH9C44C/NCL+Powered+By+Cyber+Skyline+Monotone+Logo+copy.png?content-type=image%2Fpng"
    )
    nclMessage.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )

    return nclMessage