import unittest
from unittest.mock import patch

from mock.mock_kafka_producer import KafkaProducerMock
from scraper.handler.data_handler import KafkaHandler


class KafkaHandlerTestCase(unittest.TestCase):

	@patch.object(target=KafkaHandler, attribute='_producer', new=KafkaProducerMock())
	def test_produce(self):
		handler = KafkaHandler()
		test_data = ['test-1', 'test-2']
		handler.produce(test_data)
		mock_producer = handler.producer
		self.assertEqual(test_data, mock_producer.queue)

