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
		html_text = data_scraper.download(DataScraperTestCase.target_url)
		parser = BeautifulSoup(markup=html_text, features='html.parser')
		products = parser.select('.basicList_item__2XT81')

		product_data = ''
		for idx, product in enumerate(products):
			name = product.select('.basicList_title__3P9Q7')[0].get_text()
			price = product.select('.price_num__2WUXn')[0].get_text()
			product_data += f'{name},{price}\n'

		self.assertNotEqual(product_data, '')

	# tmp_dir = path_util.ROOT_DIR.joinpath("tmp")
	# if not tmp_dir.exists():
	# 	tmp_dir.mkdir()
	#
	# file = open(f'{tmp_dir.joinpath("device_price.txt")}', 'w', encoding='UTF-8')
	# file.write(product_data)
	# file.close()
	#
	# print(product_data)


if __name__ == '__main__':
	unittest.main()
