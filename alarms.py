import time

def set_alarm(minutes, email):
    print(f"Alarm set for {minutes} minutes for {email}.")
    time.sleep(minutes * 60)
    print(f"Insulin Dose Alarm: {email}, time to take your insulin dose.")