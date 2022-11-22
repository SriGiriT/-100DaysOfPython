import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY = "V22FTN82AXF4BBBM"
NEWS_API_KEY = "59e2241390cd4afb87c8679eab21d091"
TWILIO_SID = "ACe52b8ec3949369210debd07d18593e02"
TWILIO_AUTH_TOKEN = "004466a10426030b8db4704bd267dd90" 
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey":API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_data = yesterday_data["4. close"]
print(yesterday_closing_data)
#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closing_data = data_list[1]["4. close"]
print(day_before_yesterday_closing_data)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference_in_stock = float(yesterday_closing_data) - float(day_before_yesterday_closing_data)
print(difference_in_stock)
updown = None
if difference_in_stock>0:
    updown = "📈"
else:
    updown = "📉"


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round(difference_in_stock/float(yesterday_closing_data)*100)
print(diff_percent)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if(abs(diff_percent) > 5):
    news_params = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    print(articles)

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    first_three_articles = articles[0:3]
    print(first_three_articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {updown}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in first_three_articles]
    print(formatted_articles)
#TODO 9. - Send each article as a separate message via Twilio. 
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body= article, 
            from_="+17692091254",
            to="+919344953235"
        )


