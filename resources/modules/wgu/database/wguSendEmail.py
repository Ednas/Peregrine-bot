async def wgu_send_email(code, dst_email):
    "Sends an email to the student seeking verification"
    email_text = """Greetings!
    This email was sent to verify your discord account. To ensure that this
    email address belongs to you, please reply to the bot with '!verify'
    followed by your code: {}.
    If you run into issues, feel free to contact the @administrator & @moderator
    roles, post in the #tech-support channel, or message Ursa#1337 with any
    questions.
    """.format(code)

    email_html = """
    <html>
        <body>
            <p><b>Greetings!</b><br>
            This email was sent to verify your discord account. To ensure that this email address belongs to you, please reply to the bot with '!verify' followed by your code: {}.</p>
            <p>If you run into issues, feel free to contact the @administrator & @moderator roles, post in the #tech-support channel, or message Ursa#1337 with any questions.</p>
        </body>
    </html>
    """.format(code)

    p1 = MIMEText(email_text, "plain")
    p2 = MIMEText(email_html, "html")

    message = MIMEMultipart("alternative")
    message["Subject"] = "Verification Code"
    message["From"] = SRC_EMAIL
    message["To"] = dst_email
    message.attach(p1)
    message.attach(p2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SRC_EMAIL, EMAIL_PASS)
        server.sendmail(
            SRC_EMAIL, dst_email, message.as_string()
        )
