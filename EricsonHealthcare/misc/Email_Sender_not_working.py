import smtplib, ssl
from email.message import EmailMessage

def send_email_rediff(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using Rediffmail Pro's SMTP server.

    :param sender_email: Sender's Rediffmail Pro email address
    :param sender_password: Sender's Rediffmail Pro email password
    :param recipient_email: Recipient's email address
    :param subject: Email subject
    :param body: Email body content
    """
    try:
        # Set up the email
        msg = EmailMessage()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.set_content(body)

        # Connect to Rediffmail Pro's SMTP server
        smtp_server = 'smtp.rediffmailpro.com'  # Check this with Rediffmail Pro documentation
        smtp_port = 25  # Common port for TLS encryption
        context = ssl.create_default_context()
        context.set_ciphers("DEFAULT:!DH")  # Lower SSL security level


        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.starttls()  # Upgrade to secure encrypted connection
            server.login(sender_email, sender_password)  # Log in to SMTP server
            server.send_message(msg)  # Send the email
            print("Email sent successfully.")

    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    sender = "autoresponse@ericsonhealthcare.com"
    password = "AEricsonhealthcare@123"  # Use app-specific passwords if available
    recipient = "divyamshah1234@gmail.com"
    subject = "Test Email"
    body = "This is a test email sent from Rediffmail Pro using Python."

    send_email_rediff(sender, password, recipient, subject, body)
