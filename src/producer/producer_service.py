from confluent_kafka import Producer
from src.config.settings import SSL_CONFIG, TOPIC
from src.common.logger import get_logger

log = get_logger("producer")

class ProducerService:
    def __init__(self):
        self.producer = Producer(SSL_CONFIG)

    def send(self, value):
        self.producer.produce(TOPIC, value.encode("utf-8"))
        self.producer.flush()
        log.info(f"Sent: {value}")
