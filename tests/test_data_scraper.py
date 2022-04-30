import unittest

from bs4 import BeautifulSoup

from scraper import data_scraper
from utils import path_util


class DataScraperTestCase(unittest.TestCase):
	target_url = 'https://search.shopping.naver.com/search/all?query=RTX+3060TI&bt=-1&frm=NVSCPRO'

	def test_download(self):
		html_text = data_scraper.download(DataScraperTestCase.target_url)
		self.assertIsNotNone(html_text)

	def test_parse(self):
		test_file = open(f'{path_util.ROOT_DIR.joinpath("tmp").joinpath("test.html")}', 'r', encoding='UTF-8')
		data = ''
		for line in test_file.readlines():
			data += line
		test_file.close()

		product_infos = data_scraper.parse(data)
		self.assertIsNotNone(product_infos)


if __name__ == '__main__':
	unittest.main()
