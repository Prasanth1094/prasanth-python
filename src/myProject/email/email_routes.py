from flask import Blueprint, jsonify, request, render_template, send_file
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_routes = Blueprint("email_routes", __name__)


@email_routes.route("/email", methods=["GET"])
def send_email():
    smtp_server = os.getenv("EMAIL_HOST")
    port = os.getenv("EMAIL_PORT")
    sender_email = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("SENDER_PASSWORD")  # Use the generated app password here
    receiver_email = "prasathraj94@gmail.com"
    # Create the email content
    message = MIMEMultipart("alternative")
    message["Subject"] = "Test Email"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the email body
    text = "This is a test send email sent from Python."
    html = """\
    <html>
      <body>
        <p>This is a second test email sent from <b>Python</b>.</p>
      </body>
    </html>
    """

    # Attach the email body to the message
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    try:
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            return "Email sent successfully!"
    except smtplib.SMTPServerDisconnected as e:
        return (
            f"SMTPServerDisconnected error: {e}",
            500,
        )  # HTTP 500 Internal Server Error

    except smtplib.SMTPException as e:
        return f"SMTP error: {e}", 500  # HTTP 500 Internal Server Error

    except Exception as e:
        return f"General error: {e}", 500  # HTTP 500 Internal Server Error
