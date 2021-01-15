async def wgu_check_record(code, username, conx):
    """
    Sends a SELECT query from the auth server and verifies the variables.
    Returns True if the code supplied matches the one populating the record.
    """
    cursor = conx.cursor()
    sql = "SELECT * FROM auth WHERE username = %s"
    val = (username, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    print(result[0][2] + ' - ' + code + '->' + str(bool(str(result[0][2]) == code)))
    return bool(str(result[0][2]) == code)
