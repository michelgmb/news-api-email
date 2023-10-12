import requests

from  smtp import message_send


api_key = "dee847eb9f494434acfda9bab5fa5d60"
# url = "https://finance.yahoo.com"

# endpoint :
url = "https://newsapi.org/v2/everything?q=tesla&from" \
      "=2023-09-11&sortBy=publishedAt&apiKey=" \
      "dee847eb9f494434acfda9bab5fa5d60"
# make request
request = requests.get(url)
# content = request.text
#
# print(type(content))

# to turned it to a manipulative
# Get dictionary with data
content = request.json()
# print(type(content))
# print(content['articles'])
articles = content['articles']

body = " "
for article in articles:
    if article["title"] is not None:
        body = body + article['title'] + '\n' + article['description'] + 2*'\n'

body = body.encode("utf-8")
message_send(message=body)
