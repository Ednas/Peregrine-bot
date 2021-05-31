import discord

async def perri_command_help_embed(issuer_name, guild_name, perri_commands, perri_command_docstrings):

    # Set initial message here

    perri_help_message = discord.Embed(
        title="Perri the Peregrine: Discord Management for Virtual Campus Clubs",
        description=f"""Hello {issuer_name},

        I'm Perri, a Discord bot whom provides the administrators and moderators
        of the guild a convenient way to manage student access and verification. If
        you would like to know more about a particular command, issue the following

        `!help <command name>`

        The following additional information is available for {guild_name}""",
        colour=discord.Colour.dark_blue(),
    )

    # Set commands field

    perri_help_message.add_field(
        name=f"Available commands",
        value=f"━━━━━━━━━━━━",
        inline=False
    )

    # Dynamically spawn fields with commands

    count = 0
    while count != len(perri_commands):
        for command in perri_commands:

            if command == "perri" or command == "help":
                count = count + 1
                continue

            else:

                perri_help_message.add_field(
                    name=f"__**{command}**__",
                    value=f"{perri_command_docstrings[count]}",
                    inline=True
                )
                count = count + 1
            
    # Set additional fields

    perri_help_message.add_field(
        name=f"Additional information",
        value=f"Test field\n━━━━━━━━━━━━",
        inline=False
    )

    # Standard footer and author

    perri_help_message.set_footer(
        text="This bot is under active development. If you have information or feedback you feel is important to provide the active developer, please reach out to a member of club leadership."
    )
    perri_help_message.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    perri_help_message.set_author(
        name="Peregrine",
        icon_url="https://cdn.discordapp.com/avatars/716442510423228496/f293e738c3559906120db7e4d43da13e.png?size=256",
    )

    return perri_help_message