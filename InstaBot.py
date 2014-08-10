import mechanize, yaml, re

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

def like(br, hashtags):

	br.open(WEBSTA_URL + "tag/love")

	for hashtag in hashtags:
		media_id = []
		br.open(WEBSTA_URL +"tag/" + hashtag)

		for form in br.forms():
			form.set_all_readonly(False)
			for control in form.controls:
				if control.name == "media_id":
					media_id.append(control.value)
		for id in media_id:
			br.open(WEBSTA_LIKE + id)
			if bool(re.match("{\"status\":\"OK\",\"message\":\"LIKED\"", br.response().read())):
				print "YOU LIKED" + str(id)
			else:
				print "SOMETHING WENT WRONG"
				print br.response().read()


if __name__ == "__main__":

	print "================================="
	print "            InstaBot             "
	print "    Developed by Marc Laventure  "
	print "================================="
	print ""

	profile = yaml.safe_load(open("profile.yml", "r"))	
	br = mechanize.Browser()

	br.addheaders = [('User-Agent', USER_AGENT), ('Accept', '*/*')] 

	login(br, profile)
	topHashtags = getTopHashTags(br)
	like(br, topHashtags)
