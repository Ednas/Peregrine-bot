#!usr/bin/python3

# Import core modules and dependencies

import os
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
import smtplib
import ssl
import mysql.connector
import discord
from discord.ext import commands
from resources.peregrineCore.start_peregrine import start_peregrine

# Import embed modules for direct messages

from resources.modules.wgu.embeds.direct.wgu_send_email_embed import *
from resources.modules.wgu.embeds.direct.wgu_email_already_verified_embed import *
from resources.modules.wgu.embeds.direct.wgu_user_verified_success_embed import *
from resources.modules.wgu.embeds.direct.wgu_email_bad_domain import *
from resources.modules.wgu.embeds.direct.wgu_instructions_embed import *

# Import embed modules for log embeds

from resources.modules.wgu.embeds.logs.wgu_verify_log_embed import *
from resources.modules.wgu.embeds.logs.wgu_verify_success_log_embed import *

# Import database modules

from resources.modules.wgu.database.wgu_check_record import *
from resources.modules.wgu.database.wgu_check_verified import *
from resources.modules.wgu.database.wgu_delete_record import *
from resources.modules.wgu.database.wgu_send_email import *
from resources.modules.wgu.database.wgu_set_record import *
from resources.modules.wgu.database.wgu_set_verified import *

# Import user management modules for onboarding

from resources.modules.wgu.usermanagement.onboarding.wgu_set_unverified_on_new_join import *
from resources.modules.wgu.usermanagement.onboarding.wgu_set_user_nick_on_join import *

# Import user management modules for verification
from resources.modules.wgu.usermanagement.verification.wgu_send_verification_dm import *
from resources.modules.wgu.usermanagement.verification.wgu_sqlcheckverified import *
from resources.modules.wgu.usermanagement.verification.wgu_sqlclearverified import *

# Import user management modules for self roles
from resources.modules.wgu.usermanagement.roles.wgu_enrollment_status_self_role import *
from resources.modules.wgu.usermanagement.roles.wgu_subscription_self_role import *

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
GUILD_ID = os.getenv('guild_id')
LOG_CHANNEL = os.getenv('log_channel_id')
VERIFICATION_CHANNEL = os.getenv('verification_channel_id')
VERIFICATION_MESSAGE = os.getenv('verification_message_id')
ENROLLMENT_MESSAGE = os.getenv('enrollment_self_role_message_id')
SUBSCRIPTION_MESSAGE = os.getenv('subscription_self_role_message_id')
VERIFIED_ROLE = os.getenv('verified_role_name')
UNVERIFIED_ROLE = os.getenv('unverified_role_name')
VERIFICATION_EMOJI = os.getenv('verification_emoji')
STUDENT_EMOJI = os.getenv('student_emoji')
ALUMNI_EMOJI = os.getenv('alumni_emoji')
CCDC_SUB_EMOJI = os.getenv('ccdc_sub_emoji')
NICE_SUB_EMOJI = os.getenv('nice_sub_emoji')
CTF_SUB_EMOJI = os.getenv('ctf_sub_emoji')
HTB_SUB_EMOJI = os.getenv('htb_sub_emoji')
THM_SUB_EMOJI = os.getenv('thm_sub_emoji')
OTW_SUB_EMOJI = os.getenv('otw_sub_emoji')
NCL_SUB_EMOJI = os.getenv('ncl_sub_emoji')
FOREIGN_SUB_EMOJI = os.getenv('foreign_sub_emoji')
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
        
        # Set log channel

        channel = self.get_channel(int(LOG_CHANNEL))

        # Alert console of new member and push to log channel

        on_member_join_message = "Event triggered: Member joined\n   Member: {}".format(
            member
        )
        print(on_member_join_message)
        await channel.send(content=on_member_join_message)

        # Auto assign unverified role to new members and set nickname defaults

        await wgu_set_unverified_on_new_join(member, channel)
        await wgu_set_user_nick_on_join(member, channel)
        
    async def on_raw_reaction_add(self, payload):

        if str(payload.message_id) == str(VERIFICATION_MESSAGE):
            
            print("Triggering verification")
            
            # Set log channel

            channel = channel = self.get_channel(int(LOG_CHANNEL))
            print("Log channel set")
            
            # Alert console of member leaving and push to log channel

            on_reaction_add_verification_alert = (
                "Event triggered: Member verification reaction\n   Member: {}".format(payload.member)
            )

            print(on_reaction_add_verification_alert)
            await channel.send(content=on_reaction_add_verification_alert)

            # Initiate email verification process

            member = discord.Member

            wgu_instructions_message = await wgu_instructions_embed(self, member)
            await member.send(embed=wgu_instructions_message)

            return

        if str(payload.message_id) != str(VERIFICATION_MESSAGE):
            return

    # Listen for custom commands

    async def on_message(self, message):

        # Prevent bot replying to self

        if message.author.id == self.user.id:
            return

        # Commands for querying and interacting with the SQL database

        if message.content.startswith("!sqlcheckverified"):

            try:

                print("Event triggered: !sqlcheckverified\n   Member: {}\n".format(message.author))

                email = message.content.split(' ')[-1]
                print("Email submitted is: {}".format(email))
                conx = connect()
                sqlcheckverified_embedded_message = await wgu_sqlcheckverified(self, email, conx)
                send_sqlcheckverified_message = await message.channel.send(content=sqlcheckverified_embedded_message)


            except Exception as e:

                # Set log channel

                channel = channel = self.get_channel(int(LOG_CHANNEL))

                print(e)
                error_message = "Could not process !sqlcheckverified command.\n"
                await message.channel.send(content=error_message)

            return
        
        if message.content.startswith("!sqlclearemail"):

            try:

                print("Event triggered: !verify\n   Member: {}\n".format(message.author))

                sqlclearemail_embedded_message = await wgu_sqlclearemail()
                send_verification_message = await message.channel.send(embed=sqlclearemail_embedded_message)

            except Exception as e:

                # Set log channel

                channel = channel = self.get_channel(int(LOG_CHANNEL))

                print(e)
                error_message = "Could not process !verify command.\n"
                await message.channel.send(content=error_message)

            return

