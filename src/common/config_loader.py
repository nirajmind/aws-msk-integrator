import yaml
import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()

    with open("config/settings.yaml", "r") as f:
        raw = yaml.safe_load(f)

    # Replace ${VAR} with actual env values
    def resolve(value):
        if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
            env_var = value[2:-1]
            return os.getenv(env_var)
        return value

    # Recursively resolve env vars
    def walk(obj):
        if isinstance(obj, dict):
            return {k: walk(resolve(v)) for k, v in obj.items()}
        if isinstance(obj, list):
            return [walk(resolve(i)) for i in obj]
        return resolve(obj)

    return walk(raw)
