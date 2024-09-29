import csv
from datetime import datetime

def generate_weekly_report(email):
    report_file = f'reports/{email}_weekly_report.csv'
    with open(report_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Email', 'Glucose Level', 'Timestamp'])
        
        # Sample data (In actual app, this would be fetched from database)
        sample_data = [
            [email, 180, datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
            [email, 220, datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
        ]
        
        writer.writerows(sample_data)
    
    print(f"Weekly report generated for {email}: {report_file}")
    return report_file