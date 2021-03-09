async def wgu_sqlcheckverified(self, email, conx):
    
    cursor = conx.cursor()
    sql = "SELECT * FROM verified WHERE email LIKE %s"
    val = (email, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    
    sqlEmailMessage = discord.Embed(
        title="WGU Cyber Club Database",
        description="Query Results for: {}\n     {}.\n\n".format(email, result),
        colour=discord.Colour.dark_blue(),
    )
  
    # Standard footer and author

    sqlEmailMessage.set_footer(
        text="This is a club member run Discord officially sponsored by Western Governors University. All interactions on this server are logged. All users agree to the Discord Terms of Service"
    )
    sqlEmailMessage.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/758331935054889020/39da98d02a59e22606e230e7afe6841a.png"
    )
    sqlEmailMessage.set_author(
        name="Ursa | nchri49",
        icon_url="https://cdn.discordapp.com/avatars/454132802535817219/31626daa6b0d4a01d0213a6390c5fe3e.png",
    )



    return sqlEmailMessage
