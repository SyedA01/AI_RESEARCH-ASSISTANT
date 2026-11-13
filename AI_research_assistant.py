import pandas as pd
import streamlit as st
import requests
import os

from collections import Counter
from dotenv import load_dotenv
from langchain_core.documents import Document

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma

from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq

# =================================
# LLM
# =================================
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-20b"
)

if not API_KEY:
    raise ValueError("Groq_API_KEY is missing in .env")

@st.cache_resource
def load_llm():
    llm = ChatGroq(
        model=MODEL_NAME,
        groq_api_key=API_KEY,
        temperature=0.2,
        max_retries=3
    )
    return llm

llm = load_llm()

# =================================
# SEARCH PAPERS USING OPENALEX
# =================================

def search_papers(topic, max_results=5):

    url = "https://api.openalex.org/works"

    params = {
        "search": topic,
        "per-page": max_results
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return []

    data = response.json()

    papers = []

    for paper in data.get("results", []):

        title = paper.get("title", "N/A")

        authors = ", ".join(
            [
                author["author"]["display_name"]
                for author in paper.get("authorships", [])
                if "author" in author
            ]
        )

        year = paper.get("publication_year", "N/A")

        abstract = ""

        if paper.get("abstract_inverted_index"):

            inverted = paper["abstract_inverted_index"]

            words = sorted(
                [
                    (pos, word)
                    for word, positions in inverted.items()
                    for pos in positions
                ]
            )

            abstract = " ".join(
                [
                    word
                    for pos, word in words
                ]
            )

        papers.append(
            {
                "title": title,
                "authors": authors,
                "year": year,
                "summary": abstract[:1000]
            }
        )

    return papers

# =================================
# CREATE DOCUMENTS
# =================================

@st.cache_data
def create_documents(papers):

    documents = []

    for paper in papers:

        content = f"""
        Title: {paper['title']}

        Authors: {paper['authors']}

        Year: {paper['year']}

        Summary: {paper['summary']}
        """

        documents.append(
            Document(
                page_content=content
            )
        )

    return documents

# =================================
# CREATE VECTOR DATABASE
# =================================

@st.cache_resource
def create_vector_db(
        documents
):

    embeddings = HuggingFaceEmbeddings(
        model_name=
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        documents,
        embeddings
    )

    return db

# =================================
# CONTEXT RETRIEVAL
# =================================

def retrieve_context(db,topic):

    retriever = db.as_retriever(
        search_kwargs={"k":2}
    )

    docs = retriever.invoke(
        topic
    )

    context = "\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )
    
    return context[:1000]
# =================================
# RESEARCH ANALYSIS
# =================================

@st.cache_data
def analyze_research(
        topic,
        context
):

    prompt = f"""
    Research Topic:
    {topic}

    Context:
    {context}

    Explain:

    1. Major Findings

    2. Methodologies

    3. Strengths

    4. Weaknesses

    5. Applications
    """

    return llm.invoke(
        prompt
    ).content
    
# =================================
# CITATION AGENT
# =================================

@st.cache_data
def extract_citations(
        context
):

    prompt = f"""
    Extract paper citations.

    Context:
    {context}

    Return:

    Title

    Authors

    Year
    """

    return llm.invoke(
        prompt
    ).content
    
# =================================
# GAP DETECTOR
# =================================

@st.cache_data
def detect_gaps(
        context
):

    prompt = f"""
    Identify:

    1. Research Gaps

    2. Limitations

    3. Unsolved Problems

    4. Future Opportunities

    Context:
    {context}
    """

    return llm.invoke(
        prompt
    ).content
    
# =================================
# LITERATURE REVIEW
# =================================

@st.cache_data
def generate_review(
        topic,
        context
):

    prompt = f"""
    Generate a literature review.

    Topic:
    {topic}

    Context:
    {context}

    Include:

    Introduction

    Related Work

    Findings

    Challenges

    Future Scope

    Conclusion
    """

    return llm.invoke(
        prompt
    ).content
    
# =================================
# TREND ANALYSIS
# =================================

@st.cache_data
def analyze_trends(papers):

    years = []

    for paper in papers:

        years.append(paper["year"])

    return dict(Counter(years))

# =================================
# PAPER SUMMARIZATION
# =================================

@st.cache_data
def summarize_papers(context):

    prompt = f"""
    Summarize each research paper separately.

    Context:
    {context}

    For each paper provide:

    - Title
    - Objective
    - Method
    - Key Findings
    """

    return llm.invoke(prompt).content

# =================================
# RESEARCH COMPARISION
# =================================

@st.cache_data
def compare_papers(context):

    prompt = f"""
    Compare the research papers.

    Include only:
    - Method
    - Strength
    - Limitation
    
    Context:
    {context}
    """

    return llm.invoke(prompt).content

# =================================
# KNOWLEDGE DISCOVERY
# =================================

@st.cache_data
def knowledge_discovery(context):

    prompt = f"""
    Discover hidden insights.

    Context:
    {context}

    Identify:
        1. Emerging Trends
        2. Research Gaps
        3. Future Directions

        Keep answer under 300 words.
    """

    return llm.invoke(prompt).content