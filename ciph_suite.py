#!/usr/bin/env python3

import os
import sys
import time
import hashlib
import getpass
import subprocess
import threading
from datetime import datetime

class CiphSuite:
    def __init__(self):
        self.username = "Ciph"
        self.key_hash = hashlib.sha256("123".encode()).hexdigest()
        self.access_level = "Skid"
        self.system_initialized = False
        
    def display_header(self):
        header = """
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║    ███████╗██╗      █████╗ ██╗   ██╗██████╗ ███████╗           ║
║    ██╔════╝██║     ██╔══██╗██║   ██║██╔══██╗██╔════╝           ║
║    █████╗  ██║     ███████║██║   ██║██████╔╝█████╗             ║
║    ██╔══╝  ██║     ██╔══██║██║   ██║██╔══██╗██╔══╝             ║
║    ██║     ███████╗██║  ██║╚██████╔╝██║  ██║███████╗           ║
║    ╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝           ║
║                                                                ║  
║                                                                ║
║                                                                ║
║                                                                ║
║    Flaure [Learn You How Fuck Any Website]                     ║
║    t.me/ic1ph                                                  ║
║    Created by @Ciph_api                                        ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
        """
        print(header)
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] System Ready...")
        time.sleep(1)
        
    def authenticate(self):
        print("\n[!] Authentication Required - Access Level ROOT")
        print("[!] Mismatch will result in immediate termination\n")
        
        try:
            username = input("[?] Username: ").strip()
            if username != self.username:
                print("[X] Authentication Failed: Invalid Username")
                print("[X] System Terminated")
                sys.exit(1)
                
            key = getpass.getpass("[?] Access Key: ")
            key_hash_input = hashlib.sha256(key.encode()).hexdigest()
            
            if key_hash_input != self.key_hash:
                print("[X] Authentication Failed: Invalid Access Key")
                print("[X] System Terminated")
                sys.exit(1)
                
            print("[✓] Authentication Successful")
            print("[✓] Access Granted: ROOT Level")
            self.system_initialized = True
            time.sleep(1)
            return True
            
        except KeyboardInterrupt:
            print("\n[X] Authentication Interrupted")
            print("[X] System Terminated")
            sys.exit(1)
            
    def display_menu(self):
        if not self.system_initialized:
            print("[X] System Not Initialized")
            return
            
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.display_header()
            
            menu = """
╔════════════════════════════════════════════════════════════════╗
║                        MAIN MENU                               ║
╠════════════════════════════════════════════════════════════════╣
║  1. Ciph-Scanner    - Vulnerability Hunter                     ║
║  2. Ciph-Brute      - The Speed Demon                          ║
║  3. Ciph-SQLi-Dumper - The Exfiltrator                         ║
║  4. Exit            - Terminate Session                        ║
╚════════════════════════════════════════════════════════════════╝
            """
            print(menu)
            
            try:
                choice = input("[?] Select Module [1-4]: ").strip()
                
                if choice == "1":
                    self.launch_scanner()
                elif choice == "2":
                    self.launch_brute()
                elif choice == "3":
                    self.launch_sqli_dumper()
                elif choice == "4":
                    print("[✓] Terminating Session...")
                    print("[✓] System Shutdown Complete")
                    sys.exit(0)
                else:
                    print("[X] Invalid Choice. Please select 1-4")
                    time.sleep(2)
                    
            except KeyboardInterrupt:
                print("\n[✓] Terminating Session...")
                sys.exit(0)
                
    def launch_scanner(self):
        print("[*] Launching Ciph-Scanner...")
        try:
            subprocess.run([sys.executable, "modules/ciph_scanner.py"], check=True)
        except FileNotFoundError:
            print("[X] Ciph-Scanner module not found")
            input("[!] Press Enter to continue...")
        except subprocess.CalledProcessError:
            print("[X] Ciph-Scanner execution failed")
            input("[!] Press Enter to continue...")
            
    def launch_brute(self):
        print("[*] Launching Ciph-Brute...")
        try:
            if os.path.exists("modules/ciph_brute.exe"):
                subprocess.run(["modules/ciph_brute.exe"], check=True)
            elif os.path.exists("modules/ciph_brute"):
                subprocess.run(["modules/ciph_brute"], check=True)
            else:
                print("[*] Building Ciph-Brute from source...")
                subprocess.run(["go", "build", "-o", "modules/ciph_brute.exe", "modules/ciph_brute.go"], check=True)
                subprocess.run(["modules/ciph_brute.exe"], check=True)
        except FileNotFoundError:
            print("[X] Go compiler not found or Ciph-Brute module missing")
            input("[!] Press Enter to continue...")
        except subprocess.CalledProcessError:
            print("[X] Ciph-Brute execution failed")
            input("[!] Press Enter to continue...")
            
    def launch_sqli_dumper(self):
        print("[*] Launching Ciph-SQLi-Dumper...")
        try:
            subprocess.run([sys.executable, "modules/ciph_sqli_dumper.py"], check=True)
        except FileNotFoundError:
            print("[X] Ciph-SQLi-Dumper module not found")
            input("[!] Press Enter to continue...")
        except subprocess.CalledProcessError:
            print("[X] Ciph-SQLi-Dumper execution failed")
            input("[!] Press Enter to continue...")
            
    def run(self):
        self.display_header()
        if self.authenticate():
            self.display_menu()

def main():
    try:
        suite = CiphSuite()
        suite.run()
    except KeyboardInterrupt:
        print("\n[X] System Interrupted")
        sys.exit(1)
    except Exception as e:
        print(f"[X] Critical System Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
