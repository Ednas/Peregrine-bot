import discord
import re
import subprocess
import sys
import os
import time
import json

from sys import platform
from io import StringIO
from colorama import init
from termcolor import colored


def analyzeSubmitUrl():

    # Build out card for placeholder

    peregrineCatchMessage = discord.Embed(
        Title="Peregrine: Discord Malware Protection",
        description="Peregrine malware defense has been deployed in this discord. This message is triggered when an unknown URL is posted in the server.\n\n━━━━━━━━━━━━",
        colour=discord.Colour.dark_orange(),
    )

    peregrineCatchMessage.add_field(
        name="Original Message",
        value="```\n{}\n\n\tAuthor:{}```\n\n━━━━━━━━━━━━".format(
            storedMessage.content, storedMessage.author
        ),
        inline=False,
    )

    peregrineCatchMessage.add_field(
        name="URL Submitted",
        value="This URL was not recognized and has been submitted to Hybrid-Analysis for evaluation. Once this process is completed this message will update.",
        inline=False,
    )

    # Standard footer and author for Peregrine scans

    peregrineCatchMessage.set_footer(
        text="Peregrine Malware Defense | Gem State Cyber | justin@gemstatecyber.com"
    )
    peregrineCatchMessage.set_author(
        name="Peregrine",
        icon_url="https://cdn.discordapp.com/avatars/716442510423228496/74b93108c3bcc7aff5b4814f71310ba4.png",
    )

    peregreineMessagePlaceholder = await message.channel.send(
        embed=peregrineCatchMessage
    )

    # Verify URLs and check their results

    for url in urls:

        print("URL detected in message ID: ", storedMessage.id)
        print("Initiating scan on URL: ", url)
        analysisMessage = vxapi.main()
        print("Analysis message: ", analysisMessage)
        # Build card for analysis results message

        peregrineAnalysisMessage = discord.Embed(
            Title="Peregrine: Discord Malware Protection",
            description="Peregrine malware defense has been deployed in this discord. This message is triggered when an unknown URL is posted in the server.\n\n━━━━━━━━━━━━",
            colour=discord.Colour.dark_orange(),
        )
        peregrineAnalysisMessage.add_field(
            name="Analysis Results",
            value="```\n{}\n```".format(analysisMessage),
            inline=False,
        )
        peregrineAnalysisMessage.add_field(
            name="Original Message",
            value="```\n{}\n\n\t\tAuthor:{}```".format(
                storedMessage.content, storedMessage.author
            ),
            inline=False,
        )

        # Standard footer and author

        peregrineAnalysisMessage.set_footer(
            text="Peregrine Malware Defense | Gem State Cyber | justin@gemstatecyber.com"
        )
        peregrineAnalysisMessage.set_author(
            name="Peregrine",
            icon_url="https://cdn.discordapp.com/avatars/716442510423228496/74b93108c3bcc7aff5b4814f71310ba4.png",
        )

        await peregreineMessagePlaceholder.edit(embed=peregrineAnalysisMessage)
