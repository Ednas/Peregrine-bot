import discord


async def wgu_ncl_embed():

    # Set initial message here

    resourcesMessage = discord.Embed(
        title="The National Cyber League",
        description="Welcome to the big leagues!\n\nThe NCL and Cyber Skyline host a collegiete level compeition where you can showcase your cyber skills. The WGU Cyber Club participated in the Fall 2020 competition and many members of our club placed among the top 500 players.\n\n━━━━━━━━━━━━",
        colour=discord.Colour.dark_blue(),
    )

    # Set custom fields here

    resourcesMessage.add_field(
        name="How to register",
        value="In order to participate in the NCL competition you will need to register an account [here](https://cyberskyline.com/events/ncl/welcome 'https://cyberskyline.com/events/ncl/welcome'). You need to meet the following requirements to participate\n   ┕ You must be a student with an active .edu email\n   ┕ You must agree to the rules of conduct [here](https://nationalcyberleague.org/ncl-rules 'https://nationalcyberleague.org/ncl-rules') \n\n━━━━━",
        inline=False,
    )
    resourcesMessage.add_field(
        name="Gymnasium - February 15th - May 28th",
        value="The Gymnasium will be where you test your skills. We encourage everyone to spend time in the Gymnasium and will have dedicated streams among participants on Fridays hosted by <@592047479168565272>\n   ┕ Fridays from 5:00PM - 7:00PM PST \n   ┕ Sundays from 1:00PM - 3:00PM PST\n\n━━━━━",
        inline=False,
    )
    resourcesMessage.add_field(
        name="Team Game - April 9th - April 11th",
        value="You can start your own team and register it on the board or contact the leader of a team listed below to be considered for theirs. There is no limit on the number of teams WGU may put forth, so lets take over the leaderboard!\n   ┕ The Fowl Owls | <@440718209205927937>\n   ┕ Parliament of Owls | <@246784517778571264>\n\n━━━━━",
        inline=False,
    )
    resourcesMessage.add_field(
        name="Team Game - April 9th - April 11th",
        value="You can start your own team and register it on the board or contact the leader of a team listed below to be considered for theirs. There is no limit on the number of teams WGU may put forth, so lets take over the leaderboard!\n   ┕ The Fowl Owls | <@440718209205927937>\n   ┕ Parliament of Owls | <@246784517778571264>\n\n━━━━━",
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