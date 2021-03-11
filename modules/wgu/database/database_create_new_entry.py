from datetime import datetime, timedelta
import random

async def database_create_new_entry(database_connection, user_email, discord_name, discord_id):
    '''Inserts a new user into the auth database to begin verification process'''

    # Set variables

    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    auth_code = random.randint(000000,999999)
    discord_nick = f"{discord_name[0:18]} | {user_email.split('@')[0]}"
    expiration = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')

    # Connect to database and perform query

    cursor = database_connection.cursor()
    sql_query = "INSERT INTO auth (DiscordID, DiscordUser, Email, AuthDate, AuthCode, DiscordNickname, Expiration) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    parameterized_values = (discord_id, discord_name, user_email, current_date, auth_code, discord_nick, expiration, )
    cursor.execute(sql_query, parameterized_values)
    database_connection.commit()
    return