---
layout: default
title: "NLP Fundamentals: Natural Language Processing"
---

# 🗣️ NLP Fundamentals: Natural Language Processing

Natural Language Processing is the cornerstone technology enabling computers to understand, interpret, and generate human language. It bridges the gap between human communication and machine understanding.

## Table of Contents

1. [NLP Basics](#nlp-basics)
2. [Core NLP Tasks](#core-nlp-tasks)
3. [Classical vs. Deep Learning NLP](#classical-vs-deep-learning-nlp)
4. [Popular NLP Techniques](#popular-nlp-techniques)
5. [NLP Pipeline](#nlp-pipeline)
6. [Applications](#applications)

---

## 🎯 NLP Basics

### What is NLP?

Natural Language Processing is an interdisciplinary field combining:
- **Linguistics**: Understanding language structure and meaning
- **Computer Science**: Algorithms for processing
- **Machine Learning**: Learning patterns from data
- **Statistics**: Probability and statistical models

### Why NLP is Hard

```
Challenges in NLP:

1. Ambiguity
   "I saw the man with the telescope"
   ├─ I used telescope to see man
   └─ I saw a man who had a telescope

2. Context Dependency
   "The bank is near the river"
   ├─ Financial institution
   └─ Earth beside river

3. Idioms & Metaphors
   "Break a leg" ≠ Literal bone fracture

4. Named Entities
   "Apple is looking into AI" - which Apple?

5. Evolving Language
   New slang, emojis, code-switching
```

---

## 📋 Core NLP Tasks

### **Text Classification**
Assigning content to categories
- Sentiment Analysis (positive/negative/neutral)
- Spam Detection
- Topic Classification
- Intent Recognition

### **Named Entity Recognition (NER)**
Identifying and classifying entities
```
Text: "Apple Inc. founded by Steve Jobs in Cupertino"
Entities:
- Apple Inc. → ORGANIZATION
- Steve Jobs → PERSON
- Cupertino → LOCATION
```

### **Information Extraction**
Pulling structured information from text
- Relationship extraction
- Event extraction
- Slot filling

### **Machine Translation**
Converting text between languages
- Google Translate
- Real-time translation
- Domain-specific translation

### **Question Answering**
Finding answers in text
- Document QA: Answer from given document
- Open-domain QA: Answer from web
- Clarification QA: Following up questions

### **Semantic Similarity**
Comparing meaning between texts
- Duplicate detection
- Paraphrase identification
- Semantic search

---

## 🔄 Classical vs. Deep Learning NLP

### Classical Approaches

**Bag of Words (BoW)**
- Each word as feature
- Position ignored
- Fast but information loss

**TF-IDF (Term Frequency-Inverse Document Frequency)**
- Weighted word importance
- Common in text retrieval
- Simple and interpretable

**N-grams**
- Sequences of N words
- Captures local context
- Used for language models

**Limitations**
- Loses word order and context
- No semantic understanding
- Manual feature engineering

### Deep Learning Approaches

**Word Embeddings (Word2Vec, GloVe)**
- Dense vector representations
- Captures semantic relationships
- "king - man + woman ≈ queen"

**Recurrent Neural Networks (LSTM, GRU)**
- Sequential processing
- Maintains context
- Good for variable-length text

**Transformers (BERT, GPT)**
- Parallel processing with attention
- Context from both directions
- State-of-the-art performance

**Modern Advantages**
- Automatic feature learning
- End-to-end training
- Contextual understanding
- Transfer learning capability

---

## 🛠️ Popular NLP Techniques

### **Tokenization**
Splitting text into meaningful units
```
Sent: "I can't believe it's not butter!"
Tokens: ["I", "ca", "n't", "believe", "it", "'s", "not", "butter", "!"]
```

### **Part-of-Speech Tagging**
Identifying word categories
```
"The quick brown fox"
The/DET quick/ADJ brown/ADJ fox/NOUN
```

### **Dependency Parsing**
Understanding grammatical relationships
```
"The dog ate the bone"
    ate (root)
   /  \
  dog bone
  |    |
 The  The
```

### **Sentiment Analysis**
Determining emotional tone
```
"This product is amazing!" → Positive (0.95)
"Terrible experience" → Negative (0.88)
```

### **Word Sense Disambiguation**
Resolving word meanings
```
"I'm going to the bank"
↓
Determining: Financial institution vs. river bank
```

---

## 🔄 Typical NLP Pipeline

```
Raw Text
   ↓
[Tokenization]     Break into tokens
   ↓
[Lowercasing]      Normalize case
   ↓
[Lemmatization]    Reduce to base form
   ↓
[Stop Word Removal] Remove common words
   ↓
[Feature Extraction] Create representations
   ├─ BoW, TF-IDF
   ├─ Word Embeddings
   └─ Contextual Embeddings
   ↓
[Model Processing]  Classification/Sequence models
   ↓
[Post-processing]   Format output
   ↓
Results
```

---

## 💡 Applications

### 1. **Search Engines**
- Query understanding
- Relevance ranking
- Auto-completion

### 2. **Conversational AI**
- Intent recognition
- Entity extraction
- Response generation

### 3. **Content Recommendation**
- Semantic similarity
- Topic modeling
- Personalization

### 4. **Information Extraction**
- Resume parsing
- Form filling
- Contract analysis

### 5. **Text Generation**
- Summarization
- Machine translation
- Paraphrase generation

### 6. **Accessibility**
- Text-to-speech
- Speech-to-text
- Document translation

---

## 📊 NLP Metrics

### Classification Tasks
- **Accuracy**: Correct predictions / Total
- **Precision**: True positives / Predicted positive
- **Recall**: True positives / Actual positive
- **F1 Score**: Harmonic mean of precision & recall

### Sequence Tasks
- **BLEU Score**: Machine translation quality
- **ROUGE**: Summarization evaluation
- **METEOR**: Semantic similarity in translation

### Perplexity
- Measures language model uncertainty
- Lower is better (model is more confident)

---

## 🎓 Learning Path

### Foundation
1. Tokenization and text preprocessing
2. BoW and TF-IDF
3. Sentiment analysis

### Intermediate
1. Word embeddings (Word2Vec, GloVe)
2. RNNs and LSTMs
3. Sequence-to-sequence models

### Advanced
1. Transformers and BERT
2. Transfer learning
3. Fine-tuning for specific tasks

---

## 🔗 Related Topics

- [LLM Fundamentals](./llm-fundamentals.md) - Modern NLP with transformers
- [Chatbots & Conversational AI](./chatbot-conversational-ai.md) - NLP in action
- [AI Agents](./ai-agents.md) - Using NLP for reasoning
- [LLM Architecture](./llm-architecture-deep-dive.md) - Deep transformer understanding

---

## 📚 Popular NLP Libraries

- **NLTK**: Classic NLP toolkit
- **spaCy**: Production-ready NLP
- **HuggingFace Transformers**: Pre-trained models
- **TextBlob**: Simple text processing
- **Gensim**: Topic modeling and embeddings
