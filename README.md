InstaBot
========

NOTE BIG UPDATE ON FUCTIONALITY; PLEASE UPDATE YOUR WORKING COPY AND FOLLOW NEW INSTRUCTIONS!

A simple Instagram bot that pulls trending top 100 hashtags and auto likes pictures with those hashtags to get more followers.

Developed in Python and built with the mechanize library

STILL IN DEVELOPMENT, CONTRIBUTIONS ARE WELCOME

##Requirements

1. Python is installed (Tested with version 2.6.8)
2. mechanize library is installed [Mechanize download!](http://wwwsearch.sourceforge.net/mechanize/download.html) V0.2.5
3. PyYAML libray is installed [PyYAML download!](pyyaml.org/wiki/PyYAML) V3.11
4. Authenticated your instagram account on [websta.me](http://websta.me/)
5. PycURL library installed [PycURL download!](http://pycurl.sourceforge.net/) V7.19.5
6. Registered a client for your account on [instagram](http://instagram.com/developer/clients/manage/)

##Setup
Clone this repository:
```
git clone https://github.com/marclave/InstaBot.git
```
Follow install instructions for PycURL: [instructions](PycURL Download.md)

Go to [instagram clients](http://instagram.com/developer/clients/manage/)
Register your account for a developers client
Retrieve your CLIENT SECRET and USER ID token under "Manage Clients"
To retrieve your access token, go to [instagram api console](http://instagram.com/developer/api-console/)
Run a query involving your USER ID and grab your access token from the request

Note: Ensure likes are part of the access scope [enable likes scope](https://instagram.com/oauth/authorize/?client_id=INSERT_CLIENTID&redirect_uri=INSERT_REDIRECTURI&response_type=code&scope=likes+basic)


Modify the profile to include your information, example:
```
CREDENTIALS:
  ACCESS_TOKEN: "USER_ACCESS_TOKEN"
  CLIENT_SECRET: "USER_CLIENT_SECRET"
MAXLIKES: 1000 <- If you dont want a max, input NO_MAX
PERHASHTAG: 10 <- If you dont want a max, input NO_MAX
TOP: 1 <- To use the top hashtags on Websta.me use a 1
IP: "USER_IP_ADDRESS" <- run ipconfig or ifconfig to grab your ip address
```
Note: If you do not put a 1 in the value of TOP then the program will look for a text file
called hashtags.txt.

The format for this file is to have each hashtag seperated by line, example:

```
I
Love
Python
```

Then run:
```
python InstaBot.py
```
