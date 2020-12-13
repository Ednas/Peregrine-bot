#!/bin/python3

# Import core modules and dependencies

import discord
from discord.ext import commands
from resources.peregrineCore.peregrineStartup import *

# Import custom modules for embeds

from resources.modules.wgu.wguEmbedModules.wguCertifications import *
from resources.modules.wgu.wguEmbedModules.wguVerification import *
from resources.modules.wgu.wguEmbedModules.wguQuestions import *
from resources.modules.wgu.wguEmbedModules.wguResources import *
from resources.modules.wgu.wguEmbedModules.wguRoles import *

# Import custom modules for administration

from resources.modules.wgu.wguManagementModules.wguNewUserRoles import *
from resources.modules.wgu.wguManagementModules.wguNewUserNick import *
from resources.modules.wgu.wguManagementModules.wguVerifiedRoleAssign import *
from resources.modules.wgu.wguManagementModules.wguVerifiedRoleRemove import *

# Import custom modules for logging capabilities

# Import custom modules for Hybrid-Analysis sandboxing

# Set up additional parameters for commands and intents

intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.presences = True
intents.reactions = True
client = commands.Bot(command_prefix="!")

# Validate the bot has advanced gateway permissions

# Define the bot in a OOB class


class peregrine(discord.Client):

    # Display logo and basic information on successful login

    async def on_ready(self):

        # Set log channel ID

        logChannel = 787493570659221524

        # Initiate bot and connect to guilds

        await peregrineStartup(self, logChannel)

    # Track user joins and leaves

    async def on_member_join(self, member):

        # Set log channel ID

        logChannel = 787493570659221524
        channel = self.get_channel(logChannel)

        # Alert console of new member and push to log channel

        memberJoinMessage = "Event triggered: Member joined\n   Member: {}".format(
            member
        )
        print(memberJoinMessage)
        await channel.send(content=memberJoinMessage)

        # Auto assign unverified role to new members and set nickname defaults

        await wguNewUserRoles(member, channel)
        await wguSetNewUserNick(member, channel)

    async def on_member_remove(self, member):

        # Set log channel ID

        logChannel = 787493570659221524
        channel = self.get_channel(logChannel)

        # Alert console of member leaving and push to log channel

        memberLeaveMessage = "Event triggered: Member removed\n   Member: {}".format(
            member
        )

        print(memberLeaveMessage)
        await channel.send(content=memberLeaveMessage)

    async def on_raw_reaction_add(self, payload):

        # Set verification channel ID and validate it is the proper channel

        reactionMessage = await self.get_channel(787215365737807893).fetch_message(
            787787424020299826
        )
        verificationChannel = "787215365737807893"

        if payload.message_id != reactionMessage.id:
            return

        # Set log channel ID

        logChannel = 787493570659221524
        channel = self.get_channel(logChannel)

        # Alert console of member leaving and push to log channel

        memberVerifyMessage = (
            "Event triggered: Member verification\n   Member: {}".format(payload.member)
        )

        print(memberVerifyMessage)
        await channel.send(content=memberVerifyMessage)

        # Run module

        await wguAddVerifiedRole(self, payload, channel)

    async def on_raw_reaction_remove(self, payload):

        guild = await self.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)

        # Set verification channel ID and validate it is the proper channel

        reactionMessage = await self.get_channel(787215365737807893).fetch_message(
            787787424020299826
        )
        verificationChannel = "787215365737807893"

        if payload.message_id != reactionMessage.id:
            return

        # Set log channel ID

        logChannel = 787493570659221524
        channel = self.get_channel(logChannel)

        # Alert console of member leaving and push to log channel

        memberRemoveVerifyMessage = (
            "Event triggered: Member remove verification\n   Member: {}".format(member)
        )

        print(memberRemoveVerifyMessage)
        await channel.send(content=memberRemoveVerifyMessage)

        # Run module

        await wguRemoveVerifiedRole(self, member, payload, channel)

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

                verifyMessage = await wguVerificationEmbed()
                sendMessage = await message.channel.send(embed=verifyMessage)

                # Add initial reactions

                verifyEmoji = "✅"
                message = sendMessage
                await message.add_reaction(verifyEmoji)

            except Exception as e:

                print(e)
                errorMessage = "Could not process !verify command.\n"
                await message.channel.send(content=errorMessage)

        if message.content.startswith("!certs"):

            try:

                print("Event triggered: !certs\n   Member: {}\n".format(message.author))
                certMessage = await wguCertificationsEmbed()
                await message.channel.send(embed=certMessage)

            except Exception as e:

                print(e)
                errorMessage = "Could not process !certs command.\n"
                await message.channel.send(content=errorMessage)

            return

        if message.content.startswith("!faq"):

            try:

                print("Event triggered: !faq\n   Member: {}\n".format(message.author))
                faqMessage = await wguQuestionsEmbed()
                await message.channel.send(embed=faqMessage)

            except Exception as e:

                print(e)
                errorMessage = "Could not process !faq command.\n"
                await message.channel.send(content=errorMessage)

            return

        if message.content.startswith("!resources"):

            try:

                print(
                    "Event triggered: !resources\n   Member: {}\n".format(
                        message.author
                    )
                )
                resourcesMessage = await wguResourcesEmbed()
                await message.channel.send(embed=resourcesMessage)

            except Exception as e:

                print(e)
                errorMessage = "Could not process !resources command.\n"
                await message.channel.send(content=errorMessage)

            return

        if message.content.startswith("!roles"):

            try:
                print("Event triggered: !roles\n   Member: {}\n".format(message.author))
                rolesMessage = await wguRolesEmbed()
                await message.channel.send(embed=rolesMessage)

            except Exception as e:

                print(e)
                errorMessage = "Could not process !roles command.\n"
                await message.channel.send(content=errorMessage)

            return


# Launch the bot and connect to channel

botToken = open("resources/peregrineCore/token", "r").readline()
client = peregrine(intents=intents)
client.run(botToken)
