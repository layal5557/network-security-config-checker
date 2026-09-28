try:
    with open("sample_config.txt", "r")
      as file:
          config = file.read()
except FileNotFoundError:
  print("ERROR: Configuration file not found.")
  exit()

print("Checking network configuration...")
print()

if "transport input telnet" in config:
  print("WARNING: Telnet is enabled.")
else:
  print("OK: Telnet is not enabled.")

if "transport input ssh" in config:
  print("OK: SSH is enabled.")
else:
  print("WARNING: SSH is not enabled.")

if "enable secret" in config:
  print("OK: Enable secret is not configured.")
else:
  print("WARNING: Enable secret is not configured.")
  
if "service password-encryption" in config:
  print("OK: Password encryption is enabled.")
else:
  print("WARNING: Password encryption is not enabled.")

if "switchport port-security" in config:
  print("OK: Port Security is enabled.")
else:
  print("WARNING: Port Security is not enabled.")

if "switchport port-security mac-address sticky" in config:
    print("OK: Sticky MAC is enabled.")
else:
    print("WARNING: Sticky MAC is not enabled.")
    
