async def database_delete_members(database_connection, email):
    '''Deletes members from database'''
    
    # Connect to database and delete from verified database

    cursor = database_connection.cursor(prepared=True)
    sql_query = """DELETE FROM verified WHERE Email = %s"""
    parameterized_values = (email)
    cursor.execute(sql_query, parameterized_values)
    database_connection.commit()
    
    # Connect to database and delete from auth database

    cursor = database_connection.cursor(prepared=True)
    sql_query = """DELETE FROM auth WHERE Email = %s"""
    parameterized_values = (email)
    cursor.execute(sql_query, parameterized_values)
    database_connection.commit()
    
    return