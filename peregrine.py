#!/usr/bin/python3
'''Discord bot for WGU Discord Clubs'''

# Import required modules

import os
from dotenv import load_dotenv
import discord
import discord.utils
from discord.ext import commands

# Import core custom modules
from modules.core.discord.embeds.peregrine_check_status import peregrine_check_status
from modules.core.peregrine_connect_database import peregrine_connect_database

# Import wgu custom database modules
from modules.wgu.database.database_check_existing_email import database_check_existing_email
from modules.wgu.database.database_check_existing_username import database_check_existing_username
from modules.wgu.database.database_create_new_entry import database_create_new_entry
from modules.wgu.database.database_check_ver_pin import database_check_ver_pin
from modules.wgu.database.database_push_to_verified import database_push_to_verified
from modules.wgu.database.database_normalize_entries import database_normalize_entries
from modules.wgu.database.database_delete_entries import database_delete_entries
from modules.wgu.database.database_check_existing_nickname import database_check_existing_nickname

# Import wgu custom email modules
from modules.wgu.email.email_send_ver_code import email_send_ver_code

# Import custom embed message modules
from modules.wgu.embeds.database_already_exists_embed import database_already_exists_embed
from modules.wgu.embeds.wgu_email_sent_embed import wgu_email_sent_embed
from modules.wgu.embeds.wgu_invalid_email_embed import wgu_invalid_email_embed
from modules.wgu.embeds.wgu_ver_invalid_code_embed import wgu_ver_invalid_code_embed
from modules.wgu.embeds.wgu_ver_successful_embed import wgu_ver_successful_embed
from modules.wgu.embeds.wgu_check_email_for_code_embed import wgu_check_email_for_code_embed
from modules.wgu.embeds.wgu_send_ver_start_embed import wgu_send_ver_start_embed
from modules.wgu.embeds.command_email_triggered_embed import command_email_triggered_embed
from modules.wgu.embeds.command_status_triggered_embed import command_status_triggered_embed
from modules.wgu.embeds.command_verify_triggered_embed import command_verify_triggered_embed
from modules.wgu.embeds.wgu_ver_reaction_embed import wgu_ver_reaction_embed
from modules.wgu.embeds.command_sql_triggered_embed import command_sql_triggered_embed
from modules.wgu.embeds.command_sql_check_ver_embed import command_sql_check_ver_embed
from modules.wgu.embeds.command_sql_check_auth_embed import command_sql_check_auth_embed
from modules.wgu.embeds.command_sql_check_unver_embed import command_sql_check_unver_embed
from modules.wgu.embeds.command_alert_triggered_embed import command_alert_triggered_embed
from modules.wgu.embeds.command_sqla_triggered_embed import command_sqla_triggered_embed

# Import Peregrine specific embeds
from modules.core.discord.embeds.perri_help_triggered_embed import perri_help_triggered_embed
from modules.core.discord.commands.perri_command_help_embed import perri_command_help_embed
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
DM_MESSAGE = os.getenv('dm_ver_message')
SRC_EMAIL = os.getenv('bot_email_address')
EMAIL_PASS = os.getenv('bot_email_password')
DB_USER = os.getenv('database_username')
DB_PASS = os.getenv('database_username_password')
DB_IPV4 = os.getenv('database_ipv4_address')
# DB_IPV6 = os.getenv('database_ipv6_address')
DB_NAME = os.getenv('database_name')

# Set up additional parameters for commands and intents

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.typing = True
intents.presences = True
intents.reactions = True

# Setup database connection

# Define bot under the commands framework

peregrine = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

# Jail all new members

@peregrine.event
async def on_member_join(member):
    '''Set users to Unverified when they join'''

    # Alert console of new member and push to log channel

    on_member_join_message = "Event triggered: Member joined\n   Member: {}".format(
        member
    )
    print(on_member_join_message)

    # Auto assign unverified role to new members and set nickname defaults

    await member.add_roles(discord.utils.get(member.guild.roles, name="Unverified"))

@peregrine.event
async def on_raw_reaction_add(payload):
    '''This function tells the bot to DM people who react to the verification message'''

    if str(payload.message_id) == str(VERIFICATION_MESSAGE):

        print("Triggering verification")

        # Set log channel

        channel = peregrine.get_channel(int(LOG_CHANNEL))
        await channel.send(embed=await wgu_ver_reaction_embed(payload.member, payload.guild_id,
     payload.user_id))

        # Initiate email verification process

        if str(payload.emoji.name) == str(VERIFICATION_EMOJI):
            await peregrine.get_user(payload.user_id).send(
                embed= await wgu_send_ver_start_embed(payload.member))

        return

# Main bot commands

