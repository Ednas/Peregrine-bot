async def database_normalize_entries(database_connection, member_id, member, discord_nick):
    '''Inserts matched Discord ID for nicknames or discord name'''

    # Connect to database and insert into verification database

    cursor = database_connection.cursor(prepared=True)
    sql_query = """UPDATE verified SET DiscordID = %s, DiscordNickname = %s WHERE DiscordUser = %s"""
    parameterized_values = (member_id, discord_nick , member)
    cursor.execute(sql_query, parameterized_values)
    database_connection.commit()
    
    return