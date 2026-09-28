try:
    with open("sample_config.txt", "r")
      as file:
          config = file.read()
except FileNotFoundError:
  print("ERROR: Configuration file not found.")
  exit()

print("Checking network configuration...")
print()


def chek_telnet(config):
   if "transport input telnet" in config:
      return "WARNING: Telnet is enabled."
   else:
      return "OK: Telnet is not enabled."

def check_ssh(config):
     if "transport input ssh" in config:
          return "OK: SSH is enabled."
     else:
          return "WARNING: SSH is not enabled."
def check_enable_secret(config):
      if "enable secret" in config:
           return "OK: Enable secret is not configured."
      else:
           return "WARNING: Enable secret is not configured."

def check_password_encryption(config): 
     if "service password-encryption" in config:
         return "OK: Password encryption is enabled."
     else:
         return "WARNING: Password encryption is not enabled."

def check_port_security(config):
    if "switchport port-security" in config:
        return "OK: Port Security is enabled."
    else:
        return"WARNING: Port Security is not enabled."

def check_sticky_mac(config):
    if "switchport port-security mac-address sticky" in config:
        return "OK: Sticky MAC is enabled."
    else:
        return "WARNING: Sticky MAC is not enabled."

results = []
results.append(check_telnet(config))
results.append(check_ssh(config))
results.append(check_enable_secret(config))
results.append(check_password_encryption(config))
results.append(check_port_security(config))
results.append(check_sticky_mac(config))

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

