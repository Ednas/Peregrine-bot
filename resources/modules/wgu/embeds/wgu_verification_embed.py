import discord


async def wgu_verification_embed():

    # Set initial message here

    verifyMessage = discord.Embed(
        title="Welcome to the Official WGU Cyber Club Discord!",
        description="This is a private Discord for students in the School of IT. Access is controlled and you will need to verify your identity and enrollment status with our bot.\n\n━━━━━━━━━━━━",
        colour=discord.Colour.dark_blue(),
    )

    # Set custom fields here

    verifyMessage.add_field(
        name="Housekeeping",
        value="Since this Discord is run and sponsored by WGU, verification of your identity is non-negoitable. You will be required to set your [server nickname](https://www.businessinsider.com/how-to-change-nickname-on-discord 'Click here for help (https://www.businessinsider.com/how-to-change-nickname-on-discord)') to the following format\n\n`<User Handle> | <WGU Username>`\n\nIf you would prefer to join this Discord with a new account, please click [here](https://discord.com/register 'Register account (https://discord.com/register)') and create a new Discord account using your WGU email address instead.\n\n━━━━━━━━━━━━",
        inline=False,
    )
    verifyMessage.add_field(
        name="You agree",
        value="By verifying your identity you certify and acknowledge that\n┕ You are a student or alumni of the WGU School of IT.\n┕ You agree to follow club nickname guidelines.\n┕ You agree to present yourself in a professional manner.\n┕ You agree to all bylaws outlined in the Cyber Club Constitution available [here](https://cm.wgu.edu/t5/Cyber-Security-Club/WGU-Cybersecurity-Club-Constitution-and-By-Laws/ta-p/24789 'WGU Club Bylaws (https://cm.wgu.edu/t5/Cyber-Security-Club/WGU-Cybersecurity-Club-Constitution-and-By-Laws/ta-p/24789)').\n\n━━━━━━━━━━━━",
        inline=False,
    )
    verifyMessage.add_field(
        name="Ready?",
        value="If you are ready to proceed with the verification process, please react to this message with a ✅. You will receive a DM from our verification bot with further instructions. If you require assistance, please visit [#support](https://discordapp.com/channels/688822375327989875/797540968790360084/799817535662587914) on your left.\n\n━━━━━━━━━━━━",
        inline=False,
    )

    # Standard footer and author

    verifyMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    verifyMessage.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    verifyMessage.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )

    return verifyMessage