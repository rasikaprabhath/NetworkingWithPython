#find the IP address of a given web site by creating a socket
#URL of the web site is needed to give in www. format

import requests
import socket
import sys

webaddress = input('Enter the website address in www. format : ')


#find the local IP and the client name (computer name)

clientName=socket.gethostname()
clientIP=socket.gethostbyname(clientName)


#find the website IP
try:
    websiteIP=socket.gethostbyname(webaddress)

except socket.gaierror:
    print("incorrect web site address")

public_ip = requests.get("http://wtfismyip.com/text").text

print(f" Your local computer name is {clientName} and IP Address is {clientIP}")
print(f" your public IP address is {public_ip} ")
print(f" you inquire the IP address of the web site {webaddress} and it is  {websiteIP}")