########################## VERIFICATION  SECTION ##########################
##########################                       ##########################
##########################                       ##########################
##########################                       ##########################

        if message.content.startswith("!email"):
            dst_email = message.content.split(' ')[-1]
            username = str(message.channel.recipient)
            discord_user = str(username).split('#')

            # Check domain, allow wgu domains to begin verification
            if dst_email.endswith("wgu.edu"):
                # Set up other variables
                conx = connect()
                code = []
                for _ in range(6):
                    code.append(str(random.randint(0,9)))
                code = ''.join(code)
                expiry = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
                username = str(message.channel.recipient)

                # Set up log variables
                user_email = message.content.split(' ')[-1]
                wgu_user = str(dst_email).split('@')
                discord_user = str(username).split('#')

                # Generate new user nickname
                new_nick_part_one = discord_user[0][0:18]
                new_nick_part_two = wgu_user[0]
                new_nickname = "{} | {}".format(new_nick_part_one, new_nick_part_two)

                # Get necessary role information
                guild = self.get_guild(int(GUILD_ID))
                member = discord.utils.find(lambda m : m.id == message.channel.recipient.id, guild.members)

                # Print to console
                print("Verification triggered by: {} for guild {}\n   Code is: {}\n   Email is: {}\n   New Nickname is: {}".format(str(member.id), str(member.guild), str(code), str(message.content.split(' ')[-1]), str(new_nickname)))

                if bool(await wgu_check_verified(dst_email, conx)):
                    await wgu_set_record(dst_email, username, code, expiry, conx)
                    await wgu_send_email(code, dst_email, SRC_EMAIL, EMAIL_PASS)

                    # Alert user that an email has been sent

                    email_message = await wgu_send_email_embed(dst_email, wgu_user)
                    await message.channel.send(embed=email_message)

                    # Set user nickname

                    await member.edit(nick=new_nickname)

                else:

                    # Alert user that email has already been verified

                        already_verified_message = await wgu_email_already_verified_embed(dst_email, wgu_user)
                        await message.channel.send(embed=already_verified_message)
                        await member.edit(nick=new_nickname)

                # Log information

                # Set log channel

                channel = channel = self.get_channel(int(LOG_CHANNEL))

                log_message = await wgu_verify_log_embed(user_email, wgu_user, discord_user, new_nickname, code, message)
                await channel.send(embed=log_message)

                print("Email verification triggered. Submitted message is: {}\n from: {}".format(message.content, message.author.id))
                print("    ┕ Email is: {}".format(message.content.split(' ')[-1]))
                print("    ┕ WGU user is: {}".format(wgu_user[0]))
                print("    ┕ Discord Username: {}".format(discord_user[0]))
                print("    ┕ New Nickname is: {}".format(new_nickname))

            else:
                bad_domain = await wgu_email_bad_domain(dst_email, discord_user)
                await message.channel.send(embed=bad_domain)
                # No logging here to stop attempts at flooding the feed

        if message.content.startswith("!verify"):

            # Set up variables

            conx = connect()
            expiry = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
            guild = self.get_guild(int(GUILD_ID))
            member = discord.utils.find(lambda m : m.id == message.channel.recipient.id, guild.members) 
            code = message.content.split(' ')[-1]
            username = str(message.channel.recipient)

            if bool(await wgu_check_record(code, username, conx)):
                
                try: 

                    await wgu_set_verified(username, conx)
                    await wgu_delete_record(code, conx)
                    
                    await member.add_roles(discord.utils.get(guild.roles, name=VERIFIED_ROLE))
                    await member.remove_roles(discord.utils.get(guild.roles, name=UNVERIFIED_ROLE))
                                        
                    # Alert user that they have been verified
                    
                    user_verified_success_embed = await wgu_user_verified_success_embed(username)
                    await message.channel.send(embed=user_verified_success_embed)
                    
                    # Set log channel

                    channel = channel = self.get_channel(int(LOG_CHANNEL))

                    log_message = await wgu_verify_success_log_embed(message)
                    await channel.send(embed=log_message)
                
                except Exception as e:

                    print(e)
                    errorMessage = "Failed to process verification role for new member: {}\nPlease hand verify this member or contact a bot developer".format(member)
                    await channel.send(content=errorMessage)

        if message.content.startswith("!delete"):
            
            # Set up variables

            conx = connect()         
            
            # Set up other variables
            
            field = message.content.split(' ')[-1]

            await wgu_delete_record(field, conx)
            await message.channel.send("""We'll get that taken care of for
                                       you.""")

# Launch the bot and connect to channel

client = peregrine(intents=intents)
client.run(TOKEN)
