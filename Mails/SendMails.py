import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Cre import *
import pandas as pd

def mkDF(ele, filename):
    """[Makes Dataframe of the data and add it to the CSV file through Pandas]

    Args:
        ele ([List]): [List of data to be added]
        filename ([String]): [Name of the file for the data to be added]

    Returns:
        [Boolean]: [True if data is added and False if not]
    """
    try:
        DF = pd.DataFrame([ele])
        DF.to_csv(filename, mode='a', index=False, header=False)
        return True
    except:
        return False

def getUserInfo(col, ele, filename):
    """[It searches and matches the unique data entry and returns the row data of that user]

    Args:
        col ([String]): [Column name to search and match the Unique data]
        ele ([Numeric or String]): [element to match]
        filename ([String]): [The name of the file to grasp data from]

    Returns:
        [DataFrame(Series) Row]: [The data of the user in its row]
    """
    try:
        Data = pd.read_csv(filename)
        return Data.iloc[Data[Data[col]==ele].index.values[0]]
    except:
        return None

def OTPmail(OTP):
    """[Send html body for the OTP mail for email verification]

    Args:
        OTP ([int or string]): [OTP for the mail verification]

    Returns:
        [string]: [the html body for the mail including the OTP]
    """
    MSG = ""
    with open("OTPMail.txt", 'r') as file:
        msg = file.read()
        msgS = msg.split("MYOTP")
        MSG = str(OTP).join(msgS)
    return (MSG, "html")

def sendMail(body, SenderName = "Computer Engineering Departmental Notification", subject="", recievers=None):
    """[It sends the mail from the site to reciever]

    Args:
        body ([html]): [The body of mail to be sent]
        subject ([str], optional): [The subject of the mail]. Defaults to "".
        reciever ([str], optional): [The mail of the receiver]. Defaults to None. If default is called the mail will be sent to the owner.

    Returns:
        [boolean]: [If mail is sent it will be true and vice versa]
    """
    CREs = EnCre("EncCre.txt")
    print(CREs)
    Sender_Name = SenderName
    sender_email = CREs[1]
    password = CREs[2]
    print(sender_email, password)
    receiver_email = CREs[3] if recievers == None else recievers
    if not isinstance(receiver_email, (list, tuple)):
        receiver_email = [receiver_email]
    for receiver in receiver_email:
        message = MIMEMultipart("alternative")
        message["From"] = Sender_Name
        message["To"] = receiver
        message["Subject"] = subject
        MSG = MIMEText(body[0], body[1])
        message.attach(MSG)
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                print("Login successful")
                server.sendmail(sender_email, receiver, message.as_string())
                print("Mail is sent to", receiver)
        except Exception as e:
            print("MAIL IS NOT SENT BECAUSE:", e)
