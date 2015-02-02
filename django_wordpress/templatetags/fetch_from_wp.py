from django import template
register = template.Library()
import requests

@register.assignment_tag
def fetch_posts(url, **kwargs):
	number = 20
	if 'number' in kwargs.keys():
		number = kwargs['number']
	api_url = "https://public-api.wordpress.com/rest/v1.1/sites/%s/posts/?number=%d"%(url,number)
	return requests.get(api_url).json()['posts']

@register.assignment_tag
def fetch_latest_post(url):
	api_url = "https://public-api.wordpress.com/rest/v1.1/sites/%s/posts/?number=1"%url
	return requests.get(api_url).json()['posts']

@register.assignment_tag
def fetch_latest_comments(url, **kwargs):
	number = 1
	if 'number' in kwargs.keys():
		number = kwargs['number']
	api_url = "https://public-api.wordpress.com/rest/v1/sites/%s/comments/?number=%d"%(url,number)
	return requests.get(api_url).json()['comments']