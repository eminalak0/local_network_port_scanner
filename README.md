# Local Network Port Scanner Dashboard
This is a **Python-based local network port scanner** that scans devices on your local network, checks which ports are open, and displays the results in a **web dashboard**. It is a beginner-to-intermediate level cybersecurity project that can be used for portfolio purposes.

---

## Features
- Scans a given IP or range for open ports
- Detects common services on open ports (HTTP, SSH, FTP, etc.)
- Stores scan results in a local SQLite database (`scan_results.db`)
- Displays results on a **web dashboard**
- Auto-refresh dashboard for latest scans
- Beginner-friendly and easy to extend with alerts or visualizations

---

## How to Use
1. Ensure you have **Python 3.x** installed.
2. Clone the repository or download the files.
3. Open the project folder in VS Code or any Python editor.
4. Create and activate a **Python virtual environment**.
5. Install required dependencies from `requirements.txt`.
6. Run the Flask web application:

```bash
python app.py
