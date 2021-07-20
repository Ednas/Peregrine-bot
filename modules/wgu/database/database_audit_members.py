async def database_audit_members(database_connection, email):
    '''Checks if submitted email already matches and returns results'''

    # Execute SQL query

    cursor = database_connection.cursor(prepared=True)
    sql_query = "SELECT email, username FROM verified WHERE email = %s"
    parameterized_values = (email, )
    cursor.execute(sql_query, parameterized_values)
    query_results = cursor.fetchall()

    if bool(len(query_results) >= 1) is True:

        if bool(str(query_results[0][0]) == str(email)) is True:

            print(f"{email} exists in the verified database")
            print(f"Variables are: [0]{query_results[0][0]}\n[1]{query_results[0][1]}\n[2]{query_results[0][2]}")

        return query_results[0][1], query_results[0][2]