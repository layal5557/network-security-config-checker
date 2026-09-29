# Network Security Config Checker
A Python-based tool that analyzes Cisco network configuration files and identifies common security configuration issus.
## Project Overview
This project reads a Cisco network device configuration file and performs several security checks.
The tool reports security warning and successful checks, then provides a summary of the overall configuration status.
## Security Checks
The tool checks for the following Cisco security configuration:
- Telnet
- SSH
- Enable secret
- Password encryption
- Sticky MAC
- Console security
- HTTP server
- HTTPS server
## Usage
Run the checker from the command line:
```bash
python checker.py samble_config.txt
```
## Project Structure
```text
network-security-config-checker/
|--- checker.py
|--- sample-config.txt
|--- README.md
