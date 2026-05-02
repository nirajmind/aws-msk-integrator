from kafka import KafkaProducer
from src.common.msk_auth import get_iam_auth
import json
import time

class ProducerService:
    def __init__(self, config, logger):
        self.logger = logger
        self.config = config["msk"]

        self.producer = KafkaProducer(
            bootstrap_servers=self.config["bootstrap_servers"],
            security_protocol=self.config["security_protocol"],
            sasl_mechanism=self.config["sasl_mechanism"],
            sasl_oauth_token_provider=get_iam_auth(),
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    def send(self, message):
        try:
            self.producer.send(self.config["topic"], message)
            self.producer.flush()
            self.logger.info(f"Message sent: {message}")
        except Exception as e:
            self.logger.error(f"Producer error: {e}")
            raise
