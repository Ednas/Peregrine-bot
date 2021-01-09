#!/bin/python3

# Import core modules and dependencies

import os
import random
from datetime import datetime, timedelta
import discord
from dotenv import load_dotenv
import smtplib
import ssl
import mysql.connector
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import discord
from discord.ext import commands
from resources.peregrineCore.start_peregrine import *

# Import custom modules

from resources.modules.hybridanalysis import *
from resources.modules.wgu.database import *
from resources.modules.wgu.embeds import *
from resources.modules.wgu.usermanagement import *

# Set up additional parameters for commands and intents

intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.presences = True
intents.reactions = True
client = commands.Bot(command_prefix="!")

# Validate the bot has advanced gateway permissions

# Import environment variables

load_dotenv()

TOKEN = os.getenv('bot_token')
WELCOME = os.getenv('welcome_message_id')
GUILD_ID = os.getenv('guild_id')
LOG_CHANNEL = os.getenv('log_channel_id')
NICKNAME_SCHEMA = os.getenv('nickname_schema')
VERIFICATION_CHANNEL = os.getenv('VERIFICATION_CHANNEL_ID')
VERIFICATION_MESSAGE = os.getenv('VERIFICATION_MESSAGE_ID')
VERIFIED_ROLE = os.getenv('verified_role_name')
VERIFICATION_EMOJI = os.getenv('verification_emoji')
SRC_EMAIL = os.getenv('bot_email_address')
EMAIL_PASS = os.getenv('bot_email_password')
DB_USER = os.getenv('database_username')
DB_PASS = os.getenv('database_username_password')
DB_IPV4 = os.getenv('database_ipv4_address')
# DB_IPV6 = os.getenv('database_ipv6_address')
DB_NAME = os.getenv('database_name')

# Connect to database

if DB_IPV6:

    def connect():
        return mysql.connector.connect(

            host=DB_IPV6,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
            
            )

else: 

    def connect():
    return mysql.connector.connect(

        host=DB_IPV4,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
        
        )

class peregrine(discord.Client):

    # Display logo and basic information on successful login

    async def on_ready(self):

        # Initiate bot and connect to guilds

        await start_peregrine(self, LOG_CHANNEL)

    # Track user joins and leaves

    async def on_member_join(self, member):

        # Set log channel ID

        channel = self.get_channel(LOG_CHANNEL)

        # Alert console of new member and push to log channel

        on_member_join_message = "Event triggered: Member joined\n   Member: {}".format(
            member
        )
        print(on_member_join_message)
        await channel.send(content=on_member_join_message)

        # Auto assign unverified role to new members and set nickname defaults

        await wgu_set_unverified_on_new_join(member, channel)
        await wgu_set_user_nick_on_join(member, channel)

    async def on_member_remove(self, member):

        # Set log channel

        channel = self.get_channel(LOG_CHANNEL)

        # Alert console of member leaving and push to log channel

        on_member_leave_message = "Event triggered: Member removed\n   Member: {}".format(
            member
        )

        print(on_member_leave_message)
        await channel.send(content=on_member_leave_message)

    async def on_raw_reaction_add(self, payload):

        # Set verification channel ID and validate it is the proper channel

        on_reaction_add_message = await self.get_channel(VERIFICATION_CHANNEL).fetch_message(VERIFICATION_MESSAGE)

        if payload.message_id != on_reaction_add_message.id:
            return

        # Set log channel

        channel = self.get_channel(LOG_CHANNEL)

        # Alert console of member leaving and push to log channel

        on_reaction_add_verification_alert = (
            "Event triggered: Member verification\n   Member: {}".format(payload.member)
        )

        print(on_reaction_add_verification_alert)
        await channel.send(content=on_reaction_add_verification_alert)

#*******# Initiate email verification process here ******

        # Run module to set user role to verified

        await wgu_add_verified_role(self, payload, channel)

    # Listen for custom commands

    async def on_message(self, message):

        # Prevent bot replying to self

        if message.author.id == self.user.id:
            return

        # Channel commands are listed below

        if message.content.startswith("!verify"):

            try:

                print(
                    "Event triggered: !verify\n   Member: {}\n".format(message.author)
                )

                verification_instructions_embedded_message = await wgu_verification_embed()
                send_verification_message = await message.channel.send(embed=verification_instructions_embedded_message)

                # Add initial reaction

                emoji_for_verification = "✅"
                await send_verification_message.add_reaction(emoji_for_verification)

            except Exception as e:

                print(e)
                error_message = "Could not process !verify command.\n"
                await message.channel.send(content=error_message)

        if message.content.startswith("!certs"):

            try:

                print("Event triggered: !certs\n   Member: {}\n".format(message.author))
                certification_instructions_embedded_message = await wgu_certifications_embed()
                await message.channel.send(embed=certification_instructions_embedded_message)

            except Exception as e:

                print(e)
                error_message = "Could not process !certs command.\n"
                await message.channel.send(content=error_message)

            return

        if message.content.startswith("!faq"):

            try:

                print("Event triggered: !faq\n   Member: {}\n".format(message.author))
                faq_embedded_message = await wgu_faq_embed()
                await message.channel.send(embed=faq_embedded_message)

            except Exception as e:

                print(e)
                error_message = "Could not process !faq command.\n"
                await message.channel.send(content=error_message)

            return

        if message.content.startswith("!resources"):

            try:

                print(
                    "Event triggered: !resources\n   Member: {}\n".format(
                        message.author
                    )
                )
                resources_embedded_message = await wgu_resources_embed()
                await message.channel.send(embed=resources_embedded_message)

            except Exception as e:

                print(e)
                error_message = "Could not process !resources command.\n"
                await message.channel.send(content=error_message)

            return

        if message.content.startswith("!roles"):

            try:
                print("Event triggered: !roles\n   Member: {}\n".format(message.author))
                roles_embedded_message = await wgu_roles_embed()
                await message.channel.send(embed=roles_embedded_message)

            except Exception as e:

                print(e)
                error_message = "Could not process !roles command.\n"
                await message.channel.send(content=error_message)

            return


# Launch the bot and connect to channel

client = peregrine(intents=intents)
client.run(TOKEN)
