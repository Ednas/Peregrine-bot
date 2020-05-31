import discord
import re
import subprocess
import sys
import time
from io import StringIO

with open('Peregrine.txt', 'r') as mylogo:
    logo = mylogo.read()

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
                await channel.send('Status: Logged In\n```{}```'.format(logo))

        # Prevent bot replying to self

        if message.author.id == self.user.id:
            return

        # Check if poster has moderation bypass

        #

        # Check if URL exists in message. If so, submit to HA

        if url:
            storedurl = url
            print('URL Detected in message ID: {}'.format(message.id))
            print('Processing url: {}\n\n`'.format(storedurl[0]))

            await message.delete()
            botmessage = await message.channel.send('The URL has been submitted to Hybrid-Analysis for evaluation. Awaiting report')
            await botmessage.edit(content = 'The URL has been submitted to Hybrid-Analysis for evaluation. Awaiting report.')
            time.sleep(1)
            await botmessage.edit(content = 'The URL has been submitted to Hybrid-Analysis for evaluation. Awaiting report..')
            time.sleep(1)
            await botmessage.edit(content = 'The URL has been submitted to Hybrid-Analysis for evaluation. Awaiting report...')
            time.sleep(1)
            await botmessage.edit(content = 'The URL has been submitted to Hybrid-Analysis for evaluation. Awaiting report')
            time.sleep(1)
            await botmessage.edit(content = 'The URL has been submitted to Hybrid-Analysis for evaluation. Awaiting report.')
            time.sleep(1)
            await botmessage.edit(content = 'The URL has been submitted to Hybrid-Analysis for evaluation. Awaiting report..')
            time.sleep(1)
            await botmessage.edit(content = 'The URL has been submitted to Hybrid-Analysis for evaluation. Awaiting report...')
            time.sleep(1)
            await botmessage.edit(content = 'The URL has been submitted to Hybrid-Analysis for evaluation. Awaiting report')
            time.sleep(1)
            await botmessage.edit(content = 'The URL has been submitted to Hybrid-Analysis for evaluation. Awaiting report.')
            time.sleep(1)
            await botmessage.edit(content = 'The URL has been submitted to Hybrid-Analysis for evaluation. Awaiting report..')
            time.sleep(1)
            await botmessage.edit(content = 'The URL has been submitted to Hybrid-Analysis for evaluation. Awaiting report...')
            # Generate report with Hybrid Analysis

            command = 'python3 ./VxAPI/vxapi.py scan_url_for_analysis {} all'.format(storedurl[0])
            scan = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
            output = scan.read()
            print(output)
            # Edit previous message and add URL for report
            await botmessage.edit(content = 'The URL: {} is currently being scanned. Original Message:\n```{}```\nHybrid-Analysis Output: ```{}```\n'.format(storedurl[0], message, output))
            # Query status loop..

            # Edit message further with summary and unclickable urls

client = Peregrine()
client.run('token')
