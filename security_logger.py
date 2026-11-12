# Print the supplied security event details as a single log record.
def log_event(event_id, username, ip_address, event, timestamp):
    print(f"Event ID: {event_id}, Username: {username}, IP Address: {ip_address}, Event: {event}, Timestamp: {timestamp}")
