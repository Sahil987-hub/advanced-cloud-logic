print("🔍 Launching Defensive Log Analysis Pipeline Engine...\n")
try:
    with open("production_logs.txt", "r") as log_stream:
        for line in log_stream:
            if "ALLOW_TRAFFIC_FROM" in line:
                print("🚨 [COMPLIANCE BREACH] Uninhibited routing parameter discovered inside system disk configuration!")

                print(f" Raw content logged: {line.strip()}")
                print("-" * 65)

except FileNotFoundError:
     print("❌ [CRITICAL SYSTEM ERROR] Target data source 'production_logs.txt' is missing from the directory!")
     print("   Resolution: Verify file location paths before restarting operational engine loops.")