from samsungtvws import SamsungTVWS

# Use your current Hotspot IP
TV_IP = '10.51.181.80' 

# Initialize the connection (ensure the TV is ON)
tv = SamsungTVWS(host=TV_IP, port=8002)

try:
    print("Fetching apps... (Check your TV for an 'Allow' prompt if it appears)")
    apps = tv.app_list()
    
    print("\n--- INSTALLED APPS AND IDS ---")
    for app in apps:
        # This prints the Name and the ID we need for the button
        print(f"NAME: {app['name']} | ID: {app['appId']}")
    print("------------------------------")
    
except Exception as e:
    print(f"Could not fetch list: {e}")