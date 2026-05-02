from src.common.config_loader import load_config
from src.common.logger import setup_logger
from src.producer.producer_service import ProducerService
import time

def main():
    logger = setup_logger("producer")
    config = load_config()

    producer = ProducerService(config, logger)

    message = {"msg": "Hello from MSK Lab", "ts": time.time()}
    producer.send(message)

if __name__ == "__main__":
    main()
