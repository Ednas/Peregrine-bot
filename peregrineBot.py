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
import discord
from discord.ext import commands
from resources.peregrineCore.start_peregrine import start_peregrine

# Import embed modules

from resources.modules.wgu.embeds.wgu_certifications_embed import *
from resources.modules.wgu.embeds.wgu_faq_embed import *
from resources.modules.wgu.embeds.wgu_resources_embed import *
from resources.modules.wgu.embeds.wgu_roles_embed import *
from resources.modules.wgu.embeds.wgu_verification_embed import *

# Import database modules

from resources.modules.wgu.database.wgu_check_record import *
from resources.modules.wgu.database.wgu_check_verified import *
from resources.modules.wgu.database.wgu_delete_record import *
from resources.modules.wgu.database.wgu_send_email import *
from resources.modules.wgu.database.wgu_set_record import *
from resources.modules.wgu.database.wgu_set_verified import *

# Import user management modules

from resources.modules.wgu.usermanagement.wgu_set_unverified_on_new_join import *
from resources.modules.wgu.usermanagement.wgu_set_user_nick_on_join import *
from resources.modules.wgu.usermanagement.wgu_send_verification_dm import *

# Import hybrid analysis modules

from resources.modules.hybridanalysis import *


# Set up additional parameters for commands and intents

intents = discord.Intents(messages=True, guilds=True)
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
VERIFICATION_CHANNEL = os.getenv('verification_channel_id')
VERIFICATION_MESSAGE = os.getenv('verification_message_id')
VERIFIED_ROLE = os.getenv('verified_role_name')
UNVERIFIED_ROLE = os.getenv('unverified_role_name')
VERIFICATION_EMOJI = os.getenv('verification_emoji')
DM_MESSAGE = os.getenv('dm_verification_message')
SRC_EMAIL = os.getenv('bot_email_address')
EMAIL_PASS = os.getenv('bot_email_password')
DB_USER = os.getenv('database_username')
DB_PASS = os.getenv('database_username_password')
DB_IPV4 = os.getenv('database_ipv4_address')
# DB_IPV6 = os.getenv('database_ipv6_address')
DB_NAME = os.getenv('database_name')

