import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import uuid


def get_uuid():
    return str(uuid.uuid4())


def registration(from_, to, password, name, a, action=0):
    msg = email.message.Message()
    if action == 0:
        subj = 'Registration'
    else:
        subj = 'Forgotten password'
    msg['Subject'] = subj

    msg['From'] = from_
    msg['To'] = to
    password = password
    email_content = f'Здравствуй, {name}! Приветствуем тебя на нашем сайте волонтеров! Надеюсь, тебе понравится в нашей команде! {a}'

    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    # Login Credentials for sending the mail
    s.login(msg['From'], password)

    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

# registration('gigantina.ru@gmail.com', 'gigandev@gmail.com', 'loveCaOH2', 'Пупкин Вася')
