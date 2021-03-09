async def wgu_sqlcheckverified(self, email, conx):
    
    print("Sanity check:\n {}".format(email))
    cursor = conx.cursor()
    sql = "SELECT * FROM verified WHERE email LIKE %s"
    val = (email, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    
    return result
