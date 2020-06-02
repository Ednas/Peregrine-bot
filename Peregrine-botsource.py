import discord
import re
import subprocess
import sys
import time
import json
import sys
from io import StringIO

BotToken = "token"
urlRegex = '{http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+}'


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
    print("Checking staus...")
    time.sleep(1)
    return rawOutput

def check_State(jsonSHA):
    command = 'python3 ./VxAPI/vxapi.py report_get_state {}'.format(jsonSHA)
    rawOutput = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    formattedOutput = format_Output(rawOutput)
    print("Checking state...")
    time.sleep(1)
    return formattedOutput

def submit_URL(url, message):
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

    checkReportState = check_State(jsonSHA)

    jsonTime = jsonSummary['analysis_start_time']
    jsonAV = jsonSummary['av_detect']
    jsonVerdict = jsonSummary['verdict']
    jsonState = jsonSummary['state']

    print("Compiling data...")

    if jsonState != "SUCCESS":
        formattedSummary = check_State(jsonSHA)
        checkState = convert_JSON(formattedSummary)
        jsonState = checkState['state']
        print("Report is ready! State is: ", jsonState)

    print("Time is:", jsonTime)
    print("AV Detections:", jsonAV)
    print("Verdict:", jsonVerdict)

    analysis = '```Hybrid Analysis Results:\nSubmission Time: {}\nTotal AV Detections: {}\nAnlysis Verdict: {}```*URL has been processed Succesfully*.\n\n\nOriginal Message:\n>>> {}\n- {}\n\n\nPeregrine Discord Protection :bird:'.format(jsonTime, jsonAV, jsonVerdict, message.content, message.author)

    return analysis

    # Demo and cleanup

#        time.sleep(5)
#        await botmessage.edit(content = 'This has been a demo of:\n\n\n```{}```'.format(logo))
#        time.sleep(10)
#        await botmessage.delete()

class Peregrine(discord.Client):
    # Display logo and basic information on successfull login

    async def on_ready(self):
        with open('Peregrine.txt', 'r') as mylogo:
                logo = mylogo.read()
        print('Logged in as')
        print(logo)
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
            await message.delete()
            botmessage = await message.channel.send('Peregrine Discord Malware Protection :bird:\n\n```Do not panic, {}!\nYour URL has been submitted to Hybrid-Analysis for evaluation. Once this process is completed this message will update. Moderators may whitelist this url by issuing command !whitelist <url>\n\n\nAwaiting report.```'.format(message.author))

            for url in urls:
                analysis = submit_URL(url, message)
                await botmessage.edit(content = analysis)
        # Check if poster has moderation bypass

        #

        # Generate report with Hybrid Analysis

client = Peregrine()
client.run(BotToken)
