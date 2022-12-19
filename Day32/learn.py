import smtplib

address = "smtp.gmail.com"

sender_email = 'suyashbajpai.web@gmail.com'
sender_password = 'tvfuhjbaasdbjznf'

with smtplib.SMTP(address) as connection:
    connection.starttls()
    connection.login(user=sender_email, password=sender_password)
    
    connection.sendmail(
        from_addr=sender_email,
        to_addrs='Suyash.Bajpai@ibm.com',
        msg="Subject:Congratulations Suyash. Keep it up!\n\nHey, Suyash! I appreciate you for the progress you are making. One Day at a time. One step at a time. You are now a Intermediate+ in your Python Journey. Keep Going."
    )
