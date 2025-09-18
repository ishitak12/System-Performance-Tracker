# 🖥️ System Performance Tracker

A Python-based automated **System Performance Tracker** that monitors CPU, memory, disk, and network usage in real time.  
Unlike Task Manager (manual), this tool continuously logs metrics with timestamps into a database, generates daily reports, raises alerts when thresholds are crossed, and provides an interactive Streamlit dashboard for visualization.  

---

## 🚀 Features
- Real-time monitoring of **CPU, Memory, Disk, and Network usage**
- **Threshold-based alerts** (console + optional email notifications)
- **SQLite database logging** with timestamps for historical tracking
- **Automated daily performance reports** (CSV format)
- **Streamlit dashboard** with interactive charts and filters


---

## ⚙️ Installation
```bash
# Clone the repo
git clone https://github.com/<your-username>/system-health-monitor.git
cd system-health-monitor

# Install dependencies
pip install -r requirements.txt

python monitor.py

streamlit run dashboard.py


