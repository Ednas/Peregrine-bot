async def start_peregrine(self, LOG_CHANNEL):
    
    # Print logo in terminal

    with open("resources/peregrineCore/peregrineLogo", "r") as mylogo:
        logo = mylogo.read()
        print("{}".format(logo))

    # Check for active connections to Discord Guilds


    for guild in self.guilds:

        # Print information related to the guilds

        print("{} is conencted to the following guild:".format(self.user))
        print("          {} (id: {})".format(guild.name, guild.id))

        print("\n\nPeregrine is connected and ready.")

    print("Logging messages to channel: {}".format(LOG_CHANNEL))

    return log_channel