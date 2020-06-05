import discord
import re
import subprocess
import sys
import time
import json
import sys
import colorama
from io import StringIO

from colorama import init
from termcolor import colored

BotToken = "NzE2NDQyNTEwNDIzMjI4NDk2.Xtmu_Q.gMJB8dtNddQOKeJIs9KbHeyjOyI"
urlRegex = '{http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+}'
analysisMessage = ""
analysisFull = ""
botmessage = ""

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
    command = 'python3 ./VxAPI/vxapi.py scan_url_for_analysis {} all'.format(url)
    rawOutput = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    print("Scanning URL...")
    time.sleep(1)

    return rawOutput

def check_Status(jsonSHA):
    command = 'python3 ./VxAPI/vxapi.py report_get_summary {}'.format(jsonSHA)
    rawOutput = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    print("Checking scan status...")
    time.sleep(1)
    return rawOutput

def check_Overview(jsonSHA):
    command = 'python3 ./VxAPI/vxapi.py overview_get {}'.format(jsonSHA)
    rawOutput = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    print("Retreiving overview variables...")
    time.sleep(1)
    return rawOutput

def check_State(jsonSHA):
    command = 'python3 ./VxAPI/vxapi.py report_get_state {}'.format(jsonSHA)
    rawOutput = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    formattedOutput = format_Output(rawOutput)
    print("Checking state...")
    time.sleep(1)
    return formattedOutput

async def submit_URL(url, message):
    with open('resources/analysis_Message.txt', 'r') as analysis_Message:
            scanMessage = analysis_Message.read()

    decoded = scan_URL(url)

    formattedUrl = format_Output(decoded)
    jsonUrl = convert_JSON(formattedUrl)

    jsonID = jsonUrl['id']
    jsonSHA = jsonUrl['sha256']

    print("The jsonID is: ",jsonID)
    print("The jsonSHA is: ",jsonSHA)

    checkSummary = check_Status(jsonSHA)
    formattedSummary = format_Output(checkSummary)
    jsonSummary = convert_JSON(formattedSummary)

    jsonTime = jsonSummary['analysis_start_time']
    jsonAV = jsonSummary['av_detect']
    jsonState = jsonSummary['state']

    checkOverview = check_Overview(jsonSHA)
    formattedOverview = format_Output(checkOverview)
    jsonOverview = convert_JSON(formattedOverview)

    jsonArchitecture = jsonOverview['architecture']
    jsonThreatScore = jsonOverview['threat_score']
    jsonVerdict = jsonOverview['verdict']

    print("Compiling data...")

    if jsonState != "SUCCESS":
        formattedSummary = check_State(jsonSHA)
        checkState = convert_JSON(formattedSummary)
        jsonState = checkState['state']
        print("Report is ready! State is: ", jsonState)

    print("Time is:", jsonTime)
    print("AV Detections:", jsonAV)
    print("Verdict:", jsonVerdict)

    analysisMessage = str(scanMessage).format(jsonArchitecture, url, jsonTime, jsonAV, jsonVerdict,  jsonThreatScore)

    return analysisMessage

    # Demo and cleanup

#        time.sleep(5)
#        await botmessage.edit(content = 'This has been a demo of:\n\n\n```{}```'.format(logo))
#        time.sleep(10)
#        await botmessage.delete()

class Peregrine(discord.Client):
    # Display logo and basic information on successfull login

    async def on_ready(self):
        with open('resources/logo.txt', 'r') as mylogo:
                logo = mylogo.read()
        print('Logged in as')
        print(colored(logo, 'red'))
        print(self.user.id)

    async def on_message(self, message):

        # Prevent bot replying to self

        if message.author.id == self.user.id:
            return

        # Check message for commands

        if message.content.startswith('!peregrine'):
            channel = message.channel
            return
            if message.content.endswith('status'):
                await channel.send('Status: Logged In')
                return

        # Check message for urls
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content.lower())

        if urls:

            try:

                with open('resources/quote_Message.txt', 'r') as quote_File:
                        quote_Message = quote_File.read()
                await message.delete()
                botmessage = ""
                botmessage = await message.channel.send('Peregrine Discord Malware Protection :bird:\n\n```Do not panic, {}!\nYour URL has been submitted to Hybrid-Analysis for evaluation.\nOnce this process is completed this message will update.\n\n\nAwaiting report.```'.format(message.author))
                analysisMessage = ""
                analysisFull = ""

                for url in urls:
                    print("URL detected in message ID: ", message.id)
                    print("Initiating scan on URL: ", url)
                    analysisMessage = await submit_URL(url, message)
                    analysisFull = analysisFull + analysisMessage + "\n"
                    fullMessage = "```" + analysisFull + "```" + "\n" + quote_Message.format(message.content, message.author)

                await botmessage.edit(content = fullMessage)

            except Exception:

                await botmessage.edit(content = 'Could not process url.')
                time.sleep(3)

        # Check if poster has moderation bypass

        #

        # Generate report with Hybrid analysis_Message

client = Peregrine()
client.run(BotToken)