@peregrine.command(name='status', description="Print connection status")
@commands.has_any_role("Administrator", "Moderator")
async def status(ctx):
    '''This function displays status information to the channel it is issued in'''

    # Get connection status of database
    database_status = await peregrine_connect_database(DB_IPV4, DB_USER, DB_PASS, DB_NAME)

    print("Verifying connection to database...\n")

    # Set log channel

    channel = peregrine.get_channel(int(LOG_CHANNEL))
    await channel.send(embed= await command_status_triggered_embed(ctx.author.name,
     ctx.guild, ctx.author.id))

    # Check database connectivity

    if bool(database_status.is_connected()) is True:

        try:
            print(f"\tCurrent database status is: {database_status.is_connected()}\n")

        except TypeError as exception_message:
            print(exception_message)

    if bool(database_status.is_connected()) is False:

        try:
            message = "Unable to connect to database. Please verify credentials in\
             environment file are correct"
            print(message)
            print(f"\tCurrent database status is: {database_status.is_connected()}")
            return

        except TypeError as exception_message:
            print(exception_message)
            return exception_message

    # Send message in triggered channel with bot status embed
    await ctx.send(embed= await peregrine_check_status(ctx.author.name, ctx.guild,
     ctx.guild.id, database_status.is_connected()))

# Verification process commands

@peregrine.command(name='email', description="Collect user email for verification")
async def email(ctx, user_email):
    '''This function collects the email from a wgu user for verification'''

    # Set log channel

    channel = peregrine.get_channel(int(LOG_CHANNEL))
    await channel.send(embed= await command_email_triggered_embed(ctx.author.name, ctx.guild,
     ctx.author.id, user_email))

    # Check if email is a valid wgu email address

    if user_email.split('@')[-1] != "wgu.edu":
        await ctx.send(embed= await wgu_invalid_email_embed(user_email))
        return

    # Check database for email entry

    email_check_result = await database_check_existing_email(
        await peregrine_connect_database(DB_IPV4, DB_USER, DB_PASS, DB_NAME), user_email)

    # Send message to alert member this email is already verified

    if bool(email_check_result[0]) is True and bool(email_check_result[1]) is False and str(
        email_check_result[3]) == str(ctx.author.id):

        # Set member to verified if Discord ID and email match verification entry

        guild = peregrine.get_guild(int(GUILD_ID))
        member = discord.utils.find(lambda m : m.id == ctx.message.channel.recipient.id,
         guild.members)
        await member.add_roles(discord.utils.get(guild.roles, name=VERIFIED_ROLE))
        await member.remove_roles(discord.utils.get(guild.roles, name=UNVERIFIED_ROLE))

        # Send message to alert them that they have been verified

        await ctx.send(embed=await wgu_ver_successful_embed(ctx.author.name))

        # Set user nickname

        await member.edit(nick=str(email_check_result[5]))

    if bool(email_check_result[0]) is False and bool(email_check_result[1]) is True and str(
        email_check_result[3]) != str(ctx.author.id):

        # Send message to alert them this email is already registered

        await ctx.send(embed=await database_already_exists_embed(user_email))

    if email_check_result[0] is False and email_check_result[1] is True and str(
        email_check_result[3]) == str(ctx.author.id):

        await ctx.send(embed= await wgu_check_email_for_code_embed(user_email))

    if bool(email_check_result[0]) is False and bool(email_check_result[1]) is False and bool(
        email_check_result[2]) is False:

        # Create new database entry for user

        await database_create_new_entry(await peregrine_connect_database(DB_IPV4, DB_USER,
         DB_PASS, DB_NAME), user_email, ctx.author.name, ctx.author.id)

        # Send message to user to alert them that the email and pincode has been sent

        await email_send_ver_code(await peregrine_connect_database(DB_IPV4, DB_USER,
        DB_PASS, DB_NAME), user_email, SRC_EMAIL, EMAIL_PASS)
        await ctx.send(embed= await wgu_email_sent_embed(user_email))

@peregrine.command(name='verify', description='Collects verification pin from user')
async def verify(ctx, submitted_auth_code):
    '''This function checks submitted auth code against database and validates Discord ID'''

    # Set log channel

    channel = peregrine.get_channel(int(LOG_CHANNEL))
    await channel.send(embed= await command_verify_triggered_embed(ctx.author.name, ctx.guild,
     ctx.author.id, submitted_auth_code))

    # Check database to validate the pincode

    auth_check_result = await database_check_ver_pin(await peregrine_connect_database(
        DB_IPV4, DB_USER, DB_PASS, DB_NAME), ctx.author.id, submitted_auth_code)

    if auth_check_result is True:

        # Push user information from auth table to verified table

        await database_push_to_verified(await peregrine_connect_database(
        DB_IPV4, DB_USER, DB_PASS, DB_NAME), ctx.author.id)

        # Set member to verified

        guild = peregrine.get_guild(int(GUILD_ID))
        member = discord.utils.find(lambda m : m.id == ctx.message.channel.recipient.id,
         guild.members)
        await member.add_roles(discord.utils.get(guild.roles, name=VERIFIED_ROLE))
        await member.remove_roles(discord.utils.get(guild.roles, name=UNVERIFIED_ROLE))

        # Send message to alert them that they have been verified

        await ctx.send(embed=await wgu_ver_successful_embed(ctx.author.name))

        # Set user nickname

        await member.edit(nick=str(auth_check_result[2]))

    if auth_check_result is False:
        await ctx.send(embed=await wgu_ver_invalid_code_embed(submitted_auth_code))

