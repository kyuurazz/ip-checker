import socket
import os

os.system('cls')
hostname = input(f'Please enter a domain name : ')
ip_address = socket.gethostbyname(hostname)

print(f'\nHostname \t: {hostname}')
print(f'IP Address \t: {ip_address}\n')
