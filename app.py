import database
import alarms
import graph
import reports
import utils
from datetime import datetime

# Menu Display
def display_menu():
    print("\nDiabetes Management System")
    print("1. Register User")
    print("2. Confirm Diabetes Status")
    print("3. Input Blood Glucose Levels")
    print("4. Generate Weekly/Monthly Graphs")
    print("5. Set Insulin Dose Alarm")
    print("6. Monitor Blood Glucose Spikes")
    print("7. Send Weekly Report to Trusted Contacts")
    print("8. Exit")

# Step 1: User Registration
def register_user():
    print("\n--- User Registration ---")
    email = input("Enter your email: ").strip()
    if not utils.validate_email(email):
        print("Invalid email format.")
        return
    
    password = input("Enter your password: ").strip()
    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return
    
    if database.add_user(email, password):
        print(f"User {email} registered successfully!")
    else:
        print(f"User with email {email} already exists.")

# Step 2: Confirm Diabetes Status
def confirm_diabetes_status():
    print("\n--- Confirm Diabetes Status ---")
    email = input("Enter your email: ").strip()
    if not database.user_exists(email):
        print("User not found.")
        return
    
    has_diabetes = input("Do you have diabetes? (yes/no): ").strip().lower()
    if has_diabetes == 'yes':
        diabetes_type = input("Is it Type 1 or Type 2 diabetes? (1/2): ").strip()
        if diabetes_type not in ['1', '2']:
            print("Invalid input. Please enter 1 or 2.")
            return
        database.update_diabetes_status(email, has_diabetes, diabetes_type)
        print(f"Diabetes status updated for {email}.")
    else:
        print("No diabetes status to update.")

# Step 3: Input Blood Glucose Levels
def input_blood_glucose():
    print("\n--- Input Blood Glucose Levels ---")
    email = input("Enter your email: ").strip()
    if not database.user_exists(email):
        print("User not found.")
        return
    
    glucose_level = input("Enter your blood glucose level (mg/dL): ").strip()
    try:
        glucose_level = float(glucose_level)
    except ValueError:
        print("Invalid glucose level. Please enter a number.")
        return
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    database.add_glucose_level(email, glucose_level, timestamp)
    print(f"Glucose level of {glucose_level} mg/dL added for {email}.")

# Step 4: Generate Weekly and Monthly Graphs
def generate_graphs():
    print("\n--- Generate Blood Glucose Graphs ---")
    email = input("Enter your email: ").strip()
    if not database.user_exists(email):
        print("User not found.")
        return
    
    period = input("Generate graph for: (weekly/monthly): ").strip().lower()
    if period not in ['weekly', 'monthly']:
        print("Invalid option. Please choose 'weekly' or 'monthly'.")
        return
    
    data = database.get_glucose_data(email)
    if not data:
        print("No glucose data found.")
        return
    
    if period == 'weekly':
        graph.generate_graph(data, days=7, email=email)
    elif period == 'monthly':
        graph.generate_graph(data, days=30, email=email)

# Step 5: Set Insulin Dose Alarm
def set_insulin_alarm():
    print("\n--- Set Insulin Dose Alarm ---")
    email = input("Enter your email: ").strip()
    if not database.user_exists(email):
        print("User not found.")
        return
    
    time_in_minutes = input("Set alarm for insulin dose in how many minutes? ").strip()
    try:
        time_in_minutes = int(time_in_minutes)
    except ValueError:
        print("Invalid input. Please enter a valid number of minutes.")
        return
    
    alarms.set_alarm(time_in_minutes, email)

# Step 6: Monitor Blood Glucose Spikes
def monitor_glucose_spikes():
    print("\n--- Monitor Blood Glucose Spikes ---")
    email = input("Enter your email: ").strip()
    if not database.user_exists(email):
        print("User not found.")
        return
    
    threshold = 200  # mg/dL threshold for spikes
    data = database.get_glucose_data(email)
    spikes = [entry for entry in data if entry[1] > threshold]
    
    if spikes:
        print("Blood glucose spikes detected!")
        print(f"Sending alert for glucose values above {threshold} mg/dL...")
        database.send_alert(email, spikes)
    else:
        print("No glucose spikes detected.")

# Step 7: Send Weekly Report to Trusted Contacts
def send_weekly_report():
    print("\n--- Send Weekly Report ---")
    email = input("Enter your email: ").strip()
    if not database.user_exists(email):
        print("User not found.")
        return
    
    trusted_contacts = input("Enter email addresses of 2 trusted contacts (comma-separated): ").strip().split(',')
    if len(trusted_contacts) != 2:
        print("Please provide exactly 2 email addresses.")
        return
    
    report = reports.generate_weekly_report(email)
    database.send_report_to_contacts(trusted_contacts, report)
    print(f"Weekly report sent to {trusted_contacts[0]} and {trusted_contacts[1]}.")

# Main Loop
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-8): ").strip()
        
        if choice == '1':
            register_user()
        elif choice == '2':
            confirm_diabetes_status()
        elif choice == '3':
            input_blood_glucose()
        elif choice == '4':
            generate_graphs()
        elif choice == '5':
            set_insulin_alarm()
        elif choice == '6':
            monitor_glucose_spikes()
        elif choice == '7':
            send_weekly_report()
        elif choice == '8':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()