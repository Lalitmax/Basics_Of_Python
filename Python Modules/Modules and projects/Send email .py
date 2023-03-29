# import smtplib

# # gmail and password
# main_gmail = 'lalitmaxbusiness@gmail.com'
# main_password = 'iwitlggtpqxppmup'
# send_to = 'lalit1848.be22@chitkara.edu.in'
# smtp_port = 587

# what_do_you_want_to_send = 'abcdefgh'

# # create sending some tools
# srvr = smtplib.SMTP('smtp.gmail.com', smtp_port)

# srvr.starttls()
# srvr.login(main_gmail, main_password)
# srvr.sendmail(main_gmail, send_to, what_do_you_want_to_send, "f")
# print('email successfully sent to', send_to)

# import smtplib
# from email.message import EmailMessage
# email_id = "lalitmaxbusiness@gmail.com"
# email_pas = "iwitlggtpqxppmup"

# msg = EmailMessage()
# msg["subject"] = "first mail using python and i hope you learn very"
# msg["from"] ="Lalit kumar yadav"
# msg["to"] = "lalit1848.be22@chitkara.edu.in"
# msg.set_content("how about a tnight")

# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
#     smtp.login(email_id, email_pas)
#     smtp.send_message(msg)

import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("lalitmaxbusiness@gmail.com", "iwitlggtpqxppmup")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("lalitmaxbusiness@gmail.com", "vansh2498.be22@chitkara.edu.in", message)

# terminating the session
s.quit()
