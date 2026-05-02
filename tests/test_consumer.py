from src.consumer.consumer_service import ConsumerService
from src.common.logger import setup_logger
from src.common.config_loader import load_config

def test_consumer_init():
    logger = setup_logger("test")
    config = load_config()
    consumer = ConsumerService(config, logger)
    assert consumer is not None
