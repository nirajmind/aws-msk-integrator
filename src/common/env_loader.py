from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    return {
        "bootstrap": os.getenv("MSK_BOOTSTRAP"),
        "topic": os.getenv("TOPIC"),
        "group_id": os.getenv("GROUP_ID", "demo-group")
    }
