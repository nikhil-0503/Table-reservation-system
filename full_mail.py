import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(recipient_email):
    sender_email = 'Sriswaminathcafe4@gmail.com'
    sender_password = "nrgbiqxmjcgvcprx"  # Use an app-specific password if you have 2FA enabled
    subject = "This mail is to inform you that your booking at Sri Swaminath Cafe is confirmed.Have a fine Dining!"
    with open("Seat1.txt", 'r') as a:
    # Read the contents of the file
        lis = a.readlines()
        b = ",".join(map(str, lis))
        
    body = (
        f"These are the details regarding your booking at our restaurant.We hope that you have a good experience and "
        f"come later in the future. "
        f"\nYour Booked table is Confirmed, "
        f"Your table no. is: {b}."
        f"\n For any querries and complaints regarding any facility at our restaurant,We are all ears to feedbacks and dont hesitate in "
        
        f"sending us a mail to Sriswaminathcafe4@gmail.com or call 9790901427.")
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Add body to email
        message.attach(MIMEText(body, 'plain'))

        # Use Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login to the SMTP server
        text = message.as_string()  # Convert the message to a string
        server.sendmail(sender_email, recipient_email, text)  # Send the email
        server.quit()
        # Close the connection
    except Exception as e:
        print(f'Failed to send email. Error: {e}')


def send_email_admin(mail):
    sender_email = 'Sriswaminathcafe4@gamil.com'
    sender_password = 'nrgbiqxmjcgvcprx'  # Use an app-specific password if you have 2FA enabled
    recipient_email = mail
    subject = "Table Booking"
    body = (
        f"UserMail: {mail}"
        f"This is an email Test"
    )
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Add body to email
        message.attach(MIMEText(body, 'plain'))

        # Use Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login to the SMTP server
        text = message.as_string()  # Convert the message to a string
        server.sendmail(sender_email, recipient_email, text)  # Send the email
        server.quit()  # Close the connection
    except Exception as e:
        print(f'Failed to send email. Error: {e}')
