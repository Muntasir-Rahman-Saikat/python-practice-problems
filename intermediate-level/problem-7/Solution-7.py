from collections import Counter

# Initialize a counter for IPs
ip_counter = Counter()

# Open the log file
with open("access.log", "r") as file:
    for line in file:
        line=line.strip()
        if not line:
            continue
        # Split the line by space and take the first part as IP
        ip = line.split()[0]
        ip_counter[ip] += 1

# Find the top 3 IPs with most requests
top_ips = ip_counter.most_common(3)

print("Top 3 IPs with most requests:")
for ip, count in top_ips:
    print(f"{ip}: {count} requests")
