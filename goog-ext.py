import time
from random import random
from bs4 import BeautifulSoup
import requests


class GoogleExtractor(object):

	def __init__(self, time_sec=2.0):
		"""
		Extract startupper information from Google!
		:param time_sec: seconds to wait before consecutive calls
		"""
		self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
		self.accept_language = 'en-US,en;q=0.5'
		self.w_time = time_sec
		self.last_fired = time.time()

	def is_startupper(self, name: str) -> bool:
		"""
		Check if the person in input is a startupper
		:param name: Name of the person to search for
		:return: True if the person is a startupper else False
		"""
		self.name = name.lower()
		now = time.time()
		print(f"Waiting {self.w_time} seconds to start...")
		w_tot_time = self.w_time + random()
		while now < self.last_fired + w_tot_time:
			now = time.time()
		self.last_fired = now
		print("Collection information....")
		html = self._search_name(name)
		soup = BeautifulSoup(html, 'html.parser')
		#hits = self._extract_hits(soup)
		return self._check_startup(soup)

	def _search_name(self, name: str):
		"""
		Search the name of the person on Google
		:param name: name of the person to search for
		:return: html from google search
		"""
		headers = {
			'User-Agent': self.user_agent,
			'Accept-Language': self.accept_language,
		}
		name = name.replace(' ', '+')
		r = requests.get(f'https://www.google.com/search?&q="{name}"+startup&oq="{name}"+startup', headers=headers)
		return r.text

	def _extract_hits(self, soup) -> int:
		"""
		Extract the number of results from the search
		:param soup: soup from BeautifulSoup
		:return: (int) number of hits
		"""
		text = soup.find(id='resultStats').text
		return text.split()[1]

	def _check_startup(self, soup) -> bool:
		"""
		Check if the person in associated with the term startup in one of the first 3 results
		:param soup:
		:return: True if associated with a startup, else False
		"""
		search_cards = soup.findAll("div", {"class": "g"})
		first_3_cards = search_cards[:3]
		for card in first_3_cards:
			if self._extract_search_card(card):
				return True
		return False

	def _extract_search_card(self, card_soup):
		"""
		Check if the name and the startp terms are in the search card
		:param card_soup:
		:return: True if yes else False
		"""
		ems = card_soup.findAll("em")
		ems = list(map(lambda x: x.text.lower(), ems))
		if self.name in ems and 'startup' in ems:
			return True
		else:
			return False


if __name__ == '__main__':
	ge = GoogleExtractor()
	x = ge.is_startupper('alesasdjksia ncjahks sarica')
	x = ge.is_startupper('gigi iacono')
	print(x)