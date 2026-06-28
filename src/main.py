import sys
import json
import requests
from tkinter import messagebox
import webbrowser
from interface import AppInterface 

VERSION = "1.0.1"
VERSION_URL = "https://raw.githubusercontent.com/gabrielllzs/converter/refs/heads/main/version.json"

def check_for_updates():
    try:
        response = requests.get(VERSION_URL, timeout=5)
        # Check if response is empty
        if not response.text.strip():
            return
            
        data = json.loads(response.text)
        if data['version'] > VERSION:
            if messagebox.askyesno("Update Available", f"New version {data['version']} is available. Download now?"):
                webbrowser.open(data['download_url'])
                sys.exit() 
    except Exception as e:
        print("Could not check for updates:", e)

if __name__ == "__main__":
    check_for_updates()
    
    # FIX: Remove the 'root' argument here
    app = AppInterface() 
    app.mainloop()