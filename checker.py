# ToDo
#   Format a plain hostname into a url
#   Implement proper HTTP code handling to reflect redirects etc.
#   Error handling with urllib2

# Import modules
import urllib2

# Prompt the user to input a network address
hostname = raw_input("Enter a properly-formatted URL, (including http:// or https://): ")

# Provide console feedback
print 'Checking host ' + str(hostname)

# Retrieve and print the HTTP status code
print urllib2.urlopen(hostname).getcode()
