import datetime as dt
import smtplib, random, pandas
import os

OLD_CONTENT = '[NAME]'
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

current_date = dt.datetime.now()

def update_wish(name):
    files = os.listdir('./letter_templates')
    current_file = random.choice(files)
    file_path = os.path.join('./letter_templates', current_file)
    with open(file_path, 'r') as file:
        current_file_content = file.read()
    updated_content = current_file_content.replace(OLD_CONTENT, name)
    send_email(updated_content)

def send_email(email_content):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(
            from_addr=USERNAME,
            to_addrs="u88.rahul@gmail.com",
            msg=f"Subject: Happy Birthday\n\n{email_content}"
        )

birthday_dataset = pandas.read_csv('birthdays.csv')
birthday_list = birthday_dataset.to_dict(orient="records")
for record in birthday_list:
    if current_date.month == record['month'] and current_date.day == record['day']:
        update_wish(record['name'])




