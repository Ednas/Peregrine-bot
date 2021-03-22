async def database_check_ver_pin(database_connection, discord_id, submitted_auth_code):
    '''Checks if submitted pincode belongs to this discord user'''
    
    cursor = database_connection.cursor()
    sql_query = "SELECT AuthCode, DiscordID, DiscordNickname FROM auth WHERE DiscordID = %s"
    parameterized_values = (discord_id, )
    cursor.execute(sql_query, parameterized_values)
    query_results = cursor.fetchall()

    if bool(len(query_results) >= 1) is True:
        if bool(str(query_results[0][0]) == str(submitted_auth_code)) is True:
            if bool(str(query_results[0][1]) == str(discord_id)) is True:
            
                print("Submitted pincode is correct")
                return True

        else:

            print("Submitted is incorrect")
            return False

    if bool(len(query_results) == 0) is True:
        print("This user does not have a pin in the database")
        return