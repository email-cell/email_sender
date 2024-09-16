import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email():
    # 获取环境变量
    smtp_host = os.getenv('SMTP_HOST')
    smtp_port = int(os.getenv('SMTP_PORT'))
    smtp_user = os.getenv('SMTP_USER')
    smtp_pass = os.getenv('SMTP_PASS')
    recipient_email = os.getenv('RECIPIENT_EMAIL')

    # 创建邮件内容
    subject = '每小时定时邮件'
    body = '这是一个测试每小时发送的邮件内容。'
    
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
