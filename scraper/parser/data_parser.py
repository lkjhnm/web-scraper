from bs4 import BeautifulSoup


def create(name):
	if name == 'naver-shopping':
		return NaverShoppingParser()


class NaverShoppingParser:
	# noinspection PyMethodMayBeStatic
	def parse(self, data):
		parser = BeautifulSoup(markup=data, features='html.parser')
		products = parser.select('.basicList_item__2XT81')

		builder = ProductInfoBuilder()
		for product in products:
			name = product.select('.basicList_title__3P9Q7')[0].get_text()
			price = product.select('.price_num__2WUXn')[0].get_text()
			builder.put(name=name, price=price)
		return builder.product_infos


class ProductInfoBuilder:
	def __init__(self):
		self.__product_infos = []

	def put(self, name, price):
		product = {'name': name, 'price': price}
		self.__product_infos.append(product)

	@property
	def product_infos(self):
		return self.__product_infos
