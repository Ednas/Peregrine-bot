async def wgu_check_verified(dst_email, conx):
    """
    Checks that the email isn't already verified before starting verification.
    Returns True if the email isn't found in the verified database
    """
    cursor = conx.cursor()
    sql = "SELECT * FROM verified WHERE email = %s"
    val = (dst_email, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    veri = bool(len(result) == 0)

    cursor = conx.cursor()
    sql = "SELECT * FROM auth WHERE email LIKE %s"
    val = (dst_email.split("@")[0], )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    auth = bool(len(result) == 0)

    return bool(veri == True and auth == True)
