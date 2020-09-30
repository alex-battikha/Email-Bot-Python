import os
import smtplib
import imghdr
from email.message import EmailMessage
import re

EMAIL_ADDRESS = 'your-email@example.com'
EMAIL_PASSWORD = 'your-email-password'

firstname = 'Example'
lastname = 'Example'
address = '123 Oak Wood Road'
town = 'Your Town'
zip = 'Zip Code'
state = 'Your State'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	with open("colleges.txt") as fp:
		line = fp.readline()
		while(line):
			linesplit = re.split(r'\t+', line)
			print(linesplit[0] + " : " + linesplit[1])
			msg = EmailMessage()
			msg['Subject'] = 'A Request From A Future Applicant'
			msg['From'] = EMAIL_ADDRESS
			msg.set_content('Hello ' + linesplit[0] + ' Admissions,\n\nI just finished my overseas gap-year program and want to apply to ' + linesplit[0] + ' for the upcoming fall semester. It would mean the world to me if you could send me a shirt so I could represent your university.\n\nIf possible, could you please send to: \n\n'+ firstname + ' ' + lastname +'\n'+ address + '\n' + town + ', ' + state + ' ' + zip + '\n\nThank you,\n' + firstname + ' ' + lastname)
			msg['To'] = linesplit[1]
			line = fp.readline()		
			smtp.send_message(msg)
