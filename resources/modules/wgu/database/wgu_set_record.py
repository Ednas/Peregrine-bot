async def wgu_set_record(dst_email, username, code, expiry, conx):
    """
    Takes the variables and sets them as a record in the auth table if the
    email isn't in the verified table
    """
    cursor = conx.cursor()
    sql = "INSERT INTO auth (email, username, code, expiry) VALUES (%s, %s, %s, %s)"
    val = (dst_email, username, code, expiry)
    cursor.execute(sql, val)
    conx.commit()
