---
layout: default
title: "MongoDB & AI Use Cases"
---

# 🗄️ MongoDB & AI: Real-World Applications

MongoDB's flexible schema and document-based architecture make it an ideal database for AI and machine learning applications. This guide explores practical use cases where MongoDB powers AI systems.

## Table of Contents

1. [Why MongoDB for AI](#why-mongodb-for-ai)
2. [Enterprise AI Use Cases](#enterprise-ai-use-cases)
3. [Personalization & Recommendation Engines](#personalization--recommendation-engines)
4. [Content Management & Search](#content-management--search)
5. [Real-Time Analytics](#real-time-analytics)
6. [Fraud Detection & Security](#fraud-detection--security)
7. [IoT & Time-Series Data](#iot--time-series-data)
8. [Implementation Patterns](#implementation-patterns)

---

## 🎯 Why MongoDB for AI

### Flexibility & Scalability

**Document-Based Storage:**
- Schema flexibility for evolving AI data models
- Store diverse data types: text, images, embeddings, vectors
- No rigid table structures limiting AI model experimentation

**Vector Search Capabilities:**
```javascript
// MongoDB Atlas Vector Search
db.products.search({
  "cosmosearch": {
    "vector": [0.019, 0.092, -0.031, ...],
    "k": 10
  }
})
```

### Key Advantages for AI

| Feature | Benefit |
|---------|---------|
| **Dynamic Schema** | Adapt data structure as models evolve |
| **Horizontal Scaling** | Handle massive training datasets |
| **Vector Indexing** | Fast similarity search for embeddings |
| **Real-time Updates** | Live model feature generation |
| **Aggregation Pipeline** | Complex data transformations for features |
| **TTL Indexes** | Automatic cleanup of old predictions |

---

## 💼 Enterprise AI Use Cases

### 1. Intelligent Document Processing

**Problem:** Extract structured data from unstructured documents

**Solution with MongoDB:**
```javascript
// Store document metadata and extracted data
db.documents.insertOne({
  _id: ObjectId(),
  filename: "invoice_2024.pdf",
  raw_text: "Invoice #12345...",
  extracted_data: {
    invoice_number: "12345",
    customer_name: "Acme Corp",
    total_amount: 5000,
    items: [
      { sku: "ABC123", quantity: 5, price: 100 }
    ]
  },
  confidence_scores: {
    invoice_number: 0.99,
    customer_name: 0.95,
    total_amount: 0.98
  },
  processed_at: new Date(),
  model_version: "ocr-v2.1"
})
```

**Real-World Impact:**
- Reduce manual data entry by 95%
- Process invoices, receipts, forms in minutes
- Audit trail with extracted confidence scores

### 2. Smart Search & Discovery

**Problem:** Traditional keyword search misses semantic meaning

**Solution: Vector Embeddings**
```python
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer

client = MongoClient("mongodb://...")
db = client["ecommerce"]
products_col = db["products"]

# Generate embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

for product in products_col.find():
    description = product.get("description", "")
    embedding = model.encode(description).tolist()
    
    products_col.update_one(
        {"_id": product["_id"]},
        {"$set": {"description_embedding": embedding}}
    )

# Vector search for similar products
query_embedding = model.encode("waterproof hiking boots").tolist()
similar_products = products_col.aggregate([
    {
        "$search": {
            "cosmosearch": {
                "vector": query_embedding,
                "path": "description_embedding",
                "k": 5
            }
        }
    }
])
```

---

## 🎁 Personalization & Recommendation Engines

### E-Commerce Recommendations

**Store User Behavior & Preferences:**
```javascript
db.user_profiles.insertOne({
  _id: ObjectId(),
  user_id: "user_123",
  preferences: {
    size: "M",
    color: "blue",
    brand_preferences: ["Nike", "Adidas"],
    price_range: { min: 50, max: 150 }
  },
  browsing_history: [
    {
      product_id: "prod_456",
      timestamp: new Date("2024-01-15T10:30:00"),
      time_spent: 45000, // ms
      action: "view"
    },
    {
      product_id: "prod_789",
      timestamp: new Date("2024-01-15T11:00:00"),
      time_spent: 120000,
      action: "add_to_cart"
    }
  ],
  purchase_history: [
    {
      order_id: "order_abc",
      products: [
        { product_id: "prod_111", quantity: 1, category: "shoes" }
      ],
      total: 89.99,
      date: new Date("2024-01-10")
    }
  ],
  embeddings: {
    preference_vector: [0.12, -0.45, 0.67, ...],
    behavior_vector: [0.23, 0.34, -0.12, ...]
  },
  last_updated: new Date()
})
```

**Collaborative Filtering Query:**
```javascript
// Find similar users
db.user_profiles.find({
  "embeddings.preference_vector": {
    $nearSphere: {
      $geometry: {
        type: "Point",
        coordinates: [0.12, -0.45, 0.67] // target user's vector
      },
      $maxDistance: 0.5
    }
  }
}).limit(10)
```

### Content Recommendation System

**Store Content Features:**
```javascript
db.content.insertOne({
  _id: ObjectId(),
  title: "10 Best Hiking Trails 2024",
  category: "travel",
  tags: ["hiking", "nature", "adventure"],
  author: "travel_expert_1",
  engagement_metrics: {
    views: 15000,
    shares: 450,
    likes: 2000,
    average_read_time: 8.5 // minutes
  },
  content_embedding: [0.23, 0.45, -0.12, ...],
  topics: {
    outdoor_activities: 0.9,
    fitness: 0.6,
    travel: 0.95,
    photography: 0.4
  },
  published_at: new Date("2024-01-20"),
  expires_at: new Date("2024-12-31")
})

// TTL index for auto-expiring content
db.content.createIndex({ expires_at: 1 }, { expireAfterSeconds: 0 })
```

---

## 🔍 Content Management & Search

### Multi-Language Content Search

**Problem:** Need semantic search across multiple languages

**Solution:**
```javascript
db.articles.insertOne({
  _id: ObjectId(),
  title_en: "Understanding Machine Learning",
  title_es: "Entendiendo el Aprendizaje Automático",
  title_ja: "機械学習について",
  content_en: "Machine learning is...",
  content_es: "El aprendizaje automático es...",
  
  // Multi-language embeddings
  embeddings: {
    en: [0.12, 0.34, -0.45, ...],
    es: [0.15, 0.31, -0.42, ...],
    ja: [0.14, 0.33, -0.43, ...]
  },
  
  text_index_keywords: [
    "machine learning", "artificial intelligence",
    "aprendizaje automático", "inteligencia artificial"
  ]
})

// Compound index for efficient search
db.articles.createIndex({
  "title_en": "text",
  "content_en": "text",
  "title_es": "text",
  "content_es": "text"
})
```

### FAQ & Similar Question Matching

**Store Questions with Embeddings:**
```python
from pymongo import MongoClient
import numpy as np

client = MongoClient("mongodb://...")
db = client["support_system"]
faqs = db["faqs"]

# Find similar historical questions
user_question = "How do I reset my password?"
user_embedding = model.encode(user_question).tolist()

# Use aggregation pipeline
pipeline = [
    {
        "$addFields": {
            "similarity": {
                "$function": {
                    "body": """
                    function(qvec1, qvec2) {
                        var dot = 0, i, len = qvec1.length;
                        for (i = 0; i < len; i++) dot += qvec1[i] * qvec2[i];
                        var norma = Math.sqrt(qvec1.reduce((s,n) => s+n*n, 0));
                        var normb = Math.sqrt(qvec2.reduce((s,n) => s+n*n, 0));
                        return dot / (norma * normb);
                    }
                    """,
                    "args": [user_embedding, "$question_embedding"],
                    "lang": "js"
                }
            }
        }
    },
    { "$sort": { "similarity": -1 } },
    { "$limit": 5 }
]

similar_faqs = list(faqs.aggregate(pipeline))
```

---

## 📊 Real-Time Analytics

### Live Dashboard Data

**Event Streaming & Aggregation:**
```javascript
// Insert real-time events
db.events.insertOne({
  _id: ObjectId(),
  timestamp: new Date(),
  event_type: "purchase",
  user_id: "user_123",
  product_id: "prod_456",
  amount: 79.99,
  device: "mobile",
  location: {
    country: "US",
    city: "New York"
  }
})

// Real-time aggregation
db.events.aggregate([
  {
    $match: {
      timestamp: {
        $gte: new Date(Date.now() - 3600000) // Last hour
      }
    }
  },
  {
    $group: {
      _id: {
        event_type: "$event_type",
        hour: { $hour: "$timestamp" }
      },
      count: { $sum: 1 },
      total_revenue: { $sum: "$amount" }
    }
  },
  {
    $sort: { "_id.hour": -1 }
  }
])
```

### Model Performance Tracking

**Store Predictions & Metrics:**
```javascript
db.predictions.insertOne({
  _id: ObjectId(),
  model_id: "churn_prediction_v3",
  model_version: "3.2.1",
  prediction_type: "churn",
  
  input: {
    user_id: "user_123",
    features: {
      days_since_signup: 180,
      purchases: 5,
      avg_session_duration: 45,
      support_tickets: 2
    }
  },
  
  output: {
    prediction: 0.78, // 78% churn likelihood
    confidence: 0.91,
    predicted_class: "will_churn"
  },
  
  metrics: {
    precision: 0.92,
    recall: 0.87,
    f1_score: 0.89,
    auc_roc: 0.93
  },
  
  timestamp: new Date(),
  
  actual_outcome: {
    churned: false, // Will be updated after 30 days
    verified_at: new Date("2024-02-15")
  }
})

// Track model drift
db.model_metrics.insertOne({
  model_id: "churn_prediction_v3",
  date: new Date("2024-01-20"),
  performance: {
    accuracy: 0.88,
    precision: 0.91,
    recall: 0.85,
    f1: 0.88
  },
  data_distribution: {
    mean_age: 35.2,
    median_purchases: 4,
    churn_rate: 0.12
  }
})
```

---

## 🛡️ Fraud Detection & Security

### Anomaly Detection Pipeline

**Store Transaction Features:**
```javascript
db.transactions.insertOne({
  _id: ObjectId(),
  transaction_id: "txn_xyz789",
  user_id: "user_123",
  timestamp: new Date(),
  
  transaction_details: {
    amount: 1999.99,
    merchant: "electronics_store",
    category: "electronics",
    merchant_country: "US",
    card_country: "US"
  },
  
  user_profile: {
    avg_transaction: 85.50,
    max_transaction: 500,
    typical_merchants: ["grocery", "gas", "coffee"],
    device_fingerprint: "device_hash_123",
    location_history: [
      { lat: 40.7128, lng: -74.0060, timestamp: "2024-01-19T10:00:00" }
    ]
  },
  
  risk_score: {
    amount_anomaly: 0.8,
    merchant_anomaly: 0.9,
    location_anomaly: 0.1,
    device_anomaly: 0.2,
    overall_risk: 0.65 // Threshold: 0.7
  },
  
  model_decision: "review", // "approve", "deny", "review"
  reviewed_at: null,
  human_decision: null
})

// Create index for fast lookups
db.transactions.createIndex({ user_id: 1, timestamp: -1 })
db.transactions.createIndex({ "risk_score.overall_risk": 1 })
```

**Real-Time Fraud Alerts:**
```python
from pymongo import MongoClient
from pymongo.monitoring import DatabaseListener
import asyncio

client = MongoClient("mongodb://...")
db = client["payments"]

# Watch for high-risk transactions
with db.transactions.watch([
    {
        "$match": {
            "operationType": "insert",
            "fullDocument.risk_score.overall_risk": { "$gte": 0.7 }
        }
    }
]) as stream:
    for change in stream:
        txn = change["fullDocument"]
        print(f"🚨 High Risk Transaction: {txn['transaction_id']}")
        print(f"   Risk Score: {txn['risk_score']['overall_risk']}")
        print(f"   Amount: ${txn['transaction_details']['amount']}")
        # Send alert to fraud team
```

---

## 📡 IoT & Time-Series Data

### Sensor Data Storage & Analysis

**Store Time-Series Metrics:**
```javascript
db.sensor_data.insertOne({
  _id: ObjectId(),
  device_id: "sensor_001",
  device_type: "temperature_humidity",
  location: {
    factory: "plant_a",
    floor: 3,
    room: "warehouse"
  },
  
  // Bucketed time-series data
  timestamp: new Date("2024-01-20T15:00:00"),
  measurements: [
    {
      temperature: 22.5,
      humidity: 45.2,
      timestamp: new Date("2024-01-20T15:00:00")
    },
    {
      temperature: 22.6,
      humidity: 45.1,
      timestamp: new Date("2024-01-20T15:01:00")
    }
  ],
  
  // Daily aggregates
  daily_stats: {
    avg_temperature: 22.3,
    max_temperature: 25.1,
    min_temperature: 20.8,
    avg_humidity: 45.5,
    anomalies_detected: 2
  },
  
  expiry: new Date("2024-02-20") // TTL for old data
})

// TTL index - auto-delete old records after 30 days
db.sensor_data.createIndex(
  { expiry: 1 },
  { expireAfterSeconds: 0 }
)
```

### Predictive Maintenance

**Store Equipment Health Metrics:**
```javascript
db.equipment.insertOne({
  _id: ObjectId(),
  equipment_id: "pump_001",
  equipment_type: "centrifugal_pump",
  
  current_status: {
    operational_hours: 8750,
    state: "normal", // "normal", "warning", "critical"
    efficiency: 0.92,
    last_maintenance: new Date("2023-12-15")
  },
  
  health_indicators: {
    vibration_level: 4.2, // mm/s
    temperature: 72.5, // °C
    pressure: 98.5, // PSI
    flow_rate: 250.0 // GPM
  },
  
  prediction: {
    model_version: "maintenance_v4",
    rul: 450, // Remaining Useful Life in hours
    failure_probability: 0.15,
    recommended_action: "schedule_maintenance",
    confidence: 0.88
  },
  
  maintenance_history: [
    {
      date: new Date("2023-12-15"),
      type: "seal_replacement",
      technician: "john_doe",
      hours_since_start: 8400,
      notes: "Replaced pump seals and bearing lubrication"
    }
  ],
  
  last_updated: new Date()
})
```

---

## 🛠️ Implementation Patterns

### Pattern 1: Feature Store with MongoDB

**Centralized Feature Management:**
```python
from pymongo import MongoClient
from datetime import datetime, timedelta

class FeatureStore:
    def __init__(self, mongo_uri):
        self.client = MongoClient(mongo_uri)
        self.db = self.client["feature_store"]
        self.features = self.db["features"]
        self.feature_logs = self.db["feature_logs"]
    
    def store_feature(self, entity_id, feature_name, value, version="1.0"):
        """Store feature with versioning"""
        self.features.update_one(
            {
                "entity_id": entity_id,
                "feature_name": feature_name
            },
            {
                "$set": {
                    "value": value,
                    "version": version,
                    "updated_at": datetime.now()
                }
            },
            upsert=True
        )
        
        # Log for audit trail
        self.feature_logs.insert_one({
            "entity_id": entity_id,
            "feature_name": feature_name,
            "value": value,
            "version": version,
            "timestamp": datetime.now()
        })
    
    def get_features(self, entity_id, feature_names=None):
        """Retrieve features for entity"""
        query = {"entity_id": entity_id}
        if feature_names:
            query["feature_name"] = {"$in": feature_names}
        
        return list(self.features.find(query, {"_id": 0}))

# Usage
fs = FeatureStore("mongodb://...")
fs.store_feature("user_123", "purchase_frequency", 5.2)
features = fs.get_features("user_123")
```

### Pattern 2: Model Registry

**Track All Model Versions:**
```javascript
db.model_registry.insertOne({
  _id: ObjectId(),
  model_name: "churn_predictor",
  version: "3.2.1",
  
  model_info: {
    type: "random_forest",
    framework: "scikit-learn",
    input_features: [
      "days_active",
      "purchase_count",
      "avg_session_duration"
    ],
    target_variable: "churned"
  },
  
  performance: {
    accuracy: 0.88,
    precision: 0.91,
    recall: 0.85,
    f1: 0.88,
    auc_roc: 0.93
  },
  
  training: {
    dataset_version: "production_v2",
    training_date: new Date("2024-01-15"),
    training_rows: 100000,
    features_engineered_by: "data_team"
  },
  
  deployment: {
    status: "active",
    deployed_at: new Date("2024-01-16"),
    deployment_env: "production",
    served_by: "model_service_v2"
  },
  
  monitoring: {
    last_checked: new Date(),
    performance_drift: 0.02,
    data_drift: 0.05,
    alerts_configured: true
  }
})
```

### Pattern 3: Prediction Cache

**Store Recent Predictions:**
```python
import hashlib
from datetime import datetime, timedelta

class PredictionCache:
    def __init__(self, mongo_client):
        self.db = mongo_client["prediction_cache"]
        self.cache = self.db["predictions"]
        # TTL index - cache expires after 24 hours
        self.cache.create_index(
            "created_at",
            expireAfterSeconds=86400
        )
    
    def get_or_predict(self, user_id, features, model_fn):
        """Get cached prediction or generate new"""
        # Create feature hash
        feature_hash = hashlib.md5(
            str(sorted(features.items())).encode()
        ).hexdigest()
        
        cache_key = f"{user_id}:{feature_hash}"
        
        # Check cache
        cached = self.cache.find_one({"_id": cache_key})
        if cached:
            return cached["prediction"]
        
        # Generate prediction
        prediction = model_fn(features)
        
        # Store in cache
        self.cache.insert_one({
            "_id": cache_key,
            "user_id": user_id,
            "features": features,
            "prediction": prediction,
            "created_at": datetime.now()
        })
        
        return prediction
```

---

## 🎓 Best Practices

### Data Management

1. **Embedding Storage**
   - Store embeddings as arrays for fast vector search
   - Use indexes for similarity queries
   - Consider dimensionality reduction for large embeddings

2. **TTL Policies**
   ```javascript
   // Auto-delete predictions older than 90 days
   db.predictions.createIndex(
     { created_at: 1 },
     { expireAfterSeconds: 7776000 }
   )
   ```

3. **Schema Versioning**
   - Track model versions in predictions
   - Document schema changes in migrations
   - Maintain backward compatibility

### Query Optimization

1. **Compound Indexes**
   ```javascript
   // Optimize common queries
   db.transactions.createIndex({
     user_id: 1,
     timestamp: -1,
     status: 1
   })
   ```

2. **Aggregation Pipeline**
   - Use stages in correct order: $match → $group → $sort
   - Move $match as early as possible
   - Avoid $lookup with large collections

3. **Vector Search Indexing**
   ```javascript
   // Create vector search index
   db.products.createIndex({
     product_embedding: "cosmosearch"
   })
   ```

### Monitoring & Maintenance

1. **Track Model Performance**
   - Store accuracy metrics over time
   - Alert on performance degradation
   - Version all model changes

2. **Data Quality Checks**
   - Validate input feature ranges
   - Monitor for data drift
   - Log anomalies for investigation

3. **Clean Up**
   - Use TTL indexes for temporary data
   - Archive old predictions quarterly
   - Monitor disk usage

---

## 📚 Related Resources

- [MongoDB Atlas Vector Search](https://www.mongodb.com/docs/atlas/atlas-vector-search/)
- [Aggregation Framework](https://www.mongodb.com/docs/manual/aggregation/)
- [Time-Series Collections](https://www.mongodb.com/docs/manual/core/timeseries-collections/)
- [Full-Text Search](https://www.mongodb.com/docs/manual/reference/operator/query/text/)

---

**Last Updated:** January 2024 | **Difficulty:** Advanced
