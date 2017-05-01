# CMXCheck Spark Bot

# Description

This is a simple Spark bot interface into SimpleMonitor (see below) to query the responsiveness of a web service. Its use is not limited to CMX Cloud health checking but that is the focus of this project.

# About SimpleMonitor

SimpleMonitor is a Python script which monitors hosts and network connectivity. It is designed to be quick and easy to set up and lacks complex features that can make things like Nagios, OpenNMS and Zenoss overkill for a small business or home network. Remote monitor instances can send their results back to a central location.

SimpleMonitor documentation is here: http://jamesoff.github.io/simplemonitor/

# Example Workflow

1. User tells bot - "check host.domain.com"
2. Bot initiates one (or maybe a few) round(s) of checks against host.domain.com via the HTTP health checker 
   (sits in network.py inside the Monitors folder)
3. Bot returns text to user - "Web service responded with 200/OK in 0.733s"