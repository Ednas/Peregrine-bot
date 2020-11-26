#!/bin/python3

import discord
from discord.ext import commands

import re
import subprocess
import sys
import time
import json
import sys
from io import StringIO

from colorama import init
from termcolor import colored

BotToken = "NzE2NDQyNTEwNDIzMjI4NDk2.XwCk9w.BFQu2Cda65qhxoAUQvOmidEBdXs"
analysisMessage = ""
analysisFull = ""


def convert_Output(rawOutput):
    readOutput = rawOutput.read()
    decoded = readOutput.decode()
    return decoded


def convert_JSON(formattedOutput):
    jsonOutput = json.loads(formattedOutput)
    return jsonOutput


def format_Output(rawOutput):
    formattedOutput = convert_Output(rawOutput)

    return formattedOutput


def scan_URL(url):
    command = "python3 ./VxAPI/vxapi.py scan_url_for_analysis {} all".format(url)
    rawOutput = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    print("Scanning URL...")
    time.sleep(1)

    return rawOutput


def check_Status(jsonSHA):
    command = "python3 ./VxAPI/vxapi.py report_get_summary {}".format(jsonSHA)
    rawOutput = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    print("Checking scan status...")
    time.sleep(1)
    return rawOutput


def check_Overview(jsonSHA):
    command = "python3 ./VxAPI/vxapi.py overview_get {}".format(jsonSHA)
    rawOutput = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    print("Retreiving overview variables...")
    time.sleep(1)
    return rawOutput


def check_State(jsonSHA):
    command = "python3 ./VxAPI/vxapi.py report_get_state {}".format(jsonSHA)
    rawOutput = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    formattedOutput = format_Output(rawOutput)
    print("Checking state...")
    time.sleep(1)
    return formattedOutput


async def submit_URL(url, message):
    with open("resources/analysis_Message.txt", "r") as analysis_Message:
        scanMessage = analysis_Message.read()

    decoded = scan_URL(url)

    formattedUrl = format_Output(decoded)
    jsonUrl = convert_JSON(formattedUrl)

    jsonID = jsonUrl["id"]
    jsonSHA = jsonUrl["sha256"]

    print("The jsonID is: ", jsonID)
    print("The jsonSHA is: ", jsonSHA)

    checkSummary = check_Status(jsonSHA)
    formattedSummary = format_Output(checkSummary)
    jsonSummary = convert_JSON(formattedSummary)

    jsonTime = jsonSummary["analysis_start_time"]
    jsonAV = jsonSummary["av_detect"]
    jsonState = jsonSummary["state"]

    checkOverview = check_Overview(jsonSHA)
    formattedOverview = format_Output(checkOverview)
    jsonOverview = convert_JSON(formattedOverview)

    jsonArchitecture = jsonOverview["architecture"]
    jsonThreatScore = jsonOverview["threat_score"]
    jsonVerdict = jsonOverview["verdict"]

    print("Compiling data...")

    if jsonState != "SUCCESS":
        formattedSummary = check_State(jsonSHA)
        checkState = convert_JSON(formattedSummary)
        jsonState = checkState["state"]
        print("Report is ready! State is: ", jsonState)

    print("Time is:", jsonTime)
    print("AV Detections:", jsonAV)
    print("Verdict:", jsonVerdict)

    analysisMessage = str(scanMessage).format(
        jsonArchitecture, url, jsonTime, jsonAV, jsonVerdict, jsonThreatScore
    )

    return analysisMessage

    # Demo and cleanup


#        time.sleep(5)
#        await botmessage.edit(content = 'This has been a demo of:\n\n\n```{}```'.format(logo))
#        time.sleep(10)
#        await botmessage.delete()


class Peregrine(discord.Client):
    # Display logo and basic information on successfull login

    async def on_ready(self):
        with open("resources/logo.txt", "r") as mylogo:
            logo = mylogo.read()
        print(colored(logo, "red"))
        print(colored(self.user.id, "red"))

    async def on_message(self, message):

        # Prevent bot replying to self

        if message.author.id == self.user.id:
            return

        # Check message for commands

        if message.content.startswith("!peregrine"):
            print("Hello: {}".format(message.author))

            if message.content.endswith("status"):
                print("Printing status to: {}".format(message.channel))
                await message.channel.send("Status: Logged In")
                return

        # Check message for urls
        urls = re.findall(
            r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            message.content.lower(),
        )

        if urls:

            try:

                with open("resources/quote_Message.txt", "r") as quote_File:
                    quote_Message = quote_File.read()
                await message.delete()
                botmessage = ""
                botmessage = await message.channel.send(
                    "Peregrine Discord Malware Protection :bird:\n\n```Do not panic, {}!\nYour URL has been submitted to Hybrid-Analysis for evaluation.\nOnce this process is completed this message will update.\n\n\nAwaiting report.```".format(
                        message.author
                    )
                )
                analysisMessage = ""
                analysisFull = ""

                for url in urls:
                    print("URL detected in message ID: ", message.id)
                    print("Initiating scan on URL: ", url)
                    analysisMessage = await submit_URL(url, message)
                    analysisFull = analysisFull + analysisMessage + "\n"
                    fullMessage = (
                        "```"
                        + analysisFull
                        + "```"
                        + "\n"
                        + quote_Message.format(message.content, message.author)
                    )
                    await botmessage.edit(content=fullMessage)

            except Exception as e:

                print(e)
                message = "Could not process url."
                await botmessage.send(content=message)
                time.sleep(3)

        if message.content.startswith("!verify"):

            # Set initial message here

            verifyMessage = discord.Embed(
                title="Welcome to the Official WGU Cyber Club Discord!",
                description="This is a private Discord for students in the School of IT. In order to proceed to the Discord, you will need to verify your identity and enrollment status with our bot.\n\n━━━━━━━━━━━━",
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
                value="If you are ready to proceed with the verification process, please react to this message with a :white_check_mark:. You will receive a DM from our verification bot with further instructions. If you require assistance, please visit #verification-support on your left.\n\n━━━━━━━━━━━━",
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

            await message.channel.send(embed=verifyMessage)

        if message.content.startswith("!certs"):

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

            await message.channel.send(embed=certMessage)

        return

        # Check if poster has moderation bypass

        # Code goes here for mod bypass


client = Peregrine()
client.run(BotToken)
