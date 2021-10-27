import smtplib
import random
import datetime as dt
now = dt.datetime.now()
year = now.year
# Get the current month
month = now.month
# Get the day of week i.e 0 for Monday
day_of_week = now.weekday()
if day_of_week == 0:
    with open("quotes.txt") as f:
        lines = f.readlines()
        # To select random quote from the quotes.txt file
        quote = random.choice(lines)
        # Remove black line after quote
        quote = quote.strip()
        my_email = "misslynnemunini@gmail.com"
        # Enter the email password for your account here
        # Removed mine for security purposes
        password = ""
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="muninilynne65@gmail.com",
                                msg=f"Subject:Monday Motivation\n\nHello Sunshine, here's your Monday dose of "
                                    f"motivation.\n\n{quote}\n\nHappy New Week!")




