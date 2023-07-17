import sys
import signal

# Initialize variables
lines = []
total_size = 0
status_codes = {}

# Signal handler for keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Function to print the statistics
def print_statistics():
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")

# Register the signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Read lines from stdin and compute metrics
try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        # Check if line matches the expected format
        if len(parts) != 7 or parts[2] != 'GET' or not parts[3].startswith('/projects/') or parts[4] not in ('200', '301', '400', '401', '403', '404', '405', '500'):
            continue

        # Extract relevant information from the line
        file_size = int(parts[6])
        status_code = parts[4]

        # Update the metrics
        lines.append(line)
        total_size += file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1

        # Print statistics after every 10 lines
        if len(lines) % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_statistics()
    sys.exit(0)

