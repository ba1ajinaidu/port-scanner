
import socket
from datetime import datetime
import sys


if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Translate the hostname to IPv4

else:
	print("Invalid amount of arguements")
	print("Usage: python3 scanner.py <ip/hostname>")

#Add a banner

print('-'*50)
print("scanning target " + target)
print("time started "+str(datetime.now()))
print('-'*50)

try:
	for port in range (70,83):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print(port)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns a error indicator

		if result == 0:
			print("Found port {.} open",format(port))

		s.close

except KeyboardInterrupt:
	print("\nExiting the program")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved, provide a proper host name")
	sys.exit()

except socket.error:
	print("couldn't connect to the server")
	sys.exit()
print("finished scanning")
