import unittest

from scraper.data_scraper import DataScrapper
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
		data_scraper = DataScrapper()
		html_text = data_scraper.download(DataScraperTestCase.target_url)
		self.assertIsNotNone(html_text)

	def test_parse(self):
		data_scraper = DataScrapper()
		product_infos = data_scraper.parse(data=self.__test_html__, parser='naver-shopping')
		self.assertIsNotNone(product_infos)

	def test_scrap(self):
		data_scraper = DataScrapper()
		product_infos = data_scraper.scrap()
		self.assertIsNotNone(product_infos)


if __name__ == '__main__':
	unittest.main()
