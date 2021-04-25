async def database_delete_entries(database_connection, member):
    '''Inserts matched Discord ID for nicknames or discord name'''

    # Connect to database and delete from verified database

    cursor = database_connection.cursor(prepared=True)
    sql_query = """DELETE FROM verified WHERE DiscordUser = %s"""
    parameterized_values = (member)
    cursor.execute(sql_query, parameterized_values)
    database_connection.commit()
    
    # Connect to database and delete from auth database

    cursor = database_connection.cursor(prepared=True)
    sql_query = """DELETE FROM auth WHERE DiscordUser = %s"""
    parameterized_values = (member)
    cursor.execute(sql_query, parameterized_values)
    database_connection.commit()
    
    return