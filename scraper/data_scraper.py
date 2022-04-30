import json

import requests

from .parser import data_parser
from utils import path_util


class DataScrapper:

	def __init__(self):
		self.__metas = self.__load_meta()

	# noinspection PyMethodMayBeStatic
	def __load_meta(self):
		meta = path_util.ROOT_DIR.joinpath('scraper').joinpath('resources').joinpath('meta.json')
		with open(meta, 'r') as json_file:
			return json.load(json_file)

	def scrap(self):
		product_infos = []
		for meta in self.__metas:
			data = self.download(meta['url'])
			product_infos.append(self.parse(data, meta['parser']))
		return product_infos

	# noinspection PyMethodMayBeStatic
	def download(self, target):
		response = requests.get(target)
		if response.ok:
			return response.text
		else:
			raise RuntimeError('HTTP Status is not OK')

	# noinspection PyMethodMayBeStatic
	def parse(self, data, parser_name):
		parser = data_parser.create(parser_name)
		return parser.parse(data)
