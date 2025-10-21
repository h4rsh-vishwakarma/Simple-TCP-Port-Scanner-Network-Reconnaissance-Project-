import socket
import re
import sys
from datetime import datetime

# Define the port scanning function
def scan_port(ip, port):
    """
    Attempts to connect to a specific port on a target IP.
    Returns True if the port is open, False otherwise.
    """
    # Create a new socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout value to avoid hanging on unresponsive ports
    sock.settimeout(1.0) 

    # Attempt to establish a connection
    try:
        # If connect_ex returns 0, the connection was successful (port is open)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except socket.gaierror:
        # Hostname could not be resolved
        print("[-] Error: Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        # General socket error (e.g., network unreachable)
        print("[-] Error: Could not connect to the server.")
        sys.exit()
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")
        sys.exit()

# Main function to handle user input and execution
def main():
    # --- Target Input Validation ---
    target = input("Enter the target IP address (e.g., 127.0.0.1 for local host): ")
    
    # Simple regex pattern for IPv4
    ip_pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if not ip_pattern.match(target):
        print("[-] Invalid IP address format. Exiting.")
        return

    # --- Port Range Input Validation ---
    print("\nEnter the port range to scan (e.g., 1-100 or 80):")
    port_range_input = input("StartPort-EndPort: ")

    try:
        if '-' in port_range_input:
            # Handle range input (e.g., 1-100)
            start_port, end_port = map(int, port_range_input.split('-'))
        else:
            # Handle single port input (e.g., 80)
            start_port = end_port = int(port_range_input)

        if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port <= end_port):
            print("[-] Invalid port range. Ports must be between 1 and 65535.")
            return

    except ValueError:
        print("[-] Invalid port input. Please use 'Start-End' or a single number.")
        return

    # --- Execution ---
    print("\n" + "-"*50)
    print(f"Scanning Target: {target}")
    print(f"Scanning Ports: {start_port} to {end_port}")
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    open_ports = []

    # Iterate through the specified port range
    for port in range(start_port, end_port + 1):
        # Print status without newline to show progress
        print(f"Scanning port {port}...", end='\r')
        
        if scan_port(target, port):
            open_ports.append(port)
            # Print the success message over the progress line
            print(f"[+] Port {port:<5} is OPEN")
        
    # Final Summary
    print("-" * 50)
    if open_ports:
        print(f"[*** SCAN COMPLETE ***] Found {len(open_ports)} open ports:")
        print(open_ports)
    else:
        print("[*** SCAN COMPLETE ***] No open ports found in the specified range.")
    print("-" * 50)

if __name__ == "__main__":
    # Crucial Warning for Ethical Hacking Projects
    print("WARNING: Only scan targets you have explicit permission to test (e.g., your own local machine 127.0.0.1 or a private lab environment).")
    main()
