import requests
from datetime import datetime
from datetime import timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
SHORT_COMPANY_NAME = "tesla"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
ALPHAVANTAGE_END_POINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = "JQD2P9X07EEKEHV3"

alphavantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY
}

response = requests.get(ALPHAVANTAGE_END_POINT, params=alphavantage_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

lwd_open = float(data_list[0]["4. close"])
pdtolwd_close = float(data_list[1]["4. close"])

stock_variation = ((lwd_open - pdtolwd_close) / pdtolwd_close) * 100

if (stock_variation > 5.0 or stock_variation < -0.0):
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    NEWSAPI_END_POINT = "https://newsapi.org/v2/everything"
    NEWSAPI_API_KEY = "669d5be527434a3ebca0744cc12cdc1c"
    #https://newsapi.org/v2/everything?q=tsla&from=2021-05-28&sortedBy:publishedAt&apiKey=669d5be527434a3ebca0744cc12cdc1c
    newsapi_parameters = {
        "q": SHORT_COMPANY_NAME,
        "from": "2021-05-28",
        "sortBy": "publishedAt",
        "apikey": NEWSAPI_API_KEY
        #"pageSize": 3,
        #"page":1
    }

    newsapi_response = requests.get(NEWSAPI_END_POINT, params=newsapi_parameters)
    newsapi_response.raise_for_status()
    articles = newsapi_response.json()["articles"]
    three_articles = articles[:3]

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    #Optional: Format the SMS message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """
    TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
    TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        print(article)
        message = client.messages \
            .create(
            body=article,
            from_='+15596488122',
            to='++33652734884'
        )
    print(message)
