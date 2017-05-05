# Import modules
from flask import Flask, request
from flask_restplus import Api, Resource

import urllib2

# Prompt the user to input a network address
hostname = raw_input("Enter a properly-formatted URL, (including http:// or https://): ")

# ToDo: Format a plain hostname into a url

# ToDo: Implement proper HTTP code handling to reflect redirects etc.

# Provide console feedback
print 'Checking host ' + str(hostname)

# Retrieve and print the HTTP status code
print urllib2.urlopen(hostname).getcode()
