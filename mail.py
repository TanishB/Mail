import smtplib 
 
email_sender = input("Enter your E-Mail: \n")
password = input("Enter password: \n")
email_receiver = input("Enter receiver's mail\n") 


connection = smtplib.SMTP('smtp.gmail.com', 587) 
connection.starttls()
connection.login(email_sender, password)
message = input("What would you like to send ?\n")
connection.sendmail(email_sender, email_receiver, message)
connection.quit()