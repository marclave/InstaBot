import mechanize, yaml, re, time, sys

WEBSTA_URL = "http://websta.me/"
WEBSTA_LOGIN = WEBSTA_URL + "login"
WEBSTA_HASHTAG = WEBSTA_URL + "hot"
WEBSTA_LIKE = WEBSTA_URL + "api/like/"

INSTAGRAM_LOGIN = "https://instagram.com/accounts/login/"
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'


def login(br, profile):

	br.open(INSTAGRAM_LOGIN)

	br.form = list(br.forms())[0]  # Used because the form name was not named  
	br.form.set_all_readonly(False) # allow changing the .value of all controls
	
	userNameControl = br.form.find_control("username")
	userNameControl.value = profile['CREDENTIALS']['USERNAME']
	passwordControl = br.form.find_control("password")
	passwordControl.value = profile['CREDENTIALS']['PASSWORD']

	br.submit()
	br.open(WEBSTA_LOGIN) # logs into websta.me website

def getTopHashTags(br):

	br.open(WEBSTA_HASHTAG)
	topHashtags = re.findall('\"\>#(.*)\<\/a\>\<\/strong\>', br.response().read())

	return topHashtags

def getHashtagsFromFile():
    #your list of hashtags
    hashtags = []
    filename = 'hashtags.txt'
    #Hashtag file input
    f = open(filename)
    #strips newline character
    hashtags = [line.strip() for line in open(filename)]
    f.close()
    return hashtags
	
def like(br, hashtags):

	likes = 0

	for hashtag in hashtags:
		hashtaglikes = 0
		media_id = []
		br.open(WEBSTA_URL +"tag/" + hashtag)
		print "Liking #" + str(hashtag)
		
		for form in br.forms():
			form.set_all_readonly(False)
			for control in form.controls:
				if control.name == "media_id":
					media_id.append(control.value)
		for id in media_id:
			if hashtaglikes >= LIKES_PER_HASHTAG:
				hashtaglikes = 0
				break
			if likes >= MAX_LIKES:
				print "You have reached MAX_LIKES"
				print "This # is currently " + str(MAX_LIKES)
				sys.exit()
				break
			br.open(WEBSTA_LIKE + id)
			if bool(re.match("{\"status\":\"OK\",\"message\":\"LIKED\"", br.response().read())):
				print "YOU LIKED " + str(id)
				likes += 1
				hashtaglikes += 1
				time.sleep(profile['SLEEPTIME'])
			else:
				print "SOMETHING WENT WRONG"
				print br.response().read()
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
	MAX_LIKES = profile['MAXLIKES']
	LIKES_PER_HASHTAG = profile['PERHASHTAG']
	br = mechanize.Browser()

	br.addheaders = [('User-Agent', USER_AGENT), ('Accept', '*/*')] 

	login(br, profile)
	if profile['TOP'] == 1:
		hashtags = getTopHashTags(br)
	else:
		hashtags = getHashtagsFromFile()
	like(br, hashtags)
