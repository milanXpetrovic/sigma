
def scrape_data_from_coinmarketcap(URL):
	"""
	Scrapes all available data about coin from coin market cap.
	Returns dict with prices, marketcap and links to social media.

	Input: URL (string) - url from coin market cap coin
	
	Retrun: data_dict (dict) - dict with scraped values
	"""

	data_dict = { 'price': price_USD,
	'volume_24h': volume24H,
	'telegram_url': telegramURL,
	'twitter_url': twitter_url,
	'contract_adress': contract_adress}


	return data_dict



def scrape_data_from_poocoin(contract_adress):
	"""
	Scrape info from poocoin webpage.

	Input: contract_adress (string)
	Return: data_dict (dict) - dict with scraped values
	"""

		data_dict = { 'price': price_USD,
	'volume_24h': volume24H}

	return data_dict



def process_scraped(input_dict):
	"""
	Merges scraped data and creates one row in dataframe with coin infos
	
	Input: 

	Return: Dataframe (row)

	"""



def fetch_twitter(twitter_url):
	"""
	Visits given url and return tvitter values.
	Return quantitative values from given user profile. 
	If there is no profile, returns None.

	Input: twitter_url (string)
	Return: Dataframe (row)
	"""


def fetch_4chan():
	"""
	Checks 4chan /biz if there is talking about given coin.
	Checks name and symbol of coin.

	Input: coin_name, coin_symbol (string) 

	Return: dataframe row
	"""


def fetch_reddit():
	"""
	Checks list of given subreddits if there is talking about given coin.
	Checks name and symbol of coin.

	Input: coin_name, coin_symbol (string)
			list_of_subreddits

	Return: dataframe row 

	"""


def fetch_telegram():




## Scrappers
def scrape_twitter(twitter_url):
	"""
	Scrapes data from given twitter_url
	
	Input: twitter_url (string)
	Return: multiple .csv files
	"""


def scrape_telegram(twitter_url):
	"""
	Scrapes given telegram channel
	
	Input: twitter_url (string)
	Return: multiple .csv files
	"""


def scrape_4chan(twitter_url):
	"""
	Scrapes data from 4chan /biz
	
	Input: twitter_url (string)
	Return: multiple .csv files
	"""
