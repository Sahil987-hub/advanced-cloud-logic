cloud_network = {
    "vpc_id": "vpc-09911a",
    "region": "ap-south-1", # Mumbai Hub
    "servers": [
        {"id": "srv-1", "role": "web-frontend", "ports": [80, 443]},
        {"id": "srv-2", "role": "database", "ports": [3306, 22]},     # 🚨 Port 22 Risk
        {"id": "srv-3", "role": "backup-vault", "ports":[443,21]}   # 🚨 Port 21 Risk
    ]
}

management_risks = []
legacy_risks = []
secure_ports_count = 0

print(f"🕵️‍♂️ Commencing Deep-Packet Infrastructure Review for Network: {cloud_network['vpc_id']}\n")

for server in cloud_network["servers"]:
    print(f"Inspecting Asset: {server['id']} | operational Role: {server['role']}")

    for port in server["ports"]:
        if port == 22:
         print(f"  🚨 [CRITICAL] Management Port 22 is exposed on asset {server['id']}!")
         management_risks.append(server['id'])

        elif port == 21:
           print(f"  ⚠️ [WARNING] Legacy Unencrypted Port 21 is exposed on asset {server['id']}!")
           legacy_risks.append(server["id"])

        else:
             print(f"  ✅ Port {port} matches baseline corporate filtering policies.")
             secure_ports_count = secure_ports_count + 1

print("\n================ ARCHITECTURE RISK REPORT ================")
print(f"🛡️ Compliant Communication Ports Logged: {secure_ports_count}")
print(f"🔑 SSH Management Risk Remediation Queue: {management_risks}")
print(f"📂 Legacy Protocol Removal Queue (FTP):     {legacy_risks}")
print("==========================================================")
        