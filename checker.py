config = """
hostname R1
!
enable secret MySecretPassword
!
service password-encryption
!
line vty 0 4
transport input telnet
!
"""
print("Checker network configuration...")
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
