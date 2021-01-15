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
    return bool(len(result) == 0)
