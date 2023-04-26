# Sentiment-Based-Quant-Trading-Algorithm-
Description
The code in this project retrieves news articles related to specified stock ticker symbols and stores the relevant information in a CSV file. The retrieved news headlines can be used in conjunction with a GPT-4 model to perform sentiment analysis and make trading decisions.

Prerequisites
To run this project, you'll need:

Python 3.x
The following Python libraries:
requests
pandas
os
time
datetime
newscatcherapi
You can install the required libraries using the following command:

pip install requests pandas newscatcherapi

Installation
Clone this repository or download the code.
Make sure you have Python 3.x and the required libraries installed.
Usage
Replace the key variable value in the code with your NewsCatcher API key.
Replace the symbol variable value with the stock ticker symbol you're interested in.
Set the pages variable to the number of pages you want to fetch from the NewsCatcher API.
(Optional) Update the tiklist variable with the stock symbols you're interested in.
Run the code using python <filename>.py to fetch news data and store it in a CSV file.
Important Notes
To request full access to the NewsCatcher API, please visit their website and follow their application process.
The API key provided in the code is just an example and must be replaced with your personal API key.
Be aware of the API rate limits and adjust the wait_time variable accordingly.
This code only fetches news data and stores it in a CSV file. You will need to integrate it with a GPT-4 model to perform sentiment analysis and make trading decisions.
Disclaimer
This project is for educational purposes only. The creator is not responsible for any financial gains or losses resulting from the use of this code. Please use it at your own risk.


Important Notes
- To request full access to the NewsCatcher API, please visit their website [NewsCatcher](https://newscatcherapi.com/) and follow their application process. 
- The API key provided in the code is just an example and must be replaced with your personal API key.
- Be aware of the API rate limits and adjust the wait_time variable accordingly.

