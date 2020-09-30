# Email-Bot-Python
An email bot that will email every college in the United States asking for a free t-shirt :) Inspired by hoppuman. Everything is written in python and can be run through your command line inserting the file names.

Instruction on how to use:

1) Begin by going into sendmail.py and inserting your information like house address(so colleges can ship the merch), your email and password for smtp requests to send the email via bot, first name, last name, city, zip code, and state.

2) Next you will want to create a new google account as you will be recieving many emails back and it will flood your inbox.

3) After you do that go into myaccount.google.com while logging into that same spam email and you want to turn less secure app access because we are running everything through a python file and google will try to block it to protect your email

4) Now you are ready to run your python script. The first thing you want to do is go into test.txt and enter a test email that you have access to so that we can test and see if it will work before you send all the emails to the colleges. Then, go into sendmail.py and change line 19 to test.txt in the parantheses so it will run that text file. After that, go into your command prompt and use the command "cd" and go into the folder containing these files that you downloaded. Then type this "python3 sendmail.py". Yay, it should display the college name and the email beside it if it successfully sent. Check your email that you entered into test.txt to make sure you recieved an email.

5) If you get this far, you are finally ready to send this to thousands of colleges in the United States. Go into your sendmail.py and change line 19 back to colleges.txt. Then cd into the same spot where you downloaded these files in the folder. Go back to your command prompt and run "python3 sendmail.py".

If you need any help post in the issues tab to reach out to me, I should respond right away.
