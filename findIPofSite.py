#find the IP address of a web site

import requests
import socket
import sys
port = 80
host_name = input('enter the web address in www format ')
print(host_name)
# find the local IP
clientName = socket.gethostname()
print((f'{clientName}  clientName'))
clientIP = socket.gethostbyname(clientName)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket successfully created')
except socket.error as err:
    print(f'socket creation failed {err}')

try:
    host_ip = socket.gethostbyname(host_name)

except socket.gaierror:
    print('error resolving')
    sys.exit()
s.connect((host_ip, port))
print(f'IP address of {host_name} is {host_ip}')
print(f'your local IP is {clientIP}')

public_ip = requests.get("http://wtfismyip.com/text").text
print(f'your public IP is {public_ip}')

