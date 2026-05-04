from src.common.env_loader import load_env

env = load_env()

BOOTSTRAP = env["MSK_BOOTSTRAP"]
TOPIC = env["MSK_TOPIC"]
GROUP_ID = env["GROUP_ID"]

SSL_CONFIG = {
    "bootstrap.servers": BOOTSTRAP,
    "security.protocol": "SSL"
}
