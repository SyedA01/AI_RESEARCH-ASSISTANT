import pandas as pd
import streamlit as st
import time

from AI_research_assistant import (
    search_papers,
    create_documents,
    create_vector_db,
    retrieve_context,
    analyze_research,
    extract_citations,
    detect_gaps,
    generate_review,
    analyze_trends,
    summarize_papers,
    compare_papers,
    knowledge_discovery
)

# =================================
# PAGE CONFIG
# =================================

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide"
)

st.title(
    "📚 AI Research Assistant"
)

st.write(
    "Academic RAG powered by LangChain and Ollama"
)

# =================================
# TOPIC INPUT
# =================================

topic = st.text_input(
    "Research Topic"
)

# =================================
# MAIN WORKFLOW
# =================================

if st.button(
    "Generate Report"
):

    with st.spinner(
        "Searching papers..."
    ):

        papers = search_papers(
            topic
        )

        docs = create_documents(
            papers
        )

        db = create_vector_db(
            docs
        )

        context = retrieve_context(
            db,
            topic
        )

        
         
# =================================
# TABS
# =================================

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8= st.tabs(
            [
                "Analysis",
                "Literature Review",
                "Citations",
                "Research Gaps",
                "Trends",
                "Paper Summaries",
                "Research Comparison",
                "Knowledge Discovery"
                
            ]
        )
    
# =================================
# ANALYSIS TAB
# =================================

        with tab1:
            start = time.time()
            
            st.write("Research analysis...")
            analysis = analyze_research(
                        topic,
                        context
                    )
            
            st.write(
        f"Completed in {time.time()-start:.2f} seconds"
                    )
            
            st.write(
                    "Context length:",
                    len(context)
                )

            st.markdown(
                analysis
            )
        
# =================================
# REVIEW TAB
# =================================

        with tab2:
            start = time.time()
            st.write("Generating review...")
            review = generate_review(
                        topic,
                        context
                    )
            
            st.write(
        f"Completed in {time.time()-start:.2f} seconds"
        )

            st.markdown(
                review
            )
        
# =================================
# CITATIONS TAB
# =================================

        with tab3:
            start = time.time()
            st.write("Citation extraction...")
            citations = extract_citations(
                        context
                    )
            
            st.write(
        f"Completed in {time.time()-start:.2f} seconds"
    )

            st.markdown(
                citations
                )
        
# =================================
# GAPS TAB
# =================================

        with tab4:
            start = time.time()
            st.write("Detecting gaps...")
            gaps = detect_gaps(
                        context
                    )
            
            st.write(
        f"Completed in {time.time()-start:.2f} seconds"
    )

            st.markdown(
                gaps
            )
        
# =================================
# TRENDS TAB
# =================================

        with tab5:
            start = time.time()
            st.write("Analyizing trends...")
            trends = analyze_trends(
                        papers
                    )
            
            st.write(
        f"Completed in {time.time()-start:.2f} seconds"
    )

            trend_df = pd.DataFrame(
                list(trends.items()),
                columns=[
                    "Year",
                    "Paper Count"
                ]
            )

            st.line_chart(
                trend_df.set_index(
                    "Year"
                )
            )

            st.dataframe(
                trend_df
            )
        
# =================================
# PAPER SUMMARIES TAB
# =================================

        with tab6:
            start = time.time()
            st.write("Summarize papers...")
            paper_summaries = summarize_papers(
                        context
                    )
            
            st.write(
        f"Completed in {time.time()-start:.2f} seconds"
    )

            st.subheader(
                "Paper Summaries"
            )

            st.markdown(
                paper_summaries
            )
    
# =================================
# RESEARCH COMPARISON TAB
# =================================

        with tab7:
            start = time.time()
            st.write("Running Comparison...")
            research_comparison = compare_papers(
                        context
                    )
            
            st.write(
        f"Completed in {time.time()-start:.2f} seconds"
    )

            st.subheader(
                "Research Comparison"
            )

            st.markdown(
                research_comparison
            )
    
# =================================
# KNOWLEDGE DISCOVERY TAB
# =================================

        with tab8:
            start = time.time()
            st.write("knowledge discovery...")
            discovery = knowledge_discovery(
                        context
                    )
            
            st.write(
        f"Completed in {time.time()-start:.2f} seconds"
            )
            
            st.write(
                    "Context length:",
                    len(context)
                )

            st.subheader(
                "Knowledge Discovery"
            )

            st.markdown(
                discovery
            )