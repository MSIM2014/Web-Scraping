import requests
from lxml import html

USERNAME = "****"
PASSWORD = "****"

LOGIN_URL = "https://www.yelp.com/login"
# URL = "https://bitbucket.org/dashboard/repositories"
URL = "https://www.yelp.com/search?attrs=NewBusiness&find_loc=Bellevue%2C+WA"

def main():
	# persist the login session open across all our requests
	session_requests = requests.session()

	# get login csrf token
	result = session_requests.get(LOGIN_URL)

	# print "result.text", result.text
	
	tree = html.fromstring(result.text)
	authenticity_token = list(set(tree.xpath("//input[@name='csrftok']/@value")))[0]

	# create payload
	payload = {
		"email": USERNAME,
		"password": PASSWORD,
		"csrftok": authenticity_token
	}

	print "payload: ", payload

	# perform login
	result = session_requests.post(
		LOGIN_URL, 
		data = payload, 
		headers = dict(referer = LOGIN_URL)
		)

	# scrape url
	result = session_requests.get(
		URL,
		headers = dict(referer = URL)
		)

	tree = html.fromstring(result.content)

	# get the value of business name
	bucket_names = tree.xpath("//a[@class='biz-name js-analytics-click']/span/text()")

	# get the value of how long ago business open
	open_n_weeks_ago = tree.xpath("//li[@class='tag-18x18_flame-dd5114']/small/text()")

	# remove empty item
	open_n_weeks_ago_clean = [w.replace('\n', '').strip() for w in open_n_weeks_ago]

	# remove leading and trailing spaces
	open_n_weeks_ago_clean_final = [item for item in open_n_weeks_ago_clean if item != '']

	print(bucket_names)
	print(open_n_weeks_ago_clean_final)

	# check if the last request was ok
	print result.ok

	# check the status from the last request
	print result.status_code

if __name__ == '__main__':
	main()
