---
layout: default
title: "Apache Kafka"
---

# 📨 Apache Kafka - Event Streaming Platform

Apache Kafka is a distributed event streaming platform that enables real-time data pipelines and applications. It's the backbone of modern data infrastructure for handling high-throughput, low-latency event streaming.

## Core Concepts

### What is Apache Kafka?

Kafka is a publish-subscribe messaging system that allows:
- **Real-time data**: Process and react to data in real-time
- **Durability**: Store streams of data safely across distributed clusters
- **Scalability**: Handle massive volumes of data with horizontal scaling
- **Decoupling**: Producers and consumers work independently

### Key Terminology

**Topic**: A category of events (similar to a table)  
**Partition**: Parallel unit within a topic for scalability  
**Broker**: Individual server in a Kafka cluster  
**Producer**: Application that publishes events  
**Consumer**: Application that subscribes to topics  
**Consumer Group**: Set of consumers sharing a topic  

---

## Getting Started

### Installation

```bash
# Download Kafka
wget https://archive.apache.org/dist/kafka/3.6.0/kafka_2.13-3.6.0.tgz
tar -xzf kafka_2.13-3.6.0.tgz
cd kafka_2.13-3.6.0

# Start ZooKeeper
bin/zookeeper-server-start.sh config/zookeeper.properties &

# Start Kafka broker
bin/kafka-server-start.sh config/server.properties &
```

### Create Topic

```bash
bin/kafka-topics.sh --create \
  --topic my-topic \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1
```

---

## Producer Example

```python
from kafka import KafkaProducer
import json
import time

# Create producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send events
for i in range(100):
    event = {
        'id': i,
        'timestamp': time.time(),
        'value': f'Event {i}'
    }
    producer.send('my-topic', value=event)

producer.flush()
producer.close()
```

## Consumer Example

```python
from kafka import KafkaConsumer
import json

# Create consumer
consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='my-group'
)

# Consume events
for message in consumer:
    print(f"Received: {message.value}")
```

---

## Advanced Topics

### Stream Processing with Kafka Streams

```python
from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError

def stream_processing():
    # Read from input topic
    consumer = KafkaConsumer('input-topic')
    producer = KafkaProducer()
    
    for message in consumer:
        # Process event
        processed = process_event(message.value)
        
        # Send to output topic
        producer.send('output-topic', value=processed)
```

### Best Practices

- **Partition Key**: Use consistent keys to ensure ordering
- **Replication**: Set replication-factor >= 2 for production
- **Consumer Groups**: Use consumer groups for parallel processing
- **Error Handling**: Implement retry logic and dead-letter queues
- **Monitoring**: Track lag, throughput, and error rates

---

**Last updated**: April 12, 2026
