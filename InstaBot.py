import mechanize, yaml, re, time, sys, pycurl, hmac, urllib
from hashlib import sha256

WEBSTA_URL = "http://websta.me/"
WEBSTA_HASHTAG = WEBSTA_URL + "hot"

INSTAGRAM_API = "https://api.instagram.com/v1/media/"
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'

# Function to encode the string with the IP and ID of the picture then like it
def encodeAndRequest(id):
	c = pycurl.Curl()
	signature = hmac.new(str(profile['CREDENTIALS']['CLIENT_SECRET']), profile['IP'], sha256).hexdigest()
	header = '|'.join([profile['IP'], signature])
	header = ["X-Insta-Forwarded-For: " + header]

	url = INSTAGRAM_API + id + "/likes"
	c.setopt(c.URL, url)
	c.setopt(c.POSTFIELDS, "access_token=" + str(profile['CREDENTIALS']['ACCESS_TOKEN']))
	c.setopt(pycurl.HTTPHEADER, header)
	c.perform()

	response = str(c.getinfo(c.HTTP_CODE))
	c.close()
	
	return response

# Function to parse the Top HashTag page and get the current top hashtags
def getTopHashTags(br):
	br.open(WEBSTA_HASHTAG)
	topHashtags = re.findall('\"\>#(.*)\<\/a\>\<\/strong\>', br.response().read())
	return topHashtags
	
# Function to read the hashtags from a users file if not wanting to parse the top 100
def getHashtagsFromFile():
    #your list of hashtags
    hashtags = []
    filename = 'hashtags.txt'
    #Hashtag file input
    f = open(filename)
    #strips newline character
    hashtags = [unicode(line.strip(), 'utf-8') for line in open(filename)]
    f.close()
    return hashtags
	
# Function to like hashtages
def like(br, hashtags):
    likes = 0

    for hashtag in hashtags:
        hashtaglikes = 0
        media_id = []
        response = br.open(WEBSTA_URL +"tag/" + urllib.quote(hashtag.encode('utf-8')))
        print u"Liking #%s" % hashtag
        media_id = re.findall("span class=\"like_count_(.*)\"", response.read())

        for id in media_id:

            if profile['MAXLIKES'] == "NO_MAX":
                pass
            elif likes >= int(profile['MAXLIKES']):
                print "You have reached MAX_LIKES(" + str(profile['MAXLIKES']) + ")"
                print u"This # is currently %s" % hashtag
                sys.exit()
                break

            if profile['PERHASHTAG'] == "NO_MAX":
                pass
            elif hashtaglikes >= int(profile['PERHASHTAG']):
                print "REACHED MAX_LIKES PER HASHTAG"
                print "MOVING ONTO NEXT HASHTAG"
                hashtaglikes = 0
                break

            response = encodeAndRequest(id)

            if bool(re.search("200", response)):
                print " YOU LIKED " + str(id)
                likes += 1
                hashtaglikes += 1
                time.sleep(profile['SLEEPTIME'])
            else:
                print "SOMETHING WENT WRONG"
                print response
                print "SLEEPING FOR 60 seconds"
                print "CURRENTLY LIKED " + str(likes) + " photos"
                time.sleep(60)

    print "YOU LIKED " + str(likes) + " photos"

if __name__ == "__main__":

	print "================================="
	print "            InstaBot             "
	print "    Developed by Marc Laventure  "
	print "================================="
	print ""

	profile = yaml.safe_load(open("profile.yml", "r"))	
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_equiv(False)
	br.addheaders = [('User-Agent', USER_AGENT), ('Accept', '*/*')] 

	if profile['TOP'] == 1:
		hashtags = getTopHashTags(br)
	else:
		hashtags = getHashtagsFromFile()
	like(br, hashtags)
