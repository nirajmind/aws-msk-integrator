from kafka import KafkaProducer
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

producer = KafkaProducer(
    bootstrap_servers=[bootstrap],
    security_protocol="SASL_SSL",
    sasl_mechanism="OAUTHBEARER",
    sasl_oauth_token_provider=TokenProvider(),
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

producer.send(topic, {"msg": "Hello from Windows!"})
producer.flush()

print("Sent!")
