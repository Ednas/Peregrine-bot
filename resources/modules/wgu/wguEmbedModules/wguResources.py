import discord


async def wguResourcesEmbed():

    # Set initial message here

    resourcesMessage = discord.Embed(
        title="Looking for additional resources? You've come to the right place.",
        description="Below you will find a variety of resources in different categories. We try and update this with the most recent and relevant information to assist you in your learning journey. If you have suggestions, we'd love to hear from you!\n\n━━━━━━━━━━━━",
        colour=discord.Colour.dark_blue(),
    )

    # Set custom fields here

    resourcesMessage.add_field(
        name="WGU Student Resources",
        value="Since this Discord is run and sponsored by WGU, verification of your identity is non-negoitable. You will be required to set your [server nickname](https://www.businessinsider.com/how-to-change-nickname-on-discord 'Click here for help (https://www.businessinsider.com/how-to-change-nickname-on-discord)') to the following format\n\n`<User Handle> | <WGU Username>`\n\nIf you would prefer to join this Discord with a new account, please click [here](https://discord.com/register 'Register account (https://discord.com/register)') and create a new Discord account using your WGU email address instead.\n\n━━━━━━━━━━━━",
        inline=False,
    )
    resourcesMessage.add_field(
        name="Professional Organizations",
        value="By verifying your identity you certify and acknowledge that\n┕ You are a student or alumni of the WGU School of IT.\n┕ You agree to follow club nickname guidelines.\n┕ You agree to present yourself in a professional manner.\n┕ You agree to all bylaws outlined in the Cyber Club Constitution available [here](https://cm.wgu.edu/t5/Cyber-Security-Club/WGU-Cybersecurity-Club-Constitution-and-By-Laws/ta-p/24789 'WGU Club Bylaws (https://cm.wgu.edu/t5/Cyber-Security-Club/WGU-Cybersecurity-Club-Constitution-and-By-Laws/ta-p/24789)').\n\n━━━━━━━━━━━━",
        inline=False,
    )
    resourcesMessage.add_field(
        name="Free Software",
        value="If you are ready to proceed with the verification process, please react to this message with a :white_check_mark:. You will receive a DM from our verification bot with further instructions. If you require assistance, please visit #verification-support on your left.\n\n━━━━━━━━━━━━",
        inline=False,
    )
    resourcesMessage.add_field(
        name="Free Learning",
        value="If you are ready to proceed with the verification process, please react to this message with a :white_check_mark:. You will receive a DM from our verification bot with further instructions. If you require assistance, please visit #verification-support on your left.\n\n━━━━━━━━━━━━",
        inline=False,
    )
    resourcesMessage.add_field(
        name="Paid Learning",
        value="If you are ready to proceed with the verification process, please react to this message with a :white_check_mark:. You will receive a DM from our verification bot with further instructions. If you require assistance, please visit #verification-support on your left.\n\n━━━━━━━━━━━━",
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