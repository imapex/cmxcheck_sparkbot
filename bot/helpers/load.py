import socket
import time
import urllib2

hostname = raw_input

dns_start = time.time()
ip_address = socket.gethostbyname(hostname)
dns_end = time.time()

url = 'https://%s/' % ip_address
req = urllib2.Request(url)
req.add_header('Host', hostname)

handshake_start = time.time()
stream = urllib2.urlopen(req)
handshake_end = time.time()
