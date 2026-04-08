
Overview
CIPH-SUITE is a high-performance, multi-language security framework. By combining Python 3.12+ for deep analysis and Golang for raw speed, it bypasses advanced WAFs, Cloudflare challenges, and EDR systems.

Key Modules
1. Ciph-Scanner (Vulnerability Hunter)
Engine: Python + Playwright (Headless Stealth Mode).

Target: XSS, LFI, RFI, and RCE.

Stealth: Full HTTP Header Juggling and User-Agent rotation.

Bypass: Handles JavaScript challenges and Cloudflare Turnstile automatically.

2. Ciph-Brute (The Speed Demon)
Engine: Golang (Goroutines for true parallelism).

Speed: Uses fasthttp (10x faster than standard libraries).

Evasion: Built-in Proxy Mesh (Tor/Rotating Proxies) support.

Optimization: Bloom Filters to handle massive wordlists with zero memory lag.

3. Ciph-SQLi-Dumper (The Exfiltrator)
Method: DNS Exfiltration (Tunneling data through DNS queries to bypass WAFs).

Encoding: Multi-layered obfuscation (Hex/Unicode/Double-URL).

Speed: Binary Search algorithm for 50% faster Time-based extraction.

Installation and Setup
1. Prerequisites
Ensure you have the following installed on your system:

Python 3.12+

Go 1.21+

Git

2. Clone and Install Dependencies
Bash
# Clone the repository
git clone https://github.com/your-username/ciph-suite.git
cd ciph-suite

# Install Python requirements
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Build the Go Brute-forcer
cd modules/brute
go mod tidy
go build -o ciph_brute
How to Run
Step 1: The Login Gate
The tool is protected. You must provide the correct credentials to initialize the ROOT access.

Username: Ciph

Access Key: NoData@iq

Step 2: Start the Framework
Run the main gateway to access the interactive menu:

Bash
python ciph_suite.py
Step 3: Usage Example
Select Option 1 for Scanner.

Enter Target: https://example.com

Choose Mode: auto

Wait for the framework to hunt and generate the JSON report.

Security and Stealth Features
Anti-Fingerprinting: Spoofs browser signatures.

IP Rotation: Switches identity every X requests.

DNS Tunneling: Keeps the database extraction invisible to HTTP logs.

Legal Disclaimer
This tool is for educational purposes and authorized penetration testing only. The developer (Ciph) is not responsible for any misuse or damage caused by this framework. Always get permission before testing.