# Connect to database

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

        await start_peregrine(self, int(LOG_CHANNEL))

    # Track user joins and leaves

    async def on_member_join(self, member):

        # Set log channel ID

        channel = self.get_channel(int(LOG_CHANNEL))

        # Alert console of new member and push to log channel

        on_member_join_message = "Event triggered: Member joined\n   Member: {}".format(
            member
        )
        print(on_member_join_message)
        await channel.send(content=on_member_join_message)

        # Auto assign unverified role to new members and set nickname defaults

        await wgu_set_unverified_on_new_join(member, channel)
        await wgu_set_user_nick_on_join(member, channel, NICKNAME_SCHEMA)

    async def on_member_remove(self, member):

        # Set log channel

        channel = self.get_channel(int(LOG_CHANNEL))

        # Alert console of member leaving and push to log channel

        on_member_leave_message = "Event triggered: Member removed\n   Member: {}".format(
            member
        )

        print(on_member_leave_message)
        await channel.send(content=on_member_leave_message)

    async def on_raw_reaction_add(self, payload):

        print("Verification_message_id: {}".format(VERIFICATION_MESSAGE))
        print("Payload id: {}".format(payload.message_id))
        
        if str(payload.message_id) == str(VERIFICATION_MESSAGE):
            
            print("Triggering verification")
            
            # Set log channel

            channel = self.get_channel(int(LOG_CHANNEL))
            print("Log channel set")
            
            # Alert console of member leaving and push to log channel

            on_reaction_add_verification_alert = (
                "Event triggered: Member verification\n   Member: {}".format(payload.member)
            )

            print(on_reaction_add_verification_alert)
            await channel.send(content=on_reaction_add_verification_alert)

            # Initiate email verification process

            await wgu_send_verification_dm(self, payload, VERIFICATION_MESSAGE, VERIFICATION_EMOJI, DM_MESSAGE)

            return

        if str(payload.message_id) != str(VERIFICATION_MESSAGE):
            return

    # Listen for custom commands

    async def on_message(self, message):

        # Prevent bot replying to self

        if message.author.id == self.user.id:
            return

        # Channel commands are listed below

        # Set log channel

        channel = self.get_channel(int(LOG_CHANNEL))

        if message.content.startswith("!verembed"):

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

        if message.content.startswith("!certsembed"):

            try:

                print("Event triggered: !certs\n   Member: {}\n".format(message.author))
                certification_instructions_embedded_message = await wgu_certifications_embed()
                await message.channel.send(embed=certification_instructions_embedded_message)

            except Exception as e:

                print(e)
                error_message = "Could not process !certs command.\n"
                await message.channel.send(content=error_message)

            return

        if message.content.startswith("!faqembed"):

            try:

                print("Event triggered: !faq\n   Member: {}\n".format(message.author))
                faq_embedded_message = await wgu_faq_embed()
                await message.channel.send(embed=faq_embedded_message)

            except Exception as e:

                print(e)
                error_message = "Could not process !faq command.\n"
                await message.channel.send(content=error_message)

            return

        if message.content.startswith("!resourcesembed"):

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

        if message.content.startswith("!rolesembed"):

            try:
                print("Event triggered: !roles\n   Member: {}\n".format(message.author))
                roles_embedded_message = await wgu_roles_embed()
                await message.channel.send(embed=roles_embedded_message)

            except Exception as e:

                print(e)
                error_message = "Could not process !roles command.\n"
                await message.channel.send(content=error_message)

            return

        if message.content.startswith("!email"):
        
            # Set log channel

            channel = self.get_channel(int(LOG_CHANNEL))
            
            # Set up other variables

            conx = connect()
            dst_email = message.content.split(' ')[-1]
            code = []
            for _ in range(6):
                code.append(str(random.randint(0,9)))
            code = ''.join(code)
            expiry = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
            username = str(message.channel.recipient)
            
            # Get necessary role information
            
            guild = self.get_guild(int(GUILD_ID))
            member = discord.utils.find(lambda m : m.id == message.channel.recipient.id, guild.members) 
            
            print("Verification triggered by: {} for guild {}\n   Code is: {}.\n   Email is:".format(member.id, member.guild, code, dst_email))

            if bool(await wgu_check_verified(dst_email, conx)):
                await wgu_set_record(dst_email, username, code, expiry, conx)
                await wgu_send_email(code, dst_email, SRC_EMAIL, EMAIL_PASS)
                await message.channel.send("""An email was sent to the email
                                            address you provided. If you have
                                            any trouble finding it, try
                                            refreshing your browser, waiting a
                                            few minutes, or check your spam
                                            folder. If you're still having
                                            issues, feel free to check out the
                                            `#verification-support` channel for
                                            further questions.""")
                # Log the beginning of verification attempt! Enter here.
            else:
                await message.channel.send("""That email has already been
                                            verified. If you think this message
                                            is in error, please send a message
                                            in the `#verification-support`
                                            channel.""")
                try:


                    await member.add_roles(discord.utils.get(guild.roles, name=VERIFIED_ROLE))
                    await member.remove_roles(discord.utils.get(guild.roles, name=UNVERIFIED_ROLE))
                    await message.channel.send("""You're all set, enjoy the
                                                server! We look forward to
                                                learning with you!""")

                except Exception as e:

                    print(e)
                    errorMessage = "Failed to process verification role for new member: {}\nPlease hand verify this member or contact a bot developer".format(payload.member)
                    await channel.send(content=errorMessage)
            

        if message.content.startswith("!verify"):
            
            # Get necessary role information
            
            guild = self.get_guild(int(GUILD_ID))
            member = discord.utils.find(lambda m : m.id == message.channel.recipient.id, guild.members) 

            # Set log channel

            channel = self.get_channel(int(LOG_CHANNEL))
            
            # Set up other variables

            code = message.content.split(' ')[-1]
            username = str(message.channel.recipient)

            if bool(await wgu_check_record(code, username)):
                
                try: 

                    await wgu_set_verified(username, conx)
                    await wgu_delete_record(username, conx)
                
                    await member.add_roles(discord.utils.get(guild.roles, name=VERIFIED_ROLE))
                    await member.remove_roles(discord.utils.get(guild.roles, name=UNVERIFIED_ROLE))
                
                    await message.channel.send("""You're all set, enjoy the
                                                server! We look forward to
                                                learning with you!""")

                except Exception as e:

                    print(e)
                    errorMessage = "Failed to process verification role for new member: {}\nPlease hand verify this member or contact a bot developer".format(payload.member)
                    await channel.send(content=errorMessage)

        if message.content.startswith("!delete"):
            
            # Set log channel

            channel = self.get_channel(int(LOG_CHANNEL))
            
            # Set up other variables
            
            field = message.content.split(' ')[-1]

            wgu_delete_record(field)
            await message.channel.send("""We'll get that taken care of for
                                       you.""")

# Launch the bot and connect to channel

client = peregrine(intents=intents)
client.run(TOKEN)
