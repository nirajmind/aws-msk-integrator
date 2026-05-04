from confluent_kafka import Consumer
from src.config.settings import SSL_CONFIG, TOPIC, GROUP_ID
from src.common.logger import get_logger

log = get_logger("consumer")

def main():
    log.info(f"BOOTSTRAP: {SSL_CONFIG['bootstrap.servers']}")
    log.info(f"TOPIC: {TOPIC}")
    log.info(f"GROUP: {GROUP_ID}")

    conf = {
        **SSL_CONFIG,
        "group.id": GROUP_ID,
        "auto.offset.reset": "earliest"
    }

    consumer = Consumer(conf)
    consumer.subscribe([TOPIC])

    log.info("Consuming...")

    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            log.error(msg.error())
            continue

        log.info(f"Got: {msg.value().decode('utf-8')}")

if __name__ == "__main__":
    main()
