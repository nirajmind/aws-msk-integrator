from confluent_kafka import Producer
from src.config.settings import SSL_CONFIG, TOPIC
from src.common.logger import get_logger

log = get_logger("producer")

def delivery_report(err, msg):
    if err:
        log.error(f"Delivery failed: {err}")
    else:
        log.info(f"Delivered to {msg.topic()} [{msg.partition()}] offset {msg.offset()}")

def main():
    log.info(f"BOOTSTRAP: {SSL_CONFIG['bootstrap.servers']}")
    log.info(f"TOPIC: {TOPIC}")

    producer = Producer(SSL_CONFIG)

    for i in range(10):
        producer.produce(TOPIC, f"msg-{i}".encode("utf-8"), callback=delivery_report)
        producer.flush()

    log.info("Produced 10 messages")

if __name__ == "__main__":
    main()
