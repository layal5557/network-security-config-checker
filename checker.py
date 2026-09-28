config = """
hostname R1
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
