async def database_check_existing_records(database_connection, user_email):
    '''Checks if submitted email already matches and returns results'''
    
    cursor = database_connection.cursor()
    sql_query = "SELECT Email, DiscordID, AuthDate, DiscordNickname FROM verified WHERE email = %s"
    parameterized_values = (user_email, )
    cursor.execute(sql_query, parameterized_values)
    query_results = cursor.fetchall()
    
    if bool(len(query_results) >= 1) is True:
    
        if bool(str(query_results[0][0]) == str(user_email)) is True:
            
            print(f"Submitted email exists in the verified database")
            return True

    if bool(len(query_results) == 0) is True:
        
        cursor = database_connection.cursor()
        sql_query = "SELECT Email, DiscordID, AuthDate, DiscordNickname FROM auth WHERE email = %s"
        parameterized_values = (user_email, )
        cursor.execute(sql_query, parameterized_values)
        query_results = cursor.fetchall()

        if bool(str(query_results[0][0]) == str(user_email)) is True:

            print (f"Submitted email exists in the auth database")
            return True

        if bool(len(query_results) == 0) is True:

            print(f"Submitted email does not exist in the database")
            return False