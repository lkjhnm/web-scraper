import requests
from bs4 import BeautifulSoup


def download(target):
	response = requests.get(target)
	if response.ok:
		return response.text
	else:
		raise RuntimeError('HTTP Status is not OK')


def parse(html):
	parser = BeautifulSoup(markup=html, features='html.parser')
