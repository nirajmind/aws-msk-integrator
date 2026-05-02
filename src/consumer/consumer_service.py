from kafka import KafkaConsumer
from src.common.msk_auth import get_iam_auth
import json

class ConsumerService:
    def __init__(self, config, logger):
        self.logger = logger
        self.config = config["msk"]

        self.consumer = KafkaConsumer(
            self.config["topic"],
            bootstrap_servers=self.config["bootstrap_servers"],
            security_protocol=self.config["security_protocol"],
            sasl_mechanism=self.config["sasl_mechanism"],
            sasl_oauth_token_provider=get_iam_auth(),
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            auto_offset_reset="earliest",
            enable_auto_commit=True
        )

    def start(self):
        self.logger.info("Consumer started...")
        for msg in self.consumer:
            self.logger.info(f"Received: {msg.value}")
