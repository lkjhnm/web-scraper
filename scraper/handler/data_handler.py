from kafka import KafkaProducer


class KafkaHandler:
	_producer = None

	def __init__(self):
		if self._producer is None:
			self._producer = KafkaProducer(
				bootstrap_servers=['localhost:9092'],
			)

	@property
	def producer(self):
		return self._producer

	def produce(self, product_infos):
		# todo: topic 별도로 추출
		for product_info in product_infos:
			self._producer.send(topic='test', value=bytes(product_info, 'utf-8'))
		self._producer.flush()
