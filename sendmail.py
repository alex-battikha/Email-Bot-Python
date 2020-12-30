import smtplib
import imghdr
from email.message import EmailMessage
import re
from easygui import *


def credentials():

	title = "Enter the required credentials."
	text = "T-shirt email bot"
	input_list = ["Email address", "Email Password", "First Name", "Last Name", "Address", "City", "Zip code", "State"]
	output = multenterbox(title, text, input_list)
	return output

def mainloop():
	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(output[0], output[1])
		with open("colleges.txt") as fp:
			line = fp.readline()
			while(line):
				linesplit = re.split(r'\t+', line)
				print(linesplit[0] + " : " + linesplit[1])
				msg = EmailMessage()
				msg['Subject'] = 'A Request From A Future Applicant'
				msg['From'] = output[0]
				msg.set_content('Hello ' + linesplit[0] + ' Admissions,\n\nI just finished my overseas gap-year program and want to apply to ' + linesplit[0] + ' for the upcoming fall semester. It would mean the world to me if you could send me a shirt so I could represent your university.\n\nIf possible, could you please send to: \n\n'+ output[2] + ' ' + output[3] +'\n'+ output[4] + '\n' + output[5] + ', ' + output[6] + ' ' + output[7] + '\n\nThank you,\n' + output[2] + ' ' + output[3])
				msg['To'] = linesplit[1]
				line = fp.readline()		
				smtp.send_message(msg)
output = credentials()
mainloop()
