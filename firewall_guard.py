# Simulated incoming client web request access configurations
incoming_requests = [
    {"source_ip": "192.168.1.50", "payload": "GET /index.html"},
    {"source_ip": "10.0.0.12", "payload": "POST /login; drop table users"}, # 🚨 Injection Threat!
    {"source_ip": "172.16.5.4", "payload": "GET /portfolio/images"},
    {"source_ip": "192.168.1.99", "payload": "FETCH /config/keys$secret"}    # 🚨 Injection Threat!
]

malicious_logs = []
safe_traffic_count = 0

print("🛡️ Booting Intelligent Edge Gateway Traffic Inspector Engine...\n")

# Logic Loop: Analyze each network packet payload input string line-by-line
for request in incoming_requests:
    print(f"Inspecting data packet from IP: {request['source_ip']}...")
    
    # Extract the payload string text to inspect it
    traffic_payload = request["payload"]
    
    # YOUR BOOTCAMP LOGIC IMPLEMENTED HERE:
    if ";" in traffic_payload or "$" in traffic_payload:
        print(f"  🚨 [MALICIOUS INPUT DETECTED] Injection command signatures identified inside payload string!")
        print(f"  Flagged Content: '{traffic_payload}'")
        
        # Log the dangerous attacking IP address to our isolation list
        malicious_logs.append(request["source_ip"])
    else:
        print("  ✅ Payload check passed. Traffic clean.")
        safe_traffic_count = safe_traffic_count + 1
    print("-" * 50)

# Final Automation Operations Report Dashboard
print("\n================ EDGE GATEWAY CLOSURE SUMMARY ================")
print(f"🟢 Safe Public Requests Authorized:  {safe_traffic_count}")
print(f"🔴 Attacker IPs Added to Blacklist: {malicious_logs}")
print("==============================================================")
