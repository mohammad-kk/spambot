import os
import sys
import time
from datetime import datetime

def send_imessage(phone_number, message):
    applescript = f'''
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{phone_number}" of targetService
        send "{message}" to targetBuddy
    end tell
    '''
    os.system(f"osascript -e '{applescript}'")


def schedule_imessage(phone_number, message, send_time, num_messages, delay_between_messages):
    current_time = datetime.now()
    target_time = datetime.strptime(send_time, "%Y-%m-%d %H:%M")

    if target_time <= current_time:
        print("Error: Target time should be in the future.")
        sys.exit(1)

    time_difference = (target_time - current_time).total_seconds()
    time.sleep(time_difference)

    for _ in range(num_messages):
        send_imessage(phone_number, message)
        time.sleep(delay_between_messages)


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python send_scheduled_imessage.py <phone_number> <message> <send_time> <num_messages> <delay_between_messages>")
        sys.exit(1)

    phone_number = sys.argv[1]
    message = sys.argv[2]
    send_time = sys.argv[3]
    num_messages = int(sys.argv[4])
    delay_between_messages = float(sys.argv[5])

    schedule_imessage(phone_number, message, send_time, num_messages, delay_between_messages)
