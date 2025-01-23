import smtplib
class MailSender:
    def __init__(self):
        self.sender_mail_address = "yourmailaddress@gmail.com"
        self.sender_app_password = "yourapppassword"

    #you need to use true smtp host, mail address, app password to not get any errors while sending mails
    #if the sending process freezes while sending, try changing ports after researching
    def send_mails(self,birthday_persons):
        #used gmail for host, for example if we send from yahoo account, it's gonna be smtp.mail.yahoo.com
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=self.sender_mail_address,password=self.sender_app_password)
            for person in birthday_persons:
                connection.sendmail(from_addr=self.sender_mail_address,
                                    to_addrs=person['email'],
                                    msg=f"Subject:HAPPY BIRTHDAY!\n\n{person['letter']}")
                print(f"Birthday Letters has send to {person['name']},{person['email']}")
