from src.producer.producer_service import ProducerService
from src.common.logger import setup_logger
from src.common.config_loader import load_config

def test_producer_init():
    logger = setup_logger("test")
    config = load_config()
    producer = ProducerService(config, logger)
    assert producer is not None
