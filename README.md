🔍 Simple TCP Port Scanner (Network Reconnaissance Project)

🎯 Project Goal

This project is a fundamental cybersecurity tool developed in Python to perform network reconnaissance. The primary goal is to scan a target host's IP address within a specified port range to identify open TCP ports, demonstrating an understanding of network services and security assessment basics.

Skills Demonstrated

Networking Fundamentals: Practical application of TCP/IP communication and understanding of ports as service endpoints.

Python Programming: Utilizes the built-in socket library to programmatically establish connections and handle network exceptions.

Security Assessment: Execution of a basic vulnerability assessment technique (port scanning) crucial for ethical hacking and defensive monitoring.

Input Handling & Validation: Implemented regex and error handling (try/except) for robust user input (IP address and port ranges).

⚠️ ETHICAL HACKING DISCLAIMER

This tool is strictly for educational and self-testing purposes. Users must only scan targets for which they have explicit, written permission. The script includes functionality to scan the local machine (127.0.0.1) for safe testing.

🚀 How to Run the Scanner

Prerequisites: Ensure you have Python 3.x installed.

Download: Clone the repository or download the port_scanner.py file.

Execute: Run the script from your command line:

python port_scanner.py


Example 1: Scanning Localhost

The safest way to test is by scanning your own computer (localhost):

Input Prompt

User Entry

Enter the target IP address...

127.0.0.1

StartPort-EndPort:

1-1000

Example 2: Scanning a Single Port

To check if a common service like HTTP is running:

Input Prompt

User Entry

Enter the target IP address...

127.0.0.1

StartPort-EndPort:

80

⚙️ Technical Details

The core of the scanner relies on the socket.connect_ex() method. This method attempts to connect to a remote server on a specified port.

If the port is open, the connection succeeds, and connect_ex() returns 0.

If the port is closed or filtered, it returns an error code.

A timeout of 1.0 second is set to prevent the scanner from hanging on non-responsive ports, ensuring quick execution.
