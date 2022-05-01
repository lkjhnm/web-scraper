class KafkaProducerMock:
	def __init__(self):
		self.__queue = []

	@property
	def queue(self):
		return self.__queue

	def send(self, topic, value):
		print(f'topic : {topic}, value :{value}')
		self.__queue.append(value)

	def flush(self):
		print(f'data is flushed!, {self.__queue}')

	def close(self):
		self.__queue = []
