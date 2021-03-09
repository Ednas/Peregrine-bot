async def wgu_sqlcheckverified(self, email, conx):
    
    cursor = conx.cursor()
    sql = "SELECT * FROM verified WHERE email LIKE %s"
    val = (email, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    print(result)
    
    return result
