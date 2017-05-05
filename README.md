# CMXCheck Spark Bot

# Description

This is a simple Spark bot interface to query the responsiveness of a web service. Its use is not limited to CMX Cloud health checking but that is the focus of this project.

# Example Workflow

1. User tells bot - "check https://host.domain.com"
2. Bot initiates one (or maybe a few) round(s) of checks https://host.domain.com via the HTTP health checker (currently in checker.py)
3. Bot returns text to user - "Web service responded with 200/OK in 0.733s"

# Dependencies

1. Spark Bot - https://github.com/imapex/boilerplate_sparkbot
2. urllib2 module
