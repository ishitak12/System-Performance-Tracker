
from config import CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD, NETWORK_THRESHOLD
from config import SEND_EMAIL_ALERTS, EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER
import smtplib
from email.mime.text import MIMEText

def check_thresholds(cpu, memory, disk, network):
    alerts = []
    if cpu > CPU_THRESHOLD:
        alerts.append(f"CPU usage high: {cpu}%")
    if memory > MEMORY_THRESHOLD:
        alerts.append(f"Memory usage high: {memory}%")
    if disk > DISK_THRESHOLD:
        alerts.append(f"Disk usage high: {disk}%")
    if network > NETWORK_THRESHOLD:
        alerts.append(f"Network usage high: {network} MB/s")
    return alerts

def send_email_alert(message):
    if not SEND_EMAIL_ALERTS:
        return
    msg = MIMEText(message)
    msg['Subject'] = "System Alert"
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
