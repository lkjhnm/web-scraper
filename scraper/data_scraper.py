import requests
from bs4 import BeautifulSoup


def download(target):
	response = requests.get(target)
	if response.ok:
		return response.text
	else:
		raise RuntimeError('HTTP Status is not OK')


def parse(data):
	parse_module = NaverShoppingParser()
	return parse_module.parse(data)


class NaverShoppingParser:
	def parse(self, data):
		parser = BeautifulSoup(markup=data, features='html.parser')
		products = parser.select('.basicList_item__2XT81')

		generator = ProductInfoGenerator()
		for idx, product in enumerate(products):
			name = product.select('.basicList_title__3P9Q7')[0].get_text()
			price = product.select('.price_num__2WUXn')[0].get_text()
			generator.put(name=name, price=price)
		return generator.get_product_infos()


class ProductInfoGenerator:
	def __init__(self):
		self.__product_infos = []

	def put(self, name, price):
		product = {name, price}
		self.__product_infos.append(product)

	def get_product_infos(self):
		return self.__product_infos
