import smtplib
import datetime as dt
import random

my_email = "charbat.serikbol@gmail.com"
password = '117878Tian'
receive_email = 'pearl.sailikebuli@yahoo.com'


def send_quote(quote):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receive_email,
            msg=f"Subject:Need Some Motivation?\n\n {quote}"
        )


def get_random_quote():
    with open('quotes.txt') as quote_file:
        quotes = quote_file.readlines()
    return random.choice(quotes)


now = dt.datetime.now()
day_of_week = now.weekday()
msg = get_random_quote()
if day_of_week == 0:
    send_quote(quote=msg)