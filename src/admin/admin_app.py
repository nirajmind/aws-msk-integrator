from confluent_kafka.admin import AdminClient, NewTopic
from src.config.settings import SSL_CONFIG, TOPIC
from src.common.logger import get_logger

log = get_logger("admin")

def main():
    admin = AdminClient(SSL_CONFIG)

    new_topic = NewTopic(TOPIC, num_partitions=3, replication_factor=3)

    log.info(f"Creating topic: {TOPIC}")

    fs = admin.create_topics([new_topic])

    for topic, f in fs.items():
        try:
            f.result()
            log.info(f"Topic {topic} created")
        except Exception as e:
            log.error(f"Failed to create topic {topic}: {e}")

if __name__ == "__main__":
    main()
