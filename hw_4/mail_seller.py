import yaml
import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


with open('testdata.yaml') as f:
    mail_data = yaml.safe_load(f)

from_address = mail_data["mail"]
to_address = "someadress@gmail.com"
my_password = mail_data["mail_password"]
report_name = "pytest_report.html"

msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = "Here are tests result"

with open(report_name, 'rb') as file:
    part = MIMEApplication(file.read(), Name=basename(report_name))
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(report_name)
    msg.attach(part)

body = "Tests result is attached"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(from_address, my_password)
text = msg.as_string()
server.sendmail(from_address, to_address, text)
server.quit()
