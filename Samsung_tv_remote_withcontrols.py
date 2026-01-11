import tkinter as tk
from wakeonlan import send_magic_packet
from samsungtvws import SamsungTVWS
import os

# --- CONFIGURATION ---
TV_IP = '10.51.181.80' 
TV_MAC = 'd0:03:df:f3:91:1a'
# Netflix ID you discovered
NETFLIX_ID = '3201907018807'
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "tv_token.txt")

class TVRemoteGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Samsung Remote")
        self.root.geometry("320x550")
        self.root.configure(bg="#1a1a1a")

        self.token = self.load_token()
        self.create_widgets()

    def load_token(self):
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, "r") as f:
                return f.read()
        return None

    def get_tv(self):
        """Creates a fresh connection with a short timeout."""
        return SamsungTVWS(host=TV_IP, port=8002, token=self.token, timeout=3)

    def send_command(self, key):
        try:
            client = self.get_tv()
            client.send_key(key)
            # Update token if the TV issues a new one
            if client.token and client.token != self.token:
                self.token = client.token
                with open(TOKEN_FILE, "w") as f: f.write(self.token)
            print(f"Sent: {key}")
        except Exception as e:
            print(f"Connection Failed: {e}")

    def run_app(self, app_id):
        """Uses your specific app ID."""
        try:
            print("Opening App...")
            client = self.get_tv()
            client.app_start(app_id)
        except Exception as e:
            print(f"App Launch Failed: {e}")
            self.send_command("KEY_NETFLIX") # Fallback

    def launch_netflix(self):
        try:
            client = self.get_tv()
            # Some TVs need a small 'ping' before launching an app
            client.send_key("KEY_HOME") 
            client.run_app(NETFLIX_ID)
            print("Netflix launch command sent.")
        except Exception as e:
            print(f"App Launch Failed: {e}")
            self.send_command("KEY_NETFLIX")       

    def power_on(self):
        """Broadcasts the Magic Packet to wake the TV."""
        print(f"Sending Wake-on-LAN to {TV_MAC}...")
        # Sending multiple times helps it bypass hotspot traffic spikes
        for _ in range(15):
            send_magic_packet(TV_MAC)
        print("Done. (Note: TV must have 'Power on with Mobile' enabled)")

    def create_widgets(self):
        btn_style = {"font": ("Helvetica", 10, "bold"), "fg": "white", "bg": "#333", "activebackground": "#555"}
        
        # Power Section
        tk.Button(self.root, text="ON", bg="#27ae60", fg="white", command=self.power_on).place(x=50, y=30, width=100, height=40)
        tk.Button(self.root, text="OFF", bg="#c0392b", fg="white", command=lambda: self.send_command("KEY_POWER")).place(x=170, y=30, width=100, height=40)

        # D-Pad
        tk.Button(self.root, text="▲", **btn_style, command=lambda: self.send_command("KEY_UP")).place(x=120, y=100, width=80, height=60)
        tk.Button(self.root, text="◀", **btn_style, command=lambda: self.send_command("KEY_LEFT")).place(x=30, y=170, width=80, height=60)
        tk.Button(self.root, text="OK", bg="#2980b9", fg="white", command=lambda: self.send_command("KEY_ENTER")).place(x=120, y=170, width=80, height=60)
        tk.Button(self.root, text="▶", **btn_style, command=lambda: self.send_command("KEY_RIGHT")).place(x=210, y=170, width=80, height=60)
        tk.Button(self.root, text="▼", **btn_style, command=lambda: self.send_command("KEY_DOWN")).place(x=120, y=240, width=80, height=60)

        # Volume & System
        tk.Button(self.root, text="VOL +", **btn_style, command=lambda: self.send_command("KEY_VOLUP")).place(x=50, y=330, width=80, height=50)
        tk.Button(self.root, text="VOL -", **btn_style, command=lambda: self.send_command("KEY_VOLDOWN")).place(x=50, y=390, width=80, height=50)
        tk.Button(self.root, text="HOME", bg="#8e44ad", fg="white", command=lambda: self.send_command("KEY_HOME")).place(x=180, y=330, width=90, height=50)
        tk.Button(self.root, text="BACK", **btn_style, command=lambda: self.send_command("KEY_RETURN")).place(x=180, y=390, width=90, height=50)

        # Apps
        tk.Button(self.root, text="NETFLIX", bg="#E50914", fg="white", font=("Helvetica", 12, "bold"),
                  command=self.launch_netflix).place(x=50, y=470, width=220, height=50)

if __name__ == "__main__":
    window = tk.Tk()
    app = TVRemoteGUI(window)
    window.mainloop()