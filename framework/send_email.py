# coding=utf-8
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from framework.logger import Logger

logger = Logger(logger = "Email").getlog()

#定义发送邮件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

def sendEmail(new_report, filename):
    '''
       :param report_file:获取最新的文件
       :param new_report_fail:获取最新的文件的路径
       :param now:当前生成报告的时间
       :return:

       :param sender 读取配置文件中发件人
       :param sendpwd 读取配置文件中发件人密码
       :param receiver 读取配置文件中收件人
       :return:
    '''

    sender = "bug_notice@jxyckj.com"
    # receiver = "815540932@qq.com"       # 收件是单人
    # receiver = ['285800179@qq.com','815540932@qq.com','kej@jxyckj.com']       # 收件为多人
    receiver = ['kej@jxyckj.com']       # 收件为多人
    # smtpserver = "smtp.qq.com"
    smtpserver = "smtp.exmail.qq.com"

    # username = "544752682@qq.com"
    # password = "qazkkfwahnitbfhi"
    username = "bug_notice@jxyckj.com"
    password = "1qaz!QAZ"

    # 定义邮件正文
    # 获取报告文件
    file = open(new_report, "rb")
    mail_body = file.read()

    msg = MIMEMultipart()

    file.close()
    # 邮件标题
    msg['Subject'] = Header('翔云每日巡检报告', 'utf-8')
    msg['From'] = sender
    # msg['To'] = receiver
    msg['To'] = ','.join(receiver)

    text = MIMEText(mail_body, _subtype="html", _charset="utf-8")
    msg.attach(text)

    # 发送附件
    html = MIMEApplication(open(filename, 'rb').read())
    html['Content-Type'] = 'application/octet-stream'
    html.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(html)

    smtp = smtplib.SMTP_SSL(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    logger.info("邮件已发送!")
