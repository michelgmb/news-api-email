import requests

from smtp import message_send

import datetime
import time
import schedule

api_key = "dee847eb9f494434acfda9bab5fa5d60"
# url = "https://finance.yahoo.com"
topic = "tesla"
# endpoint :
url = "https://newsapi.org/v2/everything?" \
      "q={topic}" \
      "&from=2023-09-11" \
      "&sortBy=publishedAt" \
      "&apiKey=dee847eb9f494434acfda9bab5fa5d60" \
      "&language=en" \
 \
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

body = ""
for article in articles[:20]:

    if article["title"] is not None:
        body = "Subject: Today's News1" +\
                "\n" + body + article['title'] + \
               "\n" + article['description'] + \
               "\n" + article['url'] + 2 * "\n"

body = body.encode("utf-8")
print(body)

message_send(body)

# schedule.every(1).minutes.do(message)

# Every day at 12am or 00:00 time bedtime() is called.
# schedule.every().day.at("00:00").do(message)

# schedule.every(1).minutes.do(message)
# def sudo_placement():
#     print("Get ready for Sudo Placement at Geeksforgeeks")
#
# # After every 10mins geeks() is called.
# schedule.every(1).minutes.do(sudo_placement)
# while True:
#     # Checks whether a scheduled task
#     # is pending to run or not
#     schedule.run_pending()
#     time.sleep(60)
