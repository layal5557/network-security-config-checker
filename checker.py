config = """
hostname R1
!
line vty 0 4
transport input telnet
!
"""
print("Checker network configuration...")

if "transport input telnet" in config:
  print("WARNING: Telnet is enabled.")
else:
  print("OK: Telnet is not enabled.")
