import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from_address = "lyhxr@example.com"
to_address = "lyhxr@example.com"
my_password = "mypass"
report_name = "report.xml"

msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = "Hello from python"

with open(report_name, 'rb') as file:
    part = MIMEApplication(file.read(), Name=basename(report_name))
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(report_name)
    msg.attach(part)

body = "Please, check the report"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.starttls()
server.login(from_address, my_password)
text = msg.as_string()
server.sendmail(from_address, to_address, text)
server.quit()
