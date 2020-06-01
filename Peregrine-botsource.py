import discord
import re
import subprocess
import sys
import time
import json
import sys
from io import StringIO

with open('Peregrine.txt', 'r') as mylogo:
    logo = mylogo.read()

def convert_Output(x):
    s = x.read()
    rawOutput = s.decode()
    return rawOutput

def mask_URL(url, message):

    u = url[0]
    trimmedMessage = message.replace(str(u), "[submitted]")
    return trimmedMessage

def convert_JSON(formattedOutput):

     jsonOutput = json.loads(formattedOutput)
     return jsonOutput

def format_Output(rawOutput):

    formattedOutput = convert_Output(rawOutput)

    return formattedOutput

def scan_URL(url):

    u = url[0]
    command = 'python3 ./VxAPI/vxapi.py scan_url_for_analysis {} all'.format(u)
    print("Executing command: {}".format(command))
    rawOutput = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout

    time.sleep(10)
    return rawOutput


def check_Status(jsonSHA):

        command = 'python3 ./VxAPI/vxapi.py report_get_summary {}'.format(jsonSHA)
        print("Executing command: {}".format(command))
        rawOutput = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout

        time.sleep(10)
        return rawOutput

def check_State(jsonSHA):

        command = 'python3 ./VxAPI/vxapi.py report_get_state {}'.format(jsonSHA)
        print("Executing command: {}".format(command))
        rawOutput = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout

        time.sleep(10)
        return rawOutput

class Peregrine(discord.Client):

    async def on_ready(self):
        print('Logged in as')
        print(logo)
        print(self.user.id)

    async def on_message(self, message):
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content.lower())
        if message.content.startswith('!peregrine'):
            channel = message.channel

            if message.content.endswith('status'):
                await channel.send('Status: Logged In')

    # Prevent bot replying to self

        if message.author.id == self.user.id:
            return

    # Check if poster has moderation bypass

    #

    # Check if url] exists in message. If so, submit to HA

        if url:
            trimmedMessage = mask_URL(url, message.content)

            print('URL detected in message ID: {}'.format(message.id))
            print('Processing url: {}\n\n'.format(url[0]))

            await message.delete()
            botmessage = await message.channel.send('Peregrine Discord Malware Protection :bird:\n\n```Do not panic!\nYour URL has been submitted to Hybrid-Analysis for evaluation. Once this process is completed this message will update. Moderators may whitelist this url by issuing command !whitelist <url>\n\n\nAwaiting report...```\n\n\nOriginal Message:\n>>> {}\n- {}\n'.format(trimmedMessage, message.author))

        # Generate report with Hybrid Analysis

            scanUrl = scan_URL(url)

            formattedUrl = format_Output(scanUrl)
            jsonUrl = convert_JSON(formattedUrl)

            jsonID = jsonUrl['id']
            jsonSHA = jsonUrl['sha256']

            print("The jsonID is: ",jsonID)
            print("The jsonSHA is: ",jsonSHA)

            checkSummary = check_Status(jsonSHA)

            formattedSummary = format_Output(checkSummary)
            jsonSummary = convert_JSON(formattedSummary)

            checkReportState = check_State(jsonSHA)

            formattedReportState = format_Output(checkReportState)
            jsonReportState = convert_JSON(formattedReportState)

            jsonTime = jsonSummary['analysis_start_time']
            jsonAV = jsonSummary['av_detect']
            jsonVerdict = jsonSummary['verdict']
            jsonState = jsonReportState['state']

            while jsonState != "SUCCESS":
                checkSummary = check_State(jsonSHA)
                print("Report is ready! State is: ", jsonState)

            print("Time is:", jsonTime)
            print("AV Detections:", jsonAV)
            print("Verdict:", jsonVerdict)

            print(jsonSummary)
            await botmessage.edit(content = 'Peregrine Discord Malware Protection :bird:\n\n\n```Hybrid Analysis Results:\nSubmission Time: {}\nTotal AV Detections: {}\nAnlysis Verdict: {}```*URL has been processed Succesfully*.\n\n\nOriginal Message:\n>>> {}\n- {}\n'.format(jsonTime, jsonAV, jsonVerdict,  trimmedMessage, message.author))

            # Demoy and cleanup

            time.sleep(5)
            await botmessage.edit(content = 'This has been a demo of:\n\n\n```{}```'.format(logo))
            time.sleep(10)
            await botmessage.delete()


client = Peregrine()
client.run('token')
