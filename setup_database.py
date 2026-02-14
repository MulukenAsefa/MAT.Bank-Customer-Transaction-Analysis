# setup_database.py
import sqlite3
import os

# Ensure database folder exists
os.makedirs('Database', exist_ok=True)

# Connect to SQLite database
conn = sqlite3.connect('Database/bank.db')
cursor = conn.cursor()

# Drop table if it exists
cursor.execute("DROP TABLE IF EXISTS transactions")

# Create table
cursor.execute('''
CREATE TABLE transactions (
    Customer_ID INTEGER,
    Transaction_ID TEXT PRIMARY KEY,
    Transaction_Type TEXT,
    Amount REAL,
    Date TEXT,
    Service_Type TEXT
)
''')

# Insert sample data
sample_data = [
    (101, 'T001', 'Debit', 500, '2026-01-01', 'ATM'),
    (102, 'T002', 'Credit', 1200, '2026-01-02', 'Online'),
    (101, 'T003', 'Debit', 300, '2026-01-03', 'Branch'),
    (103, 'T004', 'Credit', 2000, '2026-01-04', 'Online'),
    (102, 'T005', 'Debit', 400, '2026-01-05', 'ATM'),
    (104, 'T006', 'Credit', 1500, '2026-01-06', 'Branch'),
    (101, 'T007', 'Credit', 700, '2026-01-07', 'Online'),
    (103, 'T008', 'Debit', 800, '2026-01-08', 'ATM')
]

cursor.executemany('''
INSERT INTO transactions (Customer_ID, Transaction_ID, Transaction_Type, Amount, Date, Service_Type)
VALUES (?, ?, ?, ?, ?, ?)
''', sample_data)

conn.commit()
conn.close()

print("✅ Database initialized with sample transactions!")
