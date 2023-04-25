import requests
import pandas as pd
import os
import time
from datetime import datetime, timedelta
from newscatcherapi import NewsCatcherApiClient

def get_stock_news_newscatcher(api_key, symbol, pages):
    newscatcherapi = NewsCatcherApiClient(x_api_key=api_key)

    news_data = []


    for i in range(pages):
        startTime = datetime.now()
        query = {
            "q": f"{symbol} stock",
            "lang": "en",
            "sort_by": "date",
            "page": i+1,
            "page_size": 100,
        }

        response = newscatcherapi.get_search(**query)
        data = response
   
        for article in data['articles']:
            article_date = article['published_date'][:10]
            news_data.append({
                'date': article_date,
                'symbol': symbol,
                'title': article['title'],
                'content': article['summary']
            })
        wait_time = 1
        remTime = float(wait_time-int(datetime.now().timestamp()-startTime.timestamp()))

        print(f"Waiting {remTime} seconds...")
        if remTime > 0:
            time.sleep(remTime)



    return news_data


def get_headlines_from_csv(file_name, symbol, start_date, end_date):
    data = pd.read_csv(file_name)
    filtered_data = data[(data['symbol'] == symbol) & (data['date'] >= start_date) & (data['date'] <= end_date)]
    
    headlines = filtered_data['title'].tolist()
    return headlines



def save_news_to_csv(news_data, file_name='stock_news_scracher.csv'):
    new_data_df = pd.DataFrame(news_data)

    if os.path.isfile(file_name):
        existing_data_df = pd.read_csv(file_name)
        combined_data_df = pd.concat([existing_data_df, new_data_df], ignore_index=True)
        combined_data_df.drop_duplicates(subset=['date', 'symbol', 'title', 'content'], keep='first', inplace=True)
    else:
        combined_data_df = new_data_df

    combined_data_df.to_csv(file_name, index=False)

def scrape_news_data(file_name, key, symbol, pages):
    news_data = get_stock_news_newscatcher(key, symbol, pages)
    if news_data:
        save_news_to_csv(news_data, file_name)
    else:
        print("No news data found")

file_name = 'stock_news_scracher.csv'
key = "BbLnXN4hYq-qDhkzszCg38eC0b6WT4zvFyMEftTA07I"
symbol = 'AMZN'  # Replace with the stock ticker symbol you're interested in
pages = 100
tiklist = ["AMZN","TSLA","APPL","COST","WFC","NVDA","AMD","INTC"]
for tik in tiklist:
    scrape_news_data(file_name, key, symbol, pages)

# symbol = 'AMZN'
# start_date = '2023-04-05'
# end_date = '2023-04-05'

# headlines = get_headlines_from_csv(file_name, symbol, start_date, end_date)



# print(len(headlines))
# for h in headlines:
#     print(h)
#     print()