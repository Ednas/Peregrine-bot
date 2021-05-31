from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl

async def email_send_ver_code(database_connection, user_email, SRC_EMAIL, EMAIL_PASS):
    '''Sends an email to the student seeking verification'''

    # Collect verification code from database
    
    cursor = database_connection.cursor()
    sql_query = "SELECT AuthCode, DiscordNickname FROM auth WHERE email = %s"
    parameterized_values = (user_email, )
    cursor.execute(sql_query, parameterized_values)
    query_results = cursor.fetchall()

    # Set up variables

    auth_code = query_results[0][0]
    discord_nick = query_results[0][1]

    # Format email template with relevant information



    # Send email to user

    email_text = """Greetings, {}!
    This email was sent to verify your discord account. To ensure that this
    email address belongs to you, please reply to the bot with '!verify'
    followed by your code: {}.
    If you run into issues, feel free to contact the @administrator & @moderator
    roles, post in the #tech-support channel, or message Ursa#1337 with any
    questions.
    """.format(discord_nick, auth_code)

    email_html = open('emails/verification_email_template.html').read().replace("{auth_code}", str(auth_code))

    p1 = MIMEText(email_text, "plain")
    p2 = MIMEText(email_html, "html")

    message = MIMEMultipart("alternative")
    message["Subject"] = "Verification Code"
    message["From"] = SRC_EMAIL
    message["To"] = user_email
    message.attach(p1)
    message.attach(p2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SRC_EMAIL, EMAIL_PASS)
        server.sendmail(
            SRC_EMAIL, user_email, message.as_string()
        )
=======
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl

async def wgu_send_email(code, dst_email, SRC_EMAIL, EMAIL_PASS):
    "Sends an email to the student seeking verification"
    email_text = """Greetings!
    This email was sent to verify your discord account. To ensure that this
    email address belongs to you, please reply to the bot with: !verify {}.
    If you require assistance, please rach out to a Moderator on the Discord server. You can send a message in the channel titled #verification-support (near instant support). Alternatively, you can email jsherl1@wgu.edu (may take up to 24 hours to reply)
    questions.
    """.format(code)

    email_html = """
    <html>
        <body>
            <p><b>Greetings!</b><br>
            This email was sent to verify your discord account. To ensure that this email address belongs to you, please return to Discord and reply to the bot with the folowing command:</p> 
            <p>!verify {}</p>
            <p>If you require assistance, please reach out to a Moderator on the Discord server. You can send a message in the channel titled #verification-support (near instant support) or send an email directly to jsherl1@wgu.edu (may be up to 24 hours to respond).</p>
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
>>>>>>> master:resources/modules/wgu/database/wgu_send_email.py
