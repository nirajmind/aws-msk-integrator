# ⭐ **DAY 1 — Kafka Architecture & Consumer Groups Deep Dive (1.5 hours)**  

## 🎯 Goal: Make trainees *see* how Kafka works, not just hear it

---

## **1. Theory (35 minutes)**  

### **A. Kafka Architecture Recap (15 min)**  

Explain with a whiteboard:

- Broker  
- Topic  
- Partition  
- Replication  
- Producer → Broker → Consumer  
- Consumer Group  
- Offsets  

**Trainer script:**  
“Kafka is not a queue. It’s a distributed commit log. Every partition is an ordered, append‑only log. Consumers read at their own pace.”

---

### **B. Consumer Groups & Rebalancing (20 min)**  

Cover:

- Group.id  
- Partition assignment  
- Rebalancing triggers  
- Why consumers get kicked out  
- Heartbeats & session timeouts  

**Trainer script:**  
“A consumer group is a horizontal scaling unit. Kafka guarantees that a partition is consumed by only one consumer in a group.”

---

## **2. Practical Demo (35 minutes)**  

### **Demo 1 — Show messages flowing live (10 min)**  

You already have this working:

- Start consumer  
- Run producer  
- Show messages arriving  

This is your “wow” moment.

---

### **Demo 2 — Consumer Group Rebalancing (25 min)**  

Steps:

1. Start **consumer A**  
2. Start **consumer B** (same group.id)  
3. Show rebalancing logs  
4. Show partitions split between A and B  
5. Kill consumer A  
6. Show B taking over all partitions  

**Trainer script:**  
“This is rebalancing. Kafka redistributes partitions whenever group membership changes.”

---

## **3. Hands‑On Exercise (20 minutes)**  

Trainees do:

- Run consumer in one terminal  
- Run second consumer  
- Observe rebalancing  
- Kill one consumer  
- Observe takeover  

**Outcome:**  
They *feel* how consumer groups behave.

---

## ⭐ **DAY 2 — Offsets & Reprocessing Strategies (1.5 hours)**  

### 🎯 Goal: Make trainees understand offsets deeply and replay data confidently.

---

## **1. Theory (30 minutes)**  

### **A. Offset Basics (10 min)**  

- What is an offset  
- How Kafka stores offsets  
- auto.offset.reset  
- committed vs uncommitted  

### **B. Manual vs Auto Commit (10 min)**  

- enable.auto.commit  
- commitSync  
- commitAsync  
- Why manual commit is safer  

### **C. Reprocessing Strategies (10 min)**  

- Reset to earliest  
- Reset to latest  
- Replay entire topic  
- Replay only failed partitions  

---

## **2. Practical Demo (40 minutes)**  

### **Demo 1 — Auto Commit Behavior (10 min)**  

Steps:

1. Start consumer with auto commit  
2. Stop consumer  
3. Produce new messages  
4. Restart consumer  
5. Show it starts from last committed offset  

---

### **Demo 2 — Replay from Beginning (15 min)**  

Modify consumer:

```python
"auto.offset.reset": "earliest"
```

Steps:

1. Consume some messages  
2. Stop consumer  
3. Produce more messages  
4. Restart consumer with earliest  
5. Show full replay  

---

### **Demo 3 — Manual Commit (15 min)**  

Use:

```python
consumer.commit()
```

Steps:

1. Disable auto commit  
2. Consume messages  
3. Don’t commit  
4. Restart consumer  
5. Show replay from previous offset  

---

## **3. Hands‑On Exercise for DAY 2 (20 minutes)**  

Trainees:

- Run consumer with auto commit  
- Run consumer with manual commit  
- Reset offsets  
- Replay data  

**Outcome:**  
They understand offsets *visually* and *practically*.

---

## ⭐ **DAY 3 — Manual Partition Assignment (1.5 hours)**

## 🎯 Goal: Teach trainees how to control consumption at the partition level.

---

## **1. Theory for DAY 3 (30 minutes)**  

### **A. Auto vs Manual Assignment (10 min)**  

- subscribe() → group-based  
- assign() → manual  

### **B. Use Cases (10 min)**  

- Reprocessing  
- Deduplication  
- Partition affinity  
- Debugging  

### **C. Partition-Level Control (10 min)**  

- Seek to offset  
- Seek to beginning  
- Seek to end  

---

## **2. Practical Demo for DAY 3 (40 minutes)**  

### **Demo 1 — Manual Assignment (15 min)**  

Modify consumer:

```python
consumer.assign([TopicPartition("topics1", 0)])
```

Show:

- Only partition 0 is consumed  
- No rebalancing  
- No group coordination  

---

### **Demo 2 — Seek to Beginning (10 min)**  

```python
consumer.seek(TopicPartition("topics1", 0), 0)
```

Replay partition 0 from start.

---

### **Demo 3 — Seek to Specific Offset (15 min)**  

```python
consumer.seek(tp, 5)
```

Show:

- Jump to offset 5  
- Consume from there  

---

## **3. Hands‑On Exercise for DAY 3 (20 minutes)**  

Trainees:

- Assign to partition 0  
- Replay from beginning  
- Replay from offset 5  
- Compare with group-based consumption  

**Outcome:**  
They gain *surgical control* over consumption.

---
