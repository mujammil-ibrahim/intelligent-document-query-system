import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Intelligent Document Query System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Intelligent Document Query System")
st.write("Upload a PDF and ask questions using AI.")

# -------------------------------
# Upload PDF
# -------------------------------

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    if st.button("Upload"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file,
                "application/pdf"
            )
        }

        with st.spinner("Uploading PDF..."):

            response = requests.post(
                f"{API_URL}/upload",
                files=files
            )

        if response.status_code == 200:
            st.success("✅ PDF uploaded successfully!")
        else:
            st.error(response.text)

st.divider()

# -------------------------------
# Session State
# -------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# Ask Question
# -------------------------------

question = st.text_input("Ask a question")

if st.button("Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("🤖 Thinking..."):

            response = requests.post(
                f"{API_URL}/query",
                json={
                    "question": question
                }
            )

        if response.status_code == 200:

            data = response.json()

            answer = data["answer"]
            chunks = data["chunks"]

            # Save User Message
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            # Save AI Message
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                    "chunks": chunks
                }
            )

        else:
            st.error(response.text)

# -------------------------------
# Conversation
# -------------------------------

if st.session_state.messages:

    st.subheader("💬 Conversation")

    for message in st.session_state.messages:

        if message["role"] == "user":

            with st.chat_message("user"):
                st.write(message["content"])

        else:

            with st.chat_message("assistant"):

                st.write(message["content"])

                if "chunks" in message:

                    with st.expander("📄 Retrieved Context"):

                        for i, chunk in enumerate(message["chunks"], start=1):

                            st.markdown(f"### Chunk {i}")

                            # Distance returned by pgvector
                            st.caption(
                                f"Match Distance: {chunk['similarity']:.2f} (Lower is better)"
                            )

                            st.write(chunk["text"])

                            st.divider()