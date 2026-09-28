config = """
hostname R1
!
line vty 0 4
transport input telnet
!
"""
print("Checker network configuration...")
print(config)
