import csv
import os

USER_DATA_FILE = 'users_data.csv'
GLUCOSE_DATA_FILE = 'glucose_data.csv'
ALERTS_FILE = 'alerts.csv'

# Ensure directories exist
if not os.path.exists('reports'):
    os.makedirs('reports')
if not os.path.exists('graphs'):
    os.makedirs('graphs')

# Initialize user data file if not exists
def initialize_files():
    if not os.path.isfile(USER_DATA_FILE):
        with open(USER_DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['email', 'password', 'diabetes_status', 'diabetes_type'])

    if not os.path.isfile(GLUCOSE_DATA_FILE):
        with open(GLUCOSE_DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['email', 'glucose_level', 'timestamp'])

def add_user(email, password):
    initialize_files()
    if user_exists(email):
        return False
    
    with open(USER_DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, password, 'no', ''])
    return True

def user_exists(email):
    initialize_files()
    with open(USER_DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == email:
                return True
    return False

def update_diabetes_status(email, has_diabetes, diabetes_type):
    initialize_files()
    users = []
    with open(USER_DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        users = [row for row in reader]
    
    for row in users:
        if row[0] == email:
            row[2] = has_diabetes
            row[3] = diabetes_type
    
    with open(USER_DATA_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(users)

def add_glucose_level(email, glucose_level, timestamp):
    with open(GLUCOSE_DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, glucose_level, timestamp])

def get_glucose_data(email):
    data = []
    with open(GLUCOSE_DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == email:
                data.append([row[0], float(row[1]), row[2]])
    return data

def send_alert(email, spikes):
    with open(ALERTS_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        for spike in spikes:
            writer.writerow([email, spike[1], spike[2]])
    print(f"Alert recorded for {email} for spikes: {spikes}")

def send_report_to_contacts(contacts, report_file):
    print(f"Sending report {report_file} to contacts: {contacts[0]} and {contacts[1]}")