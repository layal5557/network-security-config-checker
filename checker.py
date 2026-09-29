import sys
try:
    filename = sys.argv[1]
    with open(filename, "r") as file:
          config = file.read()
        
except IndexError:
    print("ERROR: Please provide a configuration file.")
    exit()
except FileNotFoundError:
  print("ERROR: Configuration file not found.")
  exit()

print("Checking network configuration...")
print()


def check_telnet(config):
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
           return "OK: Enable secret is configured."
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
        
def check_console_security(config):
    if (
        "line console 0" in config
        and "password" in config
        and "login" in config
    ):
        return "OK: Console password authentication is configured."
    else:
        return "WARNING: Console password authentication may not be configured."

def check_http_server(config):
    if "ip http server" in config and "no ip http server" not in config:
        return "WARNING: HTTP server is enabled."
    else:
        return "OK: HTTP server is not enabled."

def check_https_server(config):
    if "ip https secure-server" in config and "no ip http secure-server" not in config:
        return "OK: HTTPS server is enabld."
    else:
        return "WARNING: HTTPS server is not enabled."
        
results = []
results.append(check_telnet(config))
results.append(check_ssh(config))
results.append(check_enable_secret(config))
results.append(check_password_encryption(config))
results.append(check_port_security(config))
results.append(check_sticky_mac(config))
results.append(check_console_security(config))
results.append(check_http_server(config))
results.append(check_https_server(config))

print("Security Check Results")
print("----------------------")

passed = 0
warnings = 0

for result in results:
    print(result)
    if result.startswith("OK:"):
        passed += 1
    elif result.startswith("WARNING:"):
        warnings += 1

print()
print("Summary")
print("-------")
print(f"Passed checks: {passed}")
print(f"Warnings: {warnings}")

