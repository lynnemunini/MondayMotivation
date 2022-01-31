import smtplib
import random
import datetime as dt
now = dt.datetime.now()
year = now.year
# Get the current month
month = now.month
# Get the day of week i.e 0 for Monday
day_of_week = now.weekday()
# Make sure you've got the correct smtp address for your email provider
# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com
if day_of_week == 0:
    with open("quotes.txt") as f:
        lines = f.readlines()
        print(lines[0])
        # To select random quote from the quotes.txt file
        quote = random.choice(lines)
        # Remove black line after quote
        quote = quote.strip()
        my_email = "misslynnemunini@gmail.com"
        # Enter the email password for your account here
        # Removed my password for security purposes, for the code to work enter you account password below
        # This method only applies to gmail account
        # For Yahoo and hotmail accounts i'll share on the ReadMe
        # Very Important to Note as an error might occur
        # Google has a security feature that prevents less secure apps (The Program), from accessing your account
        # You have to turn this off manually by logging into your account, heading over to Security, Scroll down to
        # Less secure apps access and turn that on, A critical alert will be sent to your email
        # I highly recommend not using your official google account for this program,
        # make a new account to just do this.
        # If you still get errors at this point
        # Try to go through the Gmail Captcha here
        # while logged in to the Gmail account: https://accounts.google.com/DisplayUnlockCaptcha
        # Also don't hesitate to shoot me a dm on Twitter incase of any questions, @lynnemunini
        # That said, enter your account password below
        password = "@26041978"
        # Make sure you've got the correct smtp address for your email provider
        # Gmail: smtp.gmail.com
        # Hotmail: smtp.live.com
        # Outlook: outlook.office365.com
        # Yahoo: smtp.mail.yahoo.com
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="muninilynne65@gmail.com",
                                msg=f"Subject:Monday Motivation\n\nHello Sunshine, here's your Monday dose of "
                                    f"motivation.\n\n{quote}\n\nHappy New Week!")

            # Host on the cloud to ensure it runs daily, i used PythonAnywhere
            # Link on ReadMe
