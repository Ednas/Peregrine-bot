import mysql.connector

async def peregrine_connect_database(DB_IPV4, DB_USER, DB_PASS, DB_NAME):
    '''This function provides connection to the local SQL database'''

    connection = mysql.connector.connect(

    host=DB_IPV4,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME

    )

    return connection