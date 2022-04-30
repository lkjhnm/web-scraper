import unittest

from bs4 import BeautifulSoup

from scraper import data_scraper
from utils import path_util


class DataScraperTestCase(unittest.TestCase):
	target_url = 'https://search.shopping.naver.com/search/all?query=RTX+3060TI&bt=-1&frm=NVSCPRO'

	def setUp(self):
		test_resources = path_util.ROOT_DIR.joinpath("tests").joinpath("resources").joinpath("test.html")
		test_file = open(f'{test_resources}', 'r', encoding='UTF-8')
		self.__test_html__ = ''
		for line in test_file.readlines():
			self.__test_html__ += line
		test_file.close()

	def test_download(self):
		html_text = data_scraper.download(DataScraperTestCase.target_url)
		self.assertIsNotNone(html_text)

	def test_parse(self):
		product_infos = data_scraper.parse(self.__test_html__)
		self.assertIsNotNone(product_infos)


if __name__ == '__main__':
	unittest.main()
