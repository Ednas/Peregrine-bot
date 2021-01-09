async def wgu_set_verified(username):
    "Moves the verified username and email to the verified table"
    conx = connect()
    cursor = conx.cursor()
    sql = "SELECT * FROM auth WHERE username = %s"
    val = (username, )
    cursor.execute(sql, val)
    email = cursor.fetchall()[0][0]
    sql = "INSERT INTO verified (email, username) VALUES (%s, %s)"
    val = (email, username)
    cursor.execute(sql, val)
    conx.commit()
