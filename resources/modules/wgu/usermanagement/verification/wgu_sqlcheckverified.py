async def wgu_sqlcheckverified(self, message, conx):
    
    cursor = conx.cursor()
    email = message.content.split(' ')[-1]
    sql = "SELECT * FROM verified WHERE email LIKE %s"
    val = (email, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    
    return result
