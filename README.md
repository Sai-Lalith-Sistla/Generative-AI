# 🚀 Zero to Gen AI

A curated journey from foundational GenAI concepts to hands-on implementation of advanced agentic design patterns.

This repository is a personal learning archive and a practical resource for understanding and experimenting with **Generative AI** concepts, including **semantic search**, **transformers**, and **agentic workflows** using tools like BERT, GPT-2, and AutoGen.

---

## 📚 Contents

### 🧠 Gen AI Basics

Explore how core GenAI components work behind the scenes.

- 🔍 **Chunking, Embeddings & Semantic Search on Wikipedia Pages**  
  Learn how to chunk large text, generate embeddings, and run semantic search using vector databases.

- 💼 **Semantic Search with Job Postings**  
  A hands-on use case of semantic retrieval applied to job descriptions and resume relevance.

- 🧾 **Vector Store Notes**  
  Notes and implementation insights on storing and retrieving text embeddings efficiently.

---

### 🤖 Transformer Models  
Deep dive into modern NLP using fine-tuned and pre-trained transformer models for various downstream tasks.

---

####  📊 Sentiment Analysis  
- **Fine-Tune BERT for Sentiment Analysis**  
  Fine-tuning BERT on IMDb movie reviews for binary sentiment classification.

- **Sentiment Analysis with RoBERTa**  
  Leverage a pre-trained RoBERTa model to classify text sentiment with improved contextual understanding.

- **Sentiment Analysis with Zero-Shot Classification**  
  Classify sentiments without task-specific training using zero-shot text classification with models like `facebook/bart-large-mnli`.

---

####  📚 Natural Language Inference (NLI)  
- **Zero-Shot Text Inference**  
  Perform zero-shot inference to determine textual entailment across multiple labels using `facebook/bart-large-mnli`.

---

####  🧠 Semantic Understanding  
- **Semantic Search with Sentence Transformers**  
  Build a semantic search system using Sentence-BERT (SBERT) by encoding text into dense embeddings and retrieving results with cosine similarity.

- **Text Clustering using Sentence Embeddings**  
  Cluster semantically similar texts using SBERT embeddings and unsupervised clustering algorithms like KMeans or HDBSCAN.

---

####  ❓ Question Answering  
- **Question Answering with BERT**  
  Extract precise answers from context passages using a fine-tuned BERT model for extractive QA tasks.

---

####  ✍️ Text Generation  
- **Text Generation with GPT-2**  
  Generate human-like text using GPT-2 and decoding strategies like greedy search, beam search, and top-k/top-p sampling.

---

### 🧪 LangChain Experiments  
Explore the power of **LangChain** through hands-on demonstrations covering conversational agents, image generation, memory, and retrieval-augmented generation (RAG).

---

#### 📘 00 Series – Foundations  
- **00a – OpenAI Chat with LangChain**  
  Create a basic chatbot interface using LangChain and OpenAI models.

- **00b – Google Search Integration**  
  Use LangChain to incorporate Google search for real-time query responses.

- **00c – Image Generation with DALL·E**  
  Generate images from prompts using DALL·E via LangChain integration.

---

#### 🧠 LLM & Memory  
- **01 – OpenAI Chat vs Generic LLMs**  
  Compare OpenAI models with other LLMs under the LangChain framework.

- **07 – LangChain Memory**  
  Demonstrate conversation continuity using different memory modules (e.g., `ConversationBufferMemory`, `ConversationSummaryMemory`).

---

#### 📚 RAG Workflow  
- **09 – Retrieval-Augmented Generation (RAG)**  
  End-to-end pipeline demonstrating:
  1. Document loading  
  2. Embedding generation  
  3. Vector storage using FAISS  
  4. Semantic retrieval and answer generation  

  > This notebook showcases how LangChain enables intelligent document-based Q&A using your own data.

---

> 💡 Each notebook is self-contained and annotated for easy understanding. Ideal for experimentation, learning, or extending into production-grade LLM apps.


---

### 🧩 AI Agentic Design Patterns (AutoGen)

Experimenting with multi-agent LLM-based workflows using **Microsoft AutoGen**.

- 🧑‍🤝‍🧑 **Multi-Agent Collaboration**  
  Build coordinated LLM agents that communicate and divide tasks effectively.

- 🔁 **Reflection**  
  Implement self-evaluation and iterative improvement in agent output.

- 🧰 **Tool Use**  
  Extend agent capabilities using external tools and APIs.

- 💻 **Code Generation**  
  AutoGen agents that can generate, critique, and refine code snippets in a feedback loop.

---

