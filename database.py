
import sqlite3
from config import DB_NAME

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS system_metrics (
            timestamp TEXT,
            cpu REAL,
            memory REAL,
            disk REAL,
            network REAL
        )
    ''')
    conn.commit()
    conn.close()

def insert_metrics(timestamp, cpu, memory, disk, network):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO system_metrics (timestamp, cpu, memory, disk, network)
        VALUES (?, ?, ?, ?, ?)
    ''', (timestamp, cpu, memory, disk, network))
    conn.commit()
    conn.close()

def fetch_all_metrics():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM system_metrics")
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_metrics_between(start_date, end_date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM system_metrics
        WHERE timestamp BETWEEN ? AND ?
    ''', (start_date, end_date))
    rows = cursor.fetchall()
    conn.close()
    return rows
