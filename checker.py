try:
    with open("sample_config.txt", "r")
      as file:
          config = file.read()
except FileNotFoundError:
  print("ERROR: Configuration file not found.")
  exit()

print("Checking network configuration...")
print()

results = []
if "transport input telnet" in config:
 results.append("WARNING: Telnet is enabled.")
else:
   results.append("OK: Telnet is not enabled.")

if "transport input ssh" in config:
  results.append("OK: SSH is enabled.")
else:
  results.append("WARNING: SSH is not enabled.")

if "enable secret" in config:
  results.append("OK: Enable secret is not configured.")
else:
   results.append("WARNING: Enable secret is not configured.")
  
if "service password-encryption" in config:
   results.append("OK: Password encryption is enabled.")
else:
   results.append("WARNING: Password encryption is not enabled.")

if "switchport port-security" in config:
  results.append("OK: Port Security is enabled.")
else:
   results.append("WARNING: Port Security is not enabled.")

if "switchport port-security mac-address sticky" in config:
     results.append("OK: Sticky MAC is enabled.")
else:
     results.append("WARNING: Sticky MAC is not enabled.")

print("Security Check Results")
print("----------------------")

passed = 0
warnings = 0

for result in results:
    print(result)
    if result.startwith("OK:"):
        passed += 1
    elif
    result.startwith("WARNING:"):
        warnings += 1

print()
print("Summary")
print("-------")
print(f"Passed checks: {passed}")
print(f"Warnings: {warnings}")

