async def wgu_delete_record(field, conx):
    "Deletes the selected table from the table"
    # Check for symbols to qualify index type: username -> email
    cursor = conx.cursor()
    sql = ""
    val = (field, )
    if field[-5] == '#':
        sql = "DELETE FROM auth WHERE username = %s"
    else:
        sql = "DELETE FROM auth WHERE email = %s"
    cursor.execute(sql, val)
    conx.commit()

