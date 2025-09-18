import psutil
import time
from datetime import datetime, date
import csv
from database import create_table, insert_metrics, fetch_all_metrics
from alerts import check_thresholds, send_email_alert

def get_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    net_io = psutil.net_io_counters()
    network = (net_io.bytes_sent + net_io.bytes_recv) / (1024 * 1024)  # MB
    return cpu, memory, disk, network

def generate_daily_report():
    data = fetch_all_metrics()
    today = date.today().strftime("%Y-%m-%d")
    today_data = [row for row in data if row[0].startswith(today)]
    
    if not today_data:
        print("No data collected today.")
        return
    
    filename = f"daily_report_{today}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'CPU', 'Memory', 'Disk', 'Network'])
        writer.writerows(today_data)
    
    print(f"✅ Daily report generated: {filename}")

def main():
    create_table()
    print("🚀 Starting System Health Monitor... Press Ctrl+C to stop.")
    
    try:
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cpu, memory, disk, network = get_metrics()
            insert_metrics(timestamp, cpu, memory, disk, network)
            
            alerts = check_thresholds(cpu, memory, disk, network)
            for alert in alerts:
                print(f"[{timestamp}] ALERT: {alert}")
                send_email_alert(alert)
            
            time.sleep(10)  # check every 10 seconds
    except KeyboardInterrupt:
        print("🛑 Monitoring stopped manually.")
        generate_daily_report()

if __name__ == "__main__":
    main()
