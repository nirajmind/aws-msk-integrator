import os
from src.common.config_loader import load_config

def test_load_config():
    config = load_config()
    
    assert "msk" in config
    assert "bootstrap_servers" in config["msk"]
    assert isinstance(config["msk"]["bootstrap_servers"], list)
    assert len(config["msk"]["bootstrap_servers"]) > 0

    assert "app" in config
    assert "retries" in config["app"]
