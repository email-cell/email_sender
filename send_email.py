import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import random

msgs = [
  "注意力转移会有残留，保持长时间制作一件事情，减少耗能，不看无关的事情，看手机刷视频非常的累的",   
  "侵入性的思维，无关紧要的事情，可以先写下来，或者不理他，他不会影响你当前的状态",
   "无用的时间可以思考有用的事情，任何时间都可以利用起来，比如听无聊的讲座的时候，走路的时候等等，还记得冯卡门吗",
   "你在别人的眼中并没有那么重要，不要去过度的考虑别人，揣测别人的想法，你的生活是你自己的，不是别人的",
]


def send_email():
    # 获取环境变量
    smtp_host = os.getenv('SMTP_HOST')
    smtp_port = int(os.getenv('SMTP_PORT'))
    smtp_user = os.getenv('SMTP_USER')
    smtp_pass = os.getenv('SMTP_PASS')
    recipient_email = os.getenv('RECIPIENT_EMAIL')

    # 创建邮件内容
    subject = random.choice(msgs)
    # 随机
    
    body = random.choice(msgs)
    
    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))

    try:
        # 连接到邮件服务器
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()  # 启用 TLS
        server.login(smtp_user, smtp_pass)  # 登录
        server.sendmail(smtp_user, recipient_email, msg.as_string())
        print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    send_email()
