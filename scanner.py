import socket
from db import init_db
import sqlite3

init_db()

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
}

def scan_ip(ip):
    results = []
    for port, service in COMMON_PORTS.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            sock.connect((ip, port))
            status = "Open"
        except:
            status = "Closed"
        finally:
            sock.close()
        results.append({"ip": ip, "port": port, "status": status, "service": service})

        # Save to DB
        conn = sqlite3.connect('scan_results.db')
        c = conn.cursor()
        c.execute(
            'INSERT INTO results (ip, port, status, service) VALUES (?,?,?,?)',
            (ip, port, status, service)
        )
        conn.commit()
        conn.close()
    return results
