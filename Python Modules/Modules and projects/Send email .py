

import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("Enter yout email", "Enter your password")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("Your email", "sender email", message)

# terminating the session
s.quit()
