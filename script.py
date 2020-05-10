from colorama import init
from termcolor import cprint
import sys
init(strip=not sys.stdout.isatty())
from pyfiglet import figlet_format
import smtplib, ssl

cprint(figlet_format('EBomber'), 'green')
port = 587 # default for starttls
smtp_server = "smtp.gmail.com"
sender_email = input("Enter email you will use to send: ")
pwd = input("Enter your password: ")
users = int(input("How many people will you send the email to?: "))
receiver_emails = []

for i in range(users):
	receiver_emails.append(input(f"Enter receiver {i}: "))

message = input("Enter message to bomb: ")
count = int(input("And finally, how many emails would you send?: "))

context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
	server.starttls(context=context)
	try:
		server.login(sender_email, pwd)
		for i in receiver_emails:
			for j in range(count):
				cprint(f"Sending email {j} to {i}...", 'green')
				server.sendmail(sender_email, i, message)
	except smtplib.SMTPAuthenticationError:
		cprint("Authentication Error", 'red')
