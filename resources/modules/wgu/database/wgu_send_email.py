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
            <p>If you require assistance, please reach out to a Moderator on the Discord server. You can send a message in the channel titled #verification-help (near instant support) or send an email directly to jsherl1@wgu.edu (may be up to 24 hours to respond).</p>
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
