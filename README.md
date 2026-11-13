# 🔬 AI Research Assistant
### AI-Powered Literature Discovery using OpenAlex, RAG & 8 Intelligent Agents

An AI-powered research assistant that automates scientific literature discovery and analysis. Users can enter a research topic, retrieve relevant academic papers using the OpenAlex API, and generate structured research insights through Retrieval-Augmented Generation (RAG) and eight specialized AI agents.

---

## 📌 Project Overview

Researchers often face information overload due to the growing number of academic publications. Manually searching, reading, comparing, and identifying research gaps across multiple papers is time-consuming.

The **AI Research Assistant** simplifies this process by combining academic paper retrieval, semantic search, and LLM-powered analysis into a single application.

### Key Objectives

- Automate academic paper discovery.
- Retrieve relevant research papers based on user queries.
- Generate context-aware answers using RAG.
- Identify research gaps, limitations, and emerging trends.
- Automate literature reviews and paper comparisons.
- Provide structured research insights through specialized AI agents.

---

## ✨ Key Features

- **Research Paper Discovery:** Fetch relevant academic papers using the OpenAlex API.
- **Abstract Extraction:** Extract paper metadata and reconstruct abstracts from OpenAlex's inverted index.
- **Semantic Search:** Generate embeddings using HuggingFace sentence-transformer models.
- **Vector Database:** Store and retrieve relevant research documents using ChromaDB.
- **Multi-Agent Analysis:** Generate eight different types of research insights.
- **Context-Grounded Responses:** Provide retrieved research context to LLM agents to reduce hallucinations.
- **Response Caching:** Cache repeated LLM calls using Streamlit caching.

---

## 🏗️ System Architecture

The application consists of three major modules:

### 1. Research Module

Uses the OpenAlex API to discover academic research papers.

Workflow:
1. Accept a research topic from the user.
2. Send the topic to the OpenAlex `/works` endpoint.
3. Retrieve the top 5 relevant papers.
4. Extract titles, authors, and publication years.
5. Reconstruct abstracts from the inverted index.
6. Retain up to 1,000 characters of each abstract.

### 2. RAG Module

Uses Retrieval-Augmented Generation to provide relevant research context to AI agents.

**Workflow:**

1. Convert retrieved papers into LangChain Documents.
2. Generate vector embeddings using `all-MiniLM-L6-v2`.
3. Store document vectors in ChromaDB.
4. Perform semantic similarity search.
5. Retrieve the top 2 relevant matches.
6. Pass the retrieved context to the specialized AI agents.

**Why RAG?**
- Grounds LLM responses in retrieved academic literature.
- Reduces unsupported or irrelevant answers.
- Provides focused context for research analysis.
- Avoids relying entirely on the LLM's internal knowledge.

### 3. Multi-Agent Analysis Module

The system contains eight specialized agents, each responsible for a different research task.

| Agent | Responsibility |
|---|---|
| Research Analysis Agent | Identifies findings, methodologies, strengths, and applications. |
| Citation Agent | Extracts paper titles, authors, and publication years. |
| Gap Detector Agent | Identifies research gaps, limitations, and open problems. |
| Literature Review Agent | Generates a structured literature review from introduction to conclusion. |
| Trend Analysis Agent | Analyzes publication trends based on publication years. |
| Summarizer Agent | Summarizes objectives, methodologies, and key findings. |
| Comparison Agent | Compares research methodologies, strengths, and limitations. |
| Knowledge Discovery Agent | Identifies emerging trends and potential future research directions. |

---

## 🔄 How the System Works

```text
             USER INPUT
          Research Topic
                 |
                 v
         OPENALEX API
                 |
                 v
       Retrieve Top 5 Papers
                 |
                 v
       Extract Paper Metadata
       + Reconstruct Abstracts
                 |
                 v
         LANGCHAIN DOCUMENTS
                 |
                 v
       HUGGINGFACE EMBEDDINGS
          all-MiniLM-L6-v2
                 |
                 v
            CHROMADB
          Vector Storage
                 |
                 v
       Semantic Similarity Search
          Retrieve Top 2
                 |
                 v
          GROQ LLM
        openai/gpt-oss-20b
                 |
                 v
        8 SPECIALIZED AGENTS
                 |
                 v
       STRUCTURED RESEARCH
             INSIGHTS
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| OpenAlex API | Academic research paper discovery |
| LangChain | Document processing and retrieval |
| HuggingFace | Text embedding generation |
| all-MiniLM-L6-v2 | Sentence embedding model |
| ChromaDB | Vector database |
| Groq | LLM inference |
| openai/gpt-oss-20b | Language model used by agents |

---

## ⚙️ LLM Configuration

The project uses the Groq inference platform to execute LLM-powered research agents.

**Model:** `openai/gpt-oss-20b`

Configuration:
- Temperature: `0.2`
- Automatic retries: Up to 3 attempts
- Response caching: `st.cache_data`

The Trend Analysis Agent is an exception: it uses Python's `Counter` to analyze publication-year frequencies instead of making an LLM call.


## 🚀 Installation & Setup

### Prerequisites

- Python 3.10+
- Groq API key
- Internet connection

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/AI-Research-Assistant.git

cd AI-Research-Assistant
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:

https://console.groq.com/keys

**Important:** Never upload your `.env` file or expose your API key on GitHub.

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Expected Outputs

For a given research topic, the application generates:

1. Research findings and methodological analysis.
2. Extracted citation information.
3. Research gaps and limitations.
4. Structured literature review.
5. Publication trend analysis.
6. Individual paper summaries.
7. Comparative research analysis.
8. Emerging research directions and future opportunities.

---

## 🔮 Future Enhancements

- Full-text PDF ingestion and analysis.
- Integration with additional research sources such as arXiv.
- Export literature reviews to Word and PDF.
- Saved research queries and search history.
- Improved multi-paper comparison.
- Citation network analysis.
- Advanced research recommendation capabilities.

---

## 🎯 Project Highlights

- Combines academic literature discovery with RAG.
- Uses semantic retrieval instead of simple keyword matching.
- Implements eight specialized research analysis agents.
- Uses Groq for fast LLM inference.
- Integrates OpenAlex for real academic paper metadata.
- Provides an interactive browser-based interface using Streamlit.

---

## 👨‍💻 Author

**Syed Abdul Kathir**

B.Tech – Artificial Intelligence and Data Science

---

## 📜 License

This project is intended for educational and research purposes. Add an appropriate open-source license before distributing the repository.

---

⭐ If you find this project useful, consider giving the repository a star!
