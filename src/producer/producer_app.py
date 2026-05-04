from src.producer.producer_service import ProducerService
from src.config.settings import TOPIC, SSL_CONFIG
from src.common.logger import get_logger

log = get_logger("producer")

def main():
    log.info(f"BOOTSTRAP: {SSL_CONFIG['bootstrap.servers']}")
    log.info(f"TOPIC: {TOPIC}")

    svc = ProducerService()

    for i in range(10):
        svc.send(f"msg-{i}")

if __name__ == "__main__":
    main()
