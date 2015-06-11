InstaBot
========

NOTE BIG UPDATE ON FUCTIONALITY; PLEASE UPDATE YOUR WORKING COPY AND FOLLOW NEW INSTRUCTIONS!

A simple Instagram bot that pulls trending top 100 hashtags and auto likes pictures with those hashtags to get more followers.

Developed in Python and built with the mechanize library

STILL IN DEVELOPMENT, CONTRIBUTIONS ARE WELCOME

##Setup
Clone this repository:
```
git clone https://github.com/marclave/InstaBot.git
```
run the following command to install the required libraries:
```
sudo pip install -r requirements.txt
```

Go to [instagram clients](http://instagram.com/developer/clients/manage/)
Register your account for a developers client
Retrieve your CLIENT SECRET and USER ID token under "Manage Clients"

To get your access token:

use the "Client ID" and "Redirect URL" from the previous step and go to this address on your browser:
```
https://instagram.com/oauth/authorize/?client_id=INSERT_CLIENTID&amp;redirect_uri=INSERT_REDIRECTURI&amp;response_type=token
```
You would get redirected to your redirect url with your access token:
```
http://REDIRECT.URL/#access_token=YOUR_ACCESS_TOKEN_IS_HERE
```
now do the same thing with the following URL to authenticate likes on this Client ID:
```
https://instagram.com/oauth/authorize/?client_id=INSERT_CLIENTID&redirect_uri=INSERT_REDIRECTURI&response_type=code&scope=likes+basic
```


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

The format for this file is to have each hashtag separated by line, example:

```
I
Love
Python
```

Then run:
```
python InstaBot.py
```
