# Port Scaner
**Repository Description**

This repository contains a simple Python script for port scanning. The script uses the Scapy library to send ICMP and TCP packets.

**Script Functions**

* `icmp_probe()` - checks if the server is available via ICMP.
* `scan()` - scans the specified server on the specified ports.
* `main()` - the main function of the script, asks the user for the hostname or IP address of the server and starts scanning.

**Script Parameters**

* `Hostname / IP Address:` - hostname or IP address of the server to be scanned.
* `ports:` - list of ports to scan. By default ports 20, 21, 22, 23, 25, 43, 53, 80, 115, 123, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 8080, 8888, 10000 are scanned.

**Script Usage**

```
python3 main.py
```

**Possible Problems**

* The script will not work if you are not root user.
* The script may not work properly if the server is behind a firewall.

**References**

* Scapy: https://scapy.readthedocs.io/en/latest/
