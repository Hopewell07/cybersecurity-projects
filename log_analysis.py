import re
from collections import defaultdict

# Path to the log file
log_path = "/var/log/auth.log"

# Regex pattern to find failed login attempts and extract IP
pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"

# Dict to store IP counts
failed_ips = defaultdict(int)

with open(log_path, "r") as f:
    for line in f:
        match = re.search(pattern, line)
        if match:
            ip = match.group(1)
            failed_ips[ip] += 1

print("\n🔥 Suspicious IPs with multiple failed login attempts:\n")
for ip, count in failed_ips.items():
    if count >= 3:  # Show only those with 3+ failed attempts
        print(f"IP: {ip} | Attempts: {count}")
