from flask import Flask, render_template_string
from samsungtvws import SamsungTVWS
from wakeonlan import send_magic_packet
import os

app = Flask(__name__)

# --- CONFIGURATION ---
TV_IP = '10.51.181.80'
TV_MAC = 'd0:03:df:f3:91:1a'
NETFLIX_ID = '3201907018807'
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "tv_token.txt")

def get_tv():
    token = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f: token = f.read()
    return SamsungTVWS(host=TV_IP, port=8002, token=token, timeout=3)

# --- HTML/CSS INTERFACE ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { background: #1a1a1a; color: white; font-family: sans-serif; text-align: center; margin: 0; padding: 20px; }
        .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; max-width: 300px; margin: auto; }
        button { padding: 20px; font-size: 18px; border: none; border-radius: 10px; background: #333; color: white; cursor: pointer; }
        button:active { background: #555; }
        .power-on { background: #27ae60; }
        .power-off { background: #c0392b; }
        .netflix { background: #E50914; grid-column: span 3; font-weight: bold; }
        .nav-btn { background: #2980b9; }
        .vol-btn { background: #8e44ad; }
    </style>
</head>
<body>
    <h2>TV Remote</h2>
    <div class="grid">
        <button class="power-on" onclick="fetch('/cmd/ON')">ON</button>
        <div></div>
        <button class="power-off" onclick="fetch('/cmd/KEY_POWER')">OFF</button>
        
        <div></div><button onclick="fetch('/cmd/KEY_UP')">▲</button><div></div>
        <button onclick="fetch('/cmd/KEY_LEFT')">◀</button>
        <button class="nav-btn" onclick="fetch('/cmd/KEY_ENTER')">OK</button>
        <button onclick="fetch('/cmd/KEY_RIGHT')">▶</button>
        <div></div><button onclick="fetch('/cmd/KEY_DOWN')">▼</button><div></div>

        <button class="vol-btn" onclick="fetch('/cmd/KEY_VOLUP')">VOL+</button>
        <button onclick="fetch('/cmd/KEY_HOME')">HOME</button>
        <button class="vol-btn" onclick="fetch('/cmd/KEY_VOLDOWN')">VOL-</button>

        <button class="netflix" onclick="fetch('/netflix')">NETFLIX</button>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/cmd/<key>')
def send_command(key):
    if key == "ON":
        for _ in range(10): send_magic_packet(TV_MAC)
        return "Sent ON"
    
    tv = get_tv()
    tv.send_key(key)
    if tv.token:
        with open(TOKEN_FILE, "w") as f: f.write(tv.token)
    return f"Sent {key}"

@app.route('/netflix')
def launch_netflix():
    tv = get_tv()
    tv.run_app(NETFLIX_ID)
    return "Netflix Launched"

if __name__ == '__main__':
    # '0.0.0.0' allows other devices on the hotspot to see the site
    app.run(host='0.0.0.0', port=5000)