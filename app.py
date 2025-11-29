from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sqlite3
from scanner import scan_ip

app = Flask(__name__)
CORS(app)

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/scan', methods=['POST'])
def api_scan():
    data = request.json
    ip = data.get("ip")
    if not ip:
        return jsonify({"error":"IP address required"}), 400
    results = scan_ip(ip)
    return jsonify(results)

@app.route('/api/results', methods=['GET'])
def get_results():
    conn = sqlite3.connect('scan_results.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM results ORDER BY timestamp DESC LIMIT 100')
    rows = c.fetchall()
    conn.close()
    results = [dict(row) for row in rows]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
