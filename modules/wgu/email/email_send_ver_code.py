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

    email_html = open('emails/verification_email_template.html').read().format(auth_code=auth_code)

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
