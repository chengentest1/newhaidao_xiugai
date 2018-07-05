"""
1. 从配置文件中读取stmp配置
2. 从report文件夹下打开report.html,发送邮件
"""
import smtplib
from email.mime.text import MIMEText
import os
import sys

sys.path.append("..")


def send_email(report_file):
    with open(report_file, "rb") as f:
        body = f.read()

    # 格式化email正文
    msg = MIMEText(body, "html", "utf-8")

    # 配置email头
    msg["Subject"] = 'Api Test Ressult'
    msg["From"] = 'chengen_cg123@126.com'
    msg["To"] = '781055847@qq.com'

    # 连接smtp服务器,发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login('chengen_cg123@126.com', 'cc123456')
    smtp.sendmail('chengen_cg123@126.com', '781055847@qq.com', msg.as_string())
    print("邮件发送成功")


if __name__ == "__main__":
    send_email(r"C:\Users\cheng\PycharmProjects\newhaidao\report\test_report.html")