# Moderation management commands

@peregrine.group()
async def sql(ctx):
    '''Provides various commands to interact with the SQL database as a moderator'''
    pass

@sql.command(name="check", description="Check database for existing user email")
@commands.has_any_role("Administrator","Moderator")
async def check(ctx, user_email):
    '''- Check database for existing user email'''

    # Set log channel

    channel = peregrine.get_channel(int(LOG_CHANNEL))
    await channel.send(embed= await command_sql_triggered_embed(ctx.author.name, ctx.guild,
     ctx.author.id, user_email))

    # Check database for requested email

    sql_check_result = await database_check_existing_email(await peregrine_connect_database(
        DB_IPV4, DB_USER, DB_PASS, DB_NAME), user_email)

    if bool(sql_check_result[0]) is True and bool(sql_check_result[1]) is False:

        await ctx.channel.send(embed= await command_sql_check_ver_embed(ctx.author.name,
            user_email, sql_check_result[4], sql_check_result[5],
            sql_check_result[3], ctx.guild))

    if bool(sql_check_result[0]) is False and bool(sql_check_result[1]) is True:
        await ctx.channel.send(embed= await command_sql_check_auth_embed(ctx.author.name,
            user_email, sql_check_result[4], sql_check_result[5],
            sql_check_result[3], ctx.guild))

    if bool(sql_check_result[0]) is False and bool(sql_check_result[1]) is False:
        await ctx.channel.send(embed= await command_sql_check_unver_embed(ctx.author.name,
            user_email, ctx.guild))

# Administrator management commands

@peregrine.command(name="alert", description="""
Provides various sub commands to send alerts to various roles""")
@commands.has_role("Administrator")
async def alert(ctx, role: discord.Role, *, message):
    '''Allows Administrators the ability to mass direct message a specificed role'''

    # Set log channel

    channel = peregrine.get_channel(int(LOG_CHANNEL))
    await channel.send(embed= await command_alert_triggered_embed(ctx.author.name, ctx.guild,
     ctx.author.id, discord.Role, message))

    # Send messages

    members = [member for member in ctx.guild.members if role in member.roles]
    for member in members:
        await member.send(message)
        print(f"Message sent to {member} successfully")

@peregrine.group()
async def sqla(ctx):
    '''Provides various commands to interact with the SQL database as an administrator'''
    pass

@sqla.command(name="normalize", description="This command syncs matching member DiscordID with an entry in the local database")
@commands.has_role("Administrator")
async def normalize(ctx):
    '''Inserts DiscordID and Discord Username for all database entries by matching username to old schema'''

    # Set log channel

    channel = peregrine.get_channel(int(LOG_CHANNEL))
    await channel.send(embed= await command_sqla_triggered_embed(ctx.author.name, ctx.guild,
    ctx.author.id))

    # Collect all members from guild

    members = [user.name for user in ctx.guild.members]
    member_nicknames = [member.display_name for member in ctx.guild.members]
    member_discriminators = [member.discriminator for member in ctx.guild.members]
    member_ids = [member.id for member in ctx.guild.members]

    # Check database for each user

    count = 0
    print(int(len(members)))
    print("### Checking all member usernames ####")

    while count != int(len(members)):
        if bool(len(str(member_ids[count])) >= 1):

            for member in members:

                checked_user = str(member) + "#" + str(member_discriminators[count])

                print(f'### Checking results for member: {str(checked_user)} ###')
                normalize_check_result = await database_check_existing_username(
                    await peregrine_connect_database(DB_IPV4, DB_USER, DB_PASS, DB_NAME),
                        str(checked_user))

                print(f'######\nResults of normalize_check_result:\n{normalize_check_result}\n\
                ######')

                if bool(normalize_check_result[0]) is True and bool(
                    normalize_check_result[1]) is False:

                    print(f'### {checked_user} was found. Normalizing entry ###')

                    await database_normalize_entries(await peregrine_connect_database(DB_IPV4,
                    DB_USER, DB_PASS, DB_NAME), int(member_ids[count]), str(checked_user),
                        str(member_nicknames[count]))

                count = count + 1

# Debugging and other commands

@peregrine.group()
async def perri(ctx):
    '''Provides various commands to interact with Peregrine and its backend'''
    pass

@perri.command(name="info", description="Displays the intro to Perri the Peregrine")
@commands.has_any_role("Administrator","Moderator")
async def info(ctx):
    '''Provides an intro and overview about Perri'''

    # Set log channel

    channel = peregrine.get_channel(int(LOG_CHANNEL))
    await channel.send(embed= await perri_help_triggered_embed(ctx.author.name, ctx.guild,
     ctx.author.id))

    # Collect commands

    perri_commands = [command.name for command in ctx.bot.commands]
    perri_command_docstrings = [command.help for command in ctx.bot.commands]

    await ctx.channel.send(embed= await perri_command_help_embed(ctx.author.name,
    ctx.guild, perri_commands, perri_command_docstrings))

# Start the bot

peregrine.run(TOKEN)
