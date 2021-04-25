async def database_check_existing_email(database_connection, user_email):
    '''Checks if submitted email already matches and returns results'''
    
    # Execute SQL query

    cursor = database_connection.cursor(prepared=True)
    sql_query = "SELECT Email, DiscordID, VerifiedDate, DiscordNickname FROM verified WHERE email = %s"
    parameterized_values = (user_email, )
    cursor.execute(sql_query, parameterized_values)
    query_results = cursor.fetchall()

    if bool(len(query_results) >= 1) is True:
    
        if bool(str(query_results[0][0]) == str(user_email)) is True:
            
            print(f"{user_email} exists in the verified database")
            return bool(True), bool(False), str(query_results[0][0]), str(
                    query_results[0][1]), str(query_results[0][2]), str(query_results[0][3])

    if bool(len(query_results) == 0) is True:

        cursor = database_connection.cursor(prepared=True)
        sql_query = "SELECT Email, DiscordID, AuthDate, DiscordNickname, Expiration FROM auth WHERE email = %s"
        parameterized_values = (user_email, )
        cursor.execute(sql_query, parameterized_values)
        query_results = cursor.fetchall()
                
        if bool(len(query_results) >= 1) is True:

            if bool(str(query_results[0][0]) == str(user_email)) is True:

                print (f"{user_email} exists in the auth database")
                return bool(False), bool(True), str(query_results[0][0]), str(
                    query_results[0][1]), str(query_results[0][2]), str(
                        query_results[0][3]), str(query_results[0][4])

        if bool(len(query_results) == 0) is True:

            print(f"{user_email} does not exist in the database")
            return bool(False), bool(False), bool(False)