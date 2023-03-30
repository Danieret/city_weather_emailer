#!/usr/bin/python3

import smtplib
import ssl
import requests
from email.message import EmailMessage

API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# MODIFY CITY NAME HERE
city = "City name"
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    # MODIFY EMAIL SUBJECT HERE
    subject = "Weather update for " + city

    # MODIFY EMAIL CONTENT HERE
    body = f"The weather in {city} is {weather} and the temperature is {temperature} Celsius."

    # MODIFY SENDER AND RECEIVER EMAILS HERE
    sender_email = "your_email_address@gmail.com"
    receiver_email = "recipient_email_address@gmail.com"
    password = 'YOUR_EMAIL_PASSWORD'

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
        </body>
    </html>
    """

    message.add_alternative(html, subtype="html")

    context = ssl.create_default_context()

    print("Sending Email!")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Success")
else:
    print("An error occurred.")

