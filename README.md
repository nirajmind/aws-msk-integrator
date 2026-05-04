# MSK Python Client – Production‑Ready Demo

This project is a production‑inspired Python client for **Amazon MSK Serverless**, designed for:

- Kafka training
- Troubleshooting labs
- Debugging simulations
- Interview demos
- Real‑world MSK client development

It includes:

- Producer & Consumer services
- IAM authentication for MSK Serverless
- Config‑driven architecture
- Logging framework
- Error handling
- Unit tests
- Debugging utilities
- Environment variable support

---

## 📁 Project Structure

msk-lab/
│
├── src/
│   ├── producer/
│   │   ├── producer_app.py
│   │   ├── producer_service.py
│   │   ├── errors.py
│   │   └── init.py
│   │
│   ├── consumer/
│   │   ├── consumer_app.py
│   │   ├── consumer_service.py
│   │   ├── errors.py
│   │   └── init.py
│   │
│   ├── common/
│   │   ├── config_loader.py
│   │   ├── logger.py
│   │   ├── msk_auth.py
│   │   ├── exceptions.py
│   │   └── init.py
│
├── config/
│   ├── settings.yaml
│   ├── logging.yaml
│   └── sample.env
│
├── tests/
│   ├── test_config.py
│   ├── test_producer.py
│   └── test_consumer.py
│
├── requirements.txt
├── run_producer.sh
├── run_consumer.sh
└── README.md


---

## 🚀 Running the Project

### 1. Install dependencies

pip install -r requirements.txt

### 2. Configure AWS credentials

aws configure

### 3. Create `.env` file

Copy from:

config/sample.env

### 4. Run consumer

python -m src.consumer.consumer_app

### 5. Run producer

python -m src.producer.producer_app

### 6. Create Topic

python -m src.admin.admin_app

---

## 🧪 Running Tests

pytest -q

---

## 🛠 Debugging Tools

### Test MSK connectivity

python -m src.common.debug

### Validate IAM identity

aws sts get-caller-identity

---

## 🧩 Architecture Diagram

+-------------------------+         +----------------------------+
|  Laptop (VS Code)       |         |  AWS MSK Serverless        |
|                         |         |                            |
|  +-------------------+  |         |  +-----------------------+ |
|  | Producer Service  |----------->|  | Kafka Topic: hello    | |
|  +-------------------+  |         |  +-----------------------+ |
|                         |         |                            |
|  +-------------------+  |         |                            |
|  | Consumer Service  |<-----------|  Streams messages back    |
|  +-------------------+  |         |                            |
+-------------------------+         +----------------------------+


---

## 📌 Notes

- Works with **MSK Serverless** (IAM auth only)
- Uses **port 9098**
- No EC2 required
- Fully local development

---

## 📜 License

MIT
