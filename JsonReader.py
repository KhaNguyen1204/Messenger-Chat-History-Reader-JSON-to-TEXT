import json
from datetime import datetime

# JSON file path
file_path = r'name.json'  # Replace with your actual file path
output_file = r'chat_history.txt'  # TXT file to save messages

# Read the JSON file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Check if there are messages
if "messages" in data:
    messages = data["messages"]
    
    # Sort messages by timestamp
    messages.sort(key=lambda x: x['timestamp'])

    # Open TXT file to write messages
    with open(output_file, 'w', encoding='utf-8') as txt_file:
        for msg in messages:
            sender = msg.get('senderName', 'Unknown')
            text = msg.get('text', '[No content]')
            timestamp = msg.get('timestamp', 0)

            # Convert timestamp to readable date and time
            time_str = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

            # Check for unsent messages
            if msg.get('isUnsent', False):
                text = "A message was unsent"

            # Write to TXT file
            txt_file.write(f"[{time_str}] {sender}: {text}\n")

    print(f"Messages have been saved to {output_file}")
else:
    print("No messages found in the JSON file.")
