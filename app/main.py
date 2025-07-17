import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.rag_engine import stream_rag_response

# Main app function
def main():
    st.title("Local RAG Assistant")
    user_input = st.text_input("Ask a question:")

    if user_input:
        with st.spinner("Thinking..."):
            response_placeholder = st.empty()
            streamed_text = ""
            for chunk in stream_rag_response(user_input):
                streamed_text += chunk
                response_placeholder.markdown(streamed_text + "...")
            response_placeholder.markdown(streamed_text)

if __name__ == "__main__":
    main()
