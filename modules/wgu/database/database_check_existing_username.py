async def database_check_existing_username(database_connection, username):
    '''Checks if submitted username already matches and returns results'''
    
    # Execute SQL query

    cursor = database_connection.cursor()
    sql_query = "SELECT Email, DiscordID, VerifiedDate, DiscordUser FROM verified WHERE DiscordUser = %s"
    parameterized_values = (username, )
    cursor.execute(sql_query, parameterized_values)
    query_results = cursor.fetchall()

    print(f'### Contents of query_results: {query_results}')

    if bool(len(query_results) >= 1) is True:
    
        if bool(str(query_results[0][3]) == str(username)) is True:
            
            print(f"{username} exists in the verified database")
            return bool(True), bool(False), str(query_results[0][0]), str(
                    query_results[0][1]), str(query_results[0][2]), str(query_results[0][3])

    if bool(len(query_results) == 0) is True:

        cursor = database_connection.cursor()
        sql_query = "SELECT Email, DiscordID, AuthDate, DiscordNickname, Expiration FROM auth WHERE DiscordUser = %s"
        parameterized_values = (username, )
        cursor.execute(sql_query, parameterized_values)
        query_results = cursor.fetchall()
                
        if bool(len(query_results) >= 1) is True:

            if bool(str(query_results[0][3]) == str(username)) is True:

                print (f"{username} exists in the auth database")
                return bool(False), bool(True), str(query_results[0][0]), str(
                    query_results[0][1]), str(query_results[0][2]), str(
                        query_results[0][3]), str(query_results[0][4])

        if bool(len(query_results) == 0) is True:

            print(f"{username} does not exist in the database")
            return bool(False), bool(False), bool(False)