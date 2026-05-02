from kafka import KafkaConsumer
from aws_msk_iam_sasl_signer.MSKAuthTokenProvider import generate_auth_token
import json
import os
import dotenv

dotenv.load_dotenv()

class TokenProvider:
    def token(self):
        return generate_auth_token()

bootstrap = os.getenv("MSK_BOOTSTRAP")
topic = os.getenv("MSK_TOPIC")

print("BOOTSTRAP:", os.getenv("MSK_BOOTSTRAP"))
print("TOPIC:", os.getenv("MSK_TOPIC"))

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=[bootstrap],
    security_protocol="SASL_SSL",
    sasl_mechanism="OAUTHBEARER",
    sasl_oauth_token_provider=TokenProvider(),
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True
)

print("Waiting for messages...")

for msg in consumer:
    print("Received:", msg.value)
