from src.common.env_loader import load_env

env = load_env()

BOOTSTRAP = env["bootstrap"]
TOPIC = env["topic"]
GROUP_ID = env["group_id"]

SSL_CONFIG = {
    "bootstrap.servers": BOOTSTRAP,
    "security.protocol": "SSL"
}
