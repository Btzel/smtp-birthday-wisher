from letter_preparer import LetterPreparer
from mail_sender import MailSender

birthday_persons = LetterPreparer().birthday_persons
mail_sender = MailSender()

#send mail
mail_sender.send_mails(birthday_persons)



