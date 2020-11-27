from requests import post

response = post('https://cleanuri.com/api/v1/shorten', {'url': 'https://www.facebook.com'})
url = response.json().get('result_url')
print('URL encurtada: %s' % url)
