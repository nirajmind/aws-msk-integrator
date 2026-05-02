from src.common.config_loader import load_config
from src.common.logger import setup_logger
from src.consumer.consumer_service import ConsumerService

def main():
    logger = setup_logger("consumer")
    config = load_config()

    consumer = ConsumerService(config, logger)
    consumer.start()

if __name__ == "__main__":
    main()
