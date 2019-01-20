import smtplib
import ssl

mail_server = "smtp.gmail.com"
port = 465
admin_username = "ali.zzeynali@gmail.com"
password = "hwbdxgknnhtowggj"


def send_mail_to(end_mail, message):
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(mail_server, port, context=context)
    server.login(admin_username, password)
    server.sendmail(admin_username, end_mail, message)

