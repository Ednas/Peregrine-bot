from datetime import datetime, timedelta
import random

async def database_push_to_verified(database_connection, discord_id):
    '''Inserts a new user into the auth database to begin verification process'''

    # Collect information from auth database

    cursor = database_connection.cursor()
    sql_query = "SELECT DiscordID, DiscordUser, Email, AuthDate, AuthCode, DiscordNickname, VerifiedDate FROM auth WHERE DiscordID = %s"
    parameterized_values = (discord_id, )
    cursor.execute(sql_query, parameterized_values)
    query_results = cursor.fetchall()

    # Set up variables for verification database

    discord_id = query_results[0][0]
    discord_name = query_results[0][1]
    user_email = query_results[0][2]
    auth_date = query_results[0][3]
    auth_code = query_results[0][4]
    discord_nick = query_results[0][5]
    verified_date = datetime.now()

    # Connect to database and perform query

    cursor = database_connection.cursor()
    sql_query = "INSERT INTO verified (DiscordID, DiscordUser, Email, AuthDate, AuthCode, DiscordNickname, VerifiedDate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    parameterized_values = (discord_id, discord_name, user_email, auth_date, auth_code, discord_nick, verified_date, )
    cursor.execute(sql_query, parameterized_values)
    database_connection.commit()
    return