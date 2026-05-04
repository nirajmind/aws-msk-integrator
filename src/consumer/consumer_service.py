from confluent_kafka import Consumer
from src.config.settings import SSL_CONFIG, TOPIC, GROUP_ID
from src.common.logger import get_logger

log = get_logger("consumer")

class ConsumerService:
    def __init__(self):
        conf = {
            **SSL_CONFIG,
            "group.id": GROUP_ID,
            "auto.offset.reset": "earliest"
        }
        self.consumer = Consumer(conf)
        self.consumer.subscribe([TOPIC])

    def start(self):
        log.info("Consuming...")
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                log.error(msg.error())
                continue
            log.info(f"Got: {msg.value().decode('utf-8')}")
